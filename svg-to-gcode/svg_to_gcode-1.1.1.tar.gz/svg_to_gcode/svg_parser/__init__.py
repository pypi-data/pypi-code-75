"""
The svg_parser sub-module is used to parse svg_files into the geometric form supplied by the geometry sub-module.

specific maintenance notes:
    - The svg origin is at the top-left, while the geometry sub-module has it's origin a the bottom-left. As such, all
    parser classes must transform input coordinates to the bottom-left coordinate system.
"""

from svg_to_gcode.svg_parser._path import Path
from svg_to_gcode.svg_parser._helper_functions import parse_file, parse_string, parse_root
