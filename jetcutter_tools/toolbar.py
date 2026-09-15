"""JetCutter Tools toolbar - creates a FreeCAD toolbar with command buttons."""

import os

import FreeCADGui

ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "macros")

ICON_FILES = {
    "JetCutter_SameEdges": os.path.join(ICON_DIR, "same-edges-as-highlighted.svg"),
    "JetCutter_FindProfiles": os.path.join(ICON_DIR, "FindProfiles.svg"),
}

TOOLBAR_NAME = "JetCutter Tools"

COMMANDS = [
    {
        "name": "JetCutter_SameEdges",
        "text": "Same Edges As Highlighted",
        "tooltip": "Select all edges matching the length and Z-level of highlighted edges",
    },
    {
        "name": "JetCutter_FindProfiles",
        "text": "Find Profiles",
        "tooltip": "Create Profile operations for internal edges on CAM Job top faces",
    },
]


def _run_command(command_name):
    """Callback for toolbar button - runs the named FreeCAD command."""
    FreeCADGui.runCommand(command_name)


def _load_icon(filepath):
    """Load an SVG file as a QIcon."""
    try:
        from PySide import QtGui
    except ImportError:
        from PySide6 import QtGui
    return QtGui.QIcon(filepath)


def _create_toolbar():
    """Create the JetCutter Tools toolbar with buttons for each command."""
    try:
        from PySide.QtWidgets import QToolBar
    except ImportError:
        from PySide6.QtWidgets import QToolBar

    main_window = FreeCADGui.getMainWindow()

    existing_toolbars = main_window.findChildren(QToolBar)
    for tb in existing_toolbars:
        if tb.objectName() == TOOLBAR_NAME:
            return tb

    toolbar = main_window.addToolBar(TOOLBAR_NAME)
    toolbar.setObjectName(TOOLBAR_NAME)
    toolbar.setToolTip("JetCutter CAM workflow tools")

    for cmd in COMMANDS:
        icon = _load_icon(ICON_FILES.get(cmd["name"], ""))
        action = toolbar.addAction(icon, cmd["text"])
        action.setToolTip(cmd["tooltip"])
        action.triggered.connect(
            lambda checked, name=cmd["name"]: _run_command(name)
        )

    return toolbar


def _remove_toolbar():
    """Remove the JetCutter Tools toolbar."""
    try:
        from PySide.QtWidgets import QToolBar
    except ImportError:
        from PySide6.QtWidgets import QToolBar

    main_window = FreeCADGui.getMainWindow()
    toolbars = main_window.findChildren(QToolBar)
    for tb in toolbars:
        if tb.objectName() == TOOLBAR_NAME:
            main_window.removeToolBar(tb)
            tb.deleteLater()
            break
