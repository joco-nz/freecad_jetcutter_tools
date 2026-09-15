"""init_gui.py - FreeCAD addon initialization for JetCutter Tools."""

import os

import FreeCADGui
from . import commands
from . import toolbar

ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Resources', 'Icons')

# Register icon path
FreeCADGui.addIconPath(ICON_DIR)

# Register commands so they are available globally
FreeCADGui.addCommand('JetCutter_SameEdges', commands.SameEdgesAsHighlighted())
FreeCADGui.addCommand('JetCutter_FindProfiles', commands.FindProfiles())

# Start polling for CAM workbench activation
toolbar._start_cam_polling()
