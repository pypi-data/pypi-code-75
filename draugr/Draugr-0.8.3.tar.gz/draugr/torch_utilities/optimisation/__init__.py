#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 15/02/2020
           """

import pathlib

with open(pathlib.Path(__file__).parent / "README.md", "r") as this_init_file:
    __doc__ += this_init_file.read()

from .debugging import *
from .parameters import *
from .scheduling import *
from .updates import *
