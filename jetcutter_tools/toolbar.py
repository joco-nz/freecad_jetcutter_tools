"""JetCutter Tools toolbar - creates a FreeCAD toolbar with macro buttons."""

import os
import shutil
import FreeCAD
import FreeCADGui
from PySide.QtCore import QToolBar

TOOLBAR_NAME = "JetCutter Tools"

MACROS = [
    {
        "name": "JetCutter_SameEdges",
        "text": "Same Edges As Highlighted",
        "tooltip": "Select all edges matching the length and Z-level of highlighted edges",
        "macro": "same-edges-as-highlighted.FCMacro",
    },
    {
        "name": "JetCutter_FindProfiles",
        "text": "Find Profiles",
        "tooltip": "Create Profile operations for internal edges on CAM Job top faces",
        "macro": "FindProfiles.FCMacro",
    },
]


def _get_macro_src_path():
    """Return the path to a macro file bundled in this extension."""
    extension_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(extension_dir, "macros")


def _get_macro_dst_dir():
    """Return the user's FreeCAD Macro directory."""
    return os.path.join(FreeCAD.getUserAppDataDir(), "Macro")


def _copy_macros_to_user_dir():
    """Copy bundled macros into the user's Macro directory."""
    src_dir = _get_macro_src_path()
    dst_dir = _get_macro_dst_dir()
    os.makedirs(dst_dir, exist_ok=True)
    for m in MACROS:
        src = os.path.join(src_dir, m["macro"])
        dst = os.path.join(dst_dir, m["macro"])
        if os.path.exists(src):
            shutil.copy2(src, dst)


def _remove_macros_from_user_dir():
    """Remove copied macros from the user's Macro directory."""
    dst_dir = _get_macro_dst_dir()
    for m in MACROS:
        dst = os.path.join(dst_dir, m["macro"])
        if os.path.exists(dst):
            try:
                os.remove(dst)
            except OSError:
                pass


def _run_macro(macro_name):
    """Callback for toolbar button - runs the named macro."""
    macro_dir = _get_macro_dst_dir()
    for m in MACROS:
        if m["name"] == macro_name:
            path = os.path.join(macro_dir, m["macro"])
            if os.path.exists(path):
                FreeCADGui.runMacro(path)
            return


def _create_toolbar():
    """Create the JetCutter Tools toolbar with buttons for each macro."""
    main_window = FreeCADGui.getMainWindow()

    # Check if toolbar already exists
    existing_toolbars = main_window.findChildren(QToolBar)
    for tb in existing_toolbars:
        if tb.objectName() == TOOLBAR_NAME:
            return tb

    toolbar = main_window.addToolBar(TOOLBAR_NAME)
    toolbar.setObjectName(TOOLBAR_NAME)
    toolbar.setToolTip("JetCutter CAM workflow tools")

    for m in MACROS:
        action = toolbar.addAction(m["text"])
        action.setToolTip(m["tooltip"])
        action.triggered.connect(lambda checked, name=m["name"]: _run_macro(name))

    return toolbar


def _remove_toolbar():
    """Remove the JetCutter Tools toolbar."""
    main_window = FreeCADGui.getMainWindow()
    toolbars = main_window.findChildren(QToolBar)
    for tb in toolbars:
        if tb.objectName() == TOOLBAR_NAME:
            main_window.removeToolBar(tb)
            tb.deleteLater()
            break


def install():
    """Install the extension: copy macros, create toolbar."""
    FreeCAD.Console.PrintMessage("Installing JetCutter Tools extension...\n")

    _copy_macros_to_user_dir()
    _create_toolbar()

    FreeCAD.Console.PrintMessage("JetCutter Tools extension installed.\n")


def uninstall():
    """Uninstall the extension: remove toolbar, clean up."""
    FreeCAD.Console.PrintMessage("Uninstalling JetCutter Tools extension...\n")

    _remove_toolbar()
    _remove_macros_from_user_dir()

    FreeCAD.Console.PrintMessage("JetCutter Tools extension uninstalled.\n")
