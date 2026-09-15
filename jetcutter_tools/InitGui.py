"""InitGui.py - FreeCAD workbench definition for JetCutter Tools."""

import FreeCADGui
from jetcutter_tools import commands
from jetcutter_tools import icons
from jetcutter_tools import toolbar


class JetCutterToolsWorkbench(FreeCADGui.Workbench):
    """Lightweight workbench providing CAM workflow tools."""

    menuText = "JetCutter Tools"
    toolTip = "JetCutter CAM workflow tools"
    Icon = ""

    def Initialize(self):
        """Register commands and create toolbar."""
        icons.register_icon_path()

        FreeCADGui.addCommand('JetCutter_SameEdges', commands.SameEdgesAsHighlighted())
        FreeCADGui.addCommand('JetCutter_FindProfiles', commands.FindProfiles())

        toolbar._create_toolbar()

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(JetCutterToolsWorkbench)
