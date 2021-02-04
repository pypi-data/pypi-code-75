"""Region Of Interest module."""

from copy import copy

import numpy as np

from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.collections import PatchCollection

from .abstract import AbstractItem, AbstractCollection
from .categories import (Category, CategoriesCollection,
                         SubCategory, SubCategoriesCollection)

from ..projections import Equirectangular
from ..trajectory import Trajectory


class ROI(AbstractItem):
    """Region Of Interest object.

    Parameters
    ----------
    key:
        Identification key.
    lons_e: [float, …]
        Polygon coordinates east longitudes.
    lats: [float, …]
        Polygon coordinates latitudes.
    name: str, optional
        Region name.
    **kwargs: str, optional
        Region description/Science objective/Observation requirement/Color.

    """

    def __init__(self, key, lons_e, lats, name=None, **kwargs):
        super().__init__(key, name=name, lons_e=lons_e, lats=lats, **kwargs)

        self.vertices = lons_e, lats

    def __call__(self, **kwargs):
        return self.patch(**kwargs)

    def __contains__(self, pt):
        return self.contains(pt).any()

    @property
    def vertices(self):
        """ROI vertices."""
        return self.__vertices

    @vertices.setter
    def vertices(self, lonlat):
        """Vertices setter.

        The vertices is automatically closed, if
        the first and last point are different.

        Parameters
        ----------
        lons_e: list
            East longitude (degrees).
        lats: list
            Latitude (degrees).

        Raises
        ------
        ValueError:
            If the east-longitude and latitude arrays are not the same
        """
        lons_e, lats = lonlat

        if isinstance(lons_e, (int, float)):
            lons_e = [lons_e]

        if isinstance(lats, (int, float)):
            lats = [lats]

        if len(lons_e) != len(lats):
            raise ValueError('Longitude and latitude vertices are not the same.')

        vert = np.transpose([lons_e, lats])

        # Close vertices if first and last points are not the same.
        if lons_e[0] != lons_e[-1] or lats[0] != lats[-1]:
            vert = np.vstack([
                vert,
                [lons_e[0], lats[0]],
            ])

        self.__vertices = vert

    @property
    def codes(self):
        """ROI path codes."""
        return None

    @property
    def path(self):
        """Region of interest path."""
        return Path(self.vertices, self.codes)

    def patch(self, **kwargs):
        """Region of interest patch with default color."""
        if 'color' in kwargs:
            kwargs['facecolor'] = kwargs['color']
            kwargs['edgecolor'] = kwargs['color']
            del kwargs['color']

        elif hasattr(self, 'color'):
            if 'facecolor' not in kwargs:
                kwargs['facecolor'] = self.get_fc()

            if 'edgecolor' not in kwargs:
                kwargs['edgecolor'] = self.get_ec()

        return PathPatch(self.path, **kwargs)

    def get_path(self):
        """ROI path."""
        return self.path

    def get_fc(self):  # pylint: disable=no-self-use
        """ROI default facecolor."""
        return 'none'

    def get_ec(self):
        """ROI default edgecolor."""
        return getattr(self, 'color', 'red')

    def contains(self, pts):
        """Check if points are inside the pixel.

        Parameters
        ----------
        pts: np.array or trajectory.Trajectory
            List of geographic point(s): ``(lon_e, lat)`` or ``[(lon_e, lat), …]``.
            If a :py:obj:`Trajectory` is provided, the intersection
            will be performed on the its sub-observer points.

        Returns
        -------
        np.array
            Return ``TRUE`` if the point is inside the pixel corners, and
            ``FALSE`` overwise.

        Warning
        -------
        The data need to be projected on a sphere first.
        Here we project the :py:obj:`ROI` on a Equirectangular
        plane before doing the intersection.

        Note
        ----
        If the point is on the edge of the contour it will be excluded.

        """
        if isinstance(pts, Trajectory):
            return self.contains(pts.sub_obs_pts[1:])

        if np.ndim(pts) == 1:
            return self.contains([pts])

        if np.shape(pts)[0] == 2 and np.shape(pts)[1] != 2:
            return self.contains(np.transpose(pts))

        eq = Equirectangular()
        return eq(self.path).contains_points(pts)


class ROIsCollection(AbstractCollection):
    """ROIs collection."""
    ITEM = ROI

    def __call__(self, **kwargs):
        return self.collection(**kwargs)

    def collection(self, **kwargs):
        """ROI patches collection with default ROI color."""
        patches = [roi.patch() for roi in self]

        if 'facecolors' not in kwargs:
            kwargs['facecolors'] = self.get_facecolors()

        if 'edgecolors' not in kwargs:
            kwargs['edgecolors'] = self.get_edgecolors()

        return PatchCollection(patches, **kwargs)

    def get_paths(self):
        """Collection paths."""
        return self.collection().get_paths()

    def get_facecolors(self, default='None'):  # pylint: disable=no-self-use
        """Default facecolors."""
        return default

    def get_edgecolors(self, default='red'):
        """Default edgecolors."""
        return [roi.color if hasattr(roi, 'color') else default for roi in self]


class ROIsCollectionWithCategories(ROIsCollection):
    """ROIs collection with categories."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.categories = CategoriesCollection()
        self.subcategories = SubCategoriesCollection()

    def __repr__(self):
        s = f'<{self.__class__.__name__}> {self.count}'
        s += f' | {self.categories.count}'
        s += f' | {self.subcategories.count}' if len(self.subcategories) >= 1 else ''
        return s

    def __contains__(self, key):
        if key in self.rois.keys():
            return True

        if key in self.categories.keys():
            return True

        if key in self.subcategories.keys():
            return True

        return False

    def __getitem__(self, key):
        if str(key) in self.data:
            return self.data[str(key)]

        if str(key) in self.categories:
            category = self.categories[str(key)]
            return ROIsCollection({
                k: v for k, v in self.items()
                if v.category == category
            })

        if str(key) in self.subcategories:
            subcategory = self.subcategories[str(key)]
            return ROIsCollection({
                k: v for k, v in self.items()
                if hasattr(v, 'subcategory') and v.subcategory == subcategory
            })

        raise KeyError(key)

    def __setitem__(self, key, item):
        """Add a new item.

        Note
        ----
        If an ``ITEM`` is directely provided, the item
        will be copy an its key will be updated with
        the new one.

        Raises
        ------
        AttributeError:
            If the provided `ITEM`` contain :py:attr:`category` or
            :py:attr:`subcategory` attribute

        Note
        ----
        If a :py:attr:`category` and a :py:attr:`subcategory` are provided
        at the sametime, the :py:attr:`subcategory` parent ``category``
        will overwrite the provided :py:attr:`category`.

        """
        if isinstance(item, self.ITEM):
            _item = copy(item)
            _item.key = key

            if hasattr(item, 'subcategory'):
                if not isinstance(_item.subcategory, SubCategory):
                    _item.subcategory = self.subcategories[_item.subcategory]
                    _item.category = _item.subcategory.category

            elif hasattr(item, 'category'):
                if not isinstance(_item.category, Category):
                    _item.category = self.categories[_item.category]

            else:
                raise AttributeError('Missing `category` or `sub-category` attribute')

            self.data[str(key)] = _item
        else:
            self.add_roi(key, **item)

    @property
    def rois(self):
        """Collection of ROIs."""
        return ROIsCollection(self.data)

    def add_category(self, key, **kwargs):
        """Add/Update a category."""
        self.categories[key] = kwargs

    def add_subcategory(self, key, **kwargs):
        """Add/Update a subcategory."""
        if 'category' not in kwargs:
            raise AttributeError('Missing `category` attribute')

        cat = str(kwargs['category'])
        if cat not in self.categories:
            raise ValueError(f'Unknown category: `{cat}`')

        if not isinstance(kwargs['category'], Category):
            kwargs['category'] = self.categories[cat]

        self.subcategories[key] = kwargs

    def add_roi(self, key, lons_e, lats, **kwargs):
        """Add/Update a subcategory."""
        if 'subcategory' in kwargs:
            subcat = str(kwargs['subcategory'])
            if subcat not in self.subcategories:
                raise ValueError(f'Unknown sub-category: `{subcat}`')

            if not isinstance(kwargs['subcategory'], SubCategory):
                kwargs['category'] = self.subcategories[subcat].category
                kwargs['subcategory'] = self.subcategories[subcat]

        elif 'category' in kwargs:
            cat = str(kwargs['category'])
            if cat not in self.categories:
                raise ValueError(f'Unknown category: `{cat}`')

            if not isinstance(kwargs['category'], Category):
                kwargs['category'] = self.categories[cat]

        else:
            raise AttributeError('Missing `category` or `sub-category` attribute')

        self.data[str(key)] = self.ITEM(key, lons_e, lats, **kwargs)
