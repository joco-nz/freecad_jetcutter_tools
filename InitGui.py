"""InitGui.py - Loaded by FreeCAD on startup to register the workbench."""

import os
import sys

try:
    _initgui_file = __file__
except NameError:
    _initgui_file = None

if _initgui_file:
    ext_dir = os.path.dirname(os.path.abspath(_initgui_file))
else:
    ext_dir = os.path.join(os.path.expanduser("~"),
                           ".local", "share", "FreeCAD",
                           "v26-3", "Mod", "freecad_jetcutter_tools")

if ext_dir not in sys.path:
    sys.path.insert(0, ext_dir)

import FreeCADGui
from jetcutter_tools.InitGui import JetCutterToolsWorkbench

FreeCADGui.addWorkbench(JetCutterToolsWorkbench)
