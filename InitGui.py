"""InitGui.py - Loaded by FreeCAD on startup to create the toolbar."""

import os
import sys

# FreeCAD loads InitGui.py with exec(), so __file__ is not defined.
# Use the known user Mod path for this extension.
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

import FreeCAD
import FreeCADGui

_toolbar_created = False

def _ensure_toolbar():
    global _toolbar_created
    if _toolbar_created:
        return
    try:
        main_window = FreeCADGui.getMainWindow()
        if not main_window:
            return
        existing = main_window.findChildren(FreeCADGui.Qt.QToolBar)
        for tb in existing:
            if tb.objectName() == "JetCutter Tools":
                _toolbar_created = True
                return
        from jetcutter_tools import toolbar
        toolbar.install()
        _toolbar_created = True
    except Exception as e:
        FreeCAD.Console.PrintWarning("JetCutter Tools: %s\n" % str(e))

_ensure_toolbar()
