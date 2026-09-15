"""InitGui.py - FreeCAD workbench definition for JetCutter Tools."""

import os

import FreeCADGui
from jetcutter_tools import commands
from jetcutter_tools import toolbar

ICON_DIR = os.path.dirname(os.path.abspath(__file__))
MACROS_DIR = os.path.join(ICON_DIR, "macros")


class JetCutterToolsWorkbench(FreeCADGui.Workbench):
    """Lightweight workbench providing CAM workflow tools."""

    Icon = "jetcutter_tools"
    menuText = "JetCutter Tools"
    toolTip = "JetCutter CAM workflow tools"

    def Initialize(self):
        """Register icon paths, commands, and toolbar."""
        FreeCADGui.addIconPath(ICON_DIR)
        FreeCADGui.addIconPath(MACROS_DIR)

        FreeCADGui.addCommand('JetCutter_SameEdges', commands.SameEdgesAsHighlighted())
        FreeCADGui.addCommand('JetCutter_FindProfiles', commands.FindProfiles())

        toolbar._create_toolbar()
        toolbar._start_cam_polling()

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(JetCutterToolsWorkbench)
