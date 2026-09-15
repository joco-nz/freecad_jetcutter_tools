"""init_gui.py - FreeCAD workbench definition for JetCutter Tools."""

import os

import FreeCADGui
from . import commands
from . import toolbar

ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Resources', 'Icons')

# Register icon path at module level, BEFORE addWorkbench() is called below.
# The workbench Icon is loaded during addWorkbench(), so the path must be
# registered before that call.
FreeCADGui.addIconPath(ICON_DIR)


class JetCutterToolsWorkbench(FreeCADGui.Workbench):
    """Lightweight workbench providing CAM workflow tools."""

    Icon = "jetcutter_tools"
    menuText = "JetCutter Tools"
    toolTip = "JetCutter CAM workflow tools"

    def Initialize(self):
        """Register commands."""
        FreeCADGui.addCommand('JetCutter_SameEdges', commands.SameEdgesAsHighlighted())
        FreeCADGui.addCommand('JetCutter_FindProfiles', commands.FindProfiles())

    def GetClassName(self):
        return "Gui::PythonWorkbench"


FreeCADGui.addWorkbench(JetCutterToolsWorkbench)
toolbar._start_cam_polling()
