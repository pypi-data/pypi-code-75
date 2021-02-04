# -*- python -*- 

from ctypes import CDLL
from pathlib import Path
import glob

__version__ = "1.7.10"

# open shared library
LIB = None
for libfile in Path(__path__[0] + '/..').glob('mint.cpython*'):
    LIB = CDLL(libfile)
    if LIB:
        break

__all__ = [LIB, 'regrid_edges', 'grid', 'polyline_integral']

from .regrid_edges import RegridEdges
from .grid import Grid
from .polyline_integral import PolylineIntegral

