"""InitGui.py - Loaded by FreeCAD on startup to create the toolbar."""

import os
import sys

# Add the extension directory to sys.path
ext_dir = os.path.expanduser("~/.local/share/FreeCAD/v26-3/Mod/freecad_jetcutter_tools")
if ext_dir not in sys.path:
    sys.path.insert(0, ext_dir)

import FreeCAD
import FreeCADGui

# Import QtWidgets from FreeCADGui's embedded Qt
try:
    from FreeCADGui import Qt as QtGui
    QtWidgets = QtGui.QtWidgets
except Exception:
    try:
        import PySide6.QtWidgets as QtWidgets
    except Exception:
        import PySide.QtWidgets as QtWidgets

# Create toolbar immediately when this module loads
_toolbar_created = False

def _ensure_toolbar():
    global _toolbar_created
    if _toolbar_created:
        return
    try:
        main_window = FreeCADGui.getMainWindow()
        if not main_window:
            return
        existing = main_window.findChildren(QtWidgets.QToolBar)
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
