"""InitGui.py - Loaded by FreeCAD on startup to create the toolbar."""

import os
import sys

ext_dir = os.path.dirname(os.path.abspath(__file__))
if ext_dir not in sys.path:
    sys.path.insert(0, ext_dir)

import FreeCAD
import FreeCADGui
from PySide.QtWidgets import QToolBar


def _create_toolbar():
    if hasattr(_create_toolbar, "_installed"):
        return
    _create_toolbar._installed = True

    main_window = FreeCADGui.getMainWindow()
    existing = main_window.findChildren(QToolBar)
    for tb in existing:
        if tb.objectName() == "JetCutter Tools":
            return

    from jetcutter_tools import toolbar
    toolbar.install()


class JetCutterToolsWorkbench(FreeCADGui.Workbench):
    menuText = "JetCutter Tools"
    toolTip = "JetCutter CAM workflow tools"
    Icon = ""

    def Initialize(self):
        _create_toolbar()

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(JetCutterToolsWorkbench)
