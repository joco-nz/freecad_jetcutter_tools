"""init_gui.py - FreeCAD workbench definition for JetCutter Tools."""

import os

import FreeCADGui
from . import commands
from . import toolbar

ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Resources', 'Icons')


class JetCutterToolsWorkbench(FreeCADGui.Workbench):
    """Lightweight workbench providing CAM workflow tools."""

    Icon = "jetcutter_tools"
    menuText = "JetCutter Tools"
    toolTip = "JetCutter CAM workflow tools"

    def Initialize(self):
        """Register icon paths, commands, and toolbar."""
        FreeCADGui.addIconPath(ICON_DIR)

        FreeCADGui.addCommand('JetCutter_SameEdges', commands.SameEdgesAsHighlighted())
        FreeCADGui.addCommand('JetCutter_FindProfiles', commands.FindProfiles())

        toolbar._create_toolbar()
        toolbar._start_cam_polling()

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(JetCutterToolsWorkbench)
