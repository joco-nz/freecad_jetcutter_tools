"""JetCutter Tools toolbar - creates a FreeCAD toolbar with command buttons."""

import os

import FreeCADGui
from PySide.QtCore import QTimer

try:
    from PySide import QtGui
except ImportError:
    from PySide6 import QtGui

ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Resources', 'Icons')

TOOLBAR_NAME = "JetCutter Tools"

COMMANDS = [
    {
        "name": "JetCutter_SameEdges",
        "icon": "same-edges-as-highlighted",
        "text": "Same Edges As Highlighted",
        "tooltip": "Select all edges matching the length and Z-level of highlighted edges",
    },
    {
        "name": "JetCutter_FindProfiles",
        "icon": "FindProfiles",
        "text": "Find Profiles",
        "tooltip": "Create Profile operations for internal edges on CAM Job top faces",
    },
]

_toolbar = None
_cam_timer = None


def _run_command(command_name):
    """Callback for toolbar button - runs the named FreeCAD command."""
    FreeCADGui.runCommand(command_name)


def _create_toolbar():
    """Create the JetCutter Tools toolbar with buttons for each command."""
    try:
        from PySide.QtWidgets import QToolBar
    except ImportError:
        from PySide6.QtWidgets import QToolBar

    global _toolbar

    main_window = FreeCADGui.getMainWindow()

    existing_toolbars = main_window.findChildren(QToolBar)
    for tb in existing_toolbars:
        if tb.objectName() == TOOLBAR_NAME:
            _toolbar = tb
            return _toolbar

    _toolbar = main_window.addToolBar(TOOLBAR_NAME)
    _toolbar.setObjectName(TOOLBAR_NAME)
    _toolbar.setToolTip("JetCutter CAM workflow tools")
    _toolbar.setVisible(False)

    for cmd in COMMANDS:
        icon_path = os.path.join(ICON_DIR, cmd["icon"] + ".svg")
        icon = QtGui.QIcon(icon_path)
        action = _toolbar.addAction(icon, cmd["text"])
        action.setToolTip(cmd["tooltip"])
        action.triggered.connect(
            lambda checked, name=cmd["name"]: _run_command(name)
        )

    return _toolbar


def _start_cam_polling():
    """Start a timer that polls for CAM workbench activation."""
    global _cam_timer

    _cam_timer = QTimer()
    _cam_timer.timeout.connect(_check_cam_active)
    _cam_timer.start(500)


def _check_cam_active():
    """Check if CAM workbench is active and show/hide toolbar accordingly."""
    wb = FreeCADGui.activeWorkbench()
    if wb and wb.name() == "CAM":
        _show_toolbar()
    else:
        _hide_toolbar()


def _show_toolbar():
    """Show the JetCutter Tools toolbar."""
    global _toolbar
    if _toolbar is not None and not _toolbar.isVisible():
        _toolbar.setVisible(True)


def _hide_toolbar():
    """Hide the JetCutter Tools toolbar."""
    global _toolbar
    if _toolbar is not None and _toolbar.isVisible():
        _toolbar.setVisible(False)
