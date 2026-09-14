"""JetCutter Tools toolbar - creates a FreeCAD toolbar with macro buttons."""

import os
import shutil
import FreeCAD
import FreeCADGui

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
    return FreeCAD.GetHomePath("Macro")


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


class _MacroCommand(FreeCADGui.Command):
    """A Gui.Command that runs a FreeCAD macro file."""

    def __init__(self, macro_path):
        super(_MacroCommand, self).__init__(macro_path)
        self.macro_path = macro_path

    def Activated(self):
        FreeCADGui.runMacro(self.macro_path)

    def IsEnabled(self):
        return bool(FreeCAD.ActiveDocument)

    def GetIcon(self):
        return []


def _register_commands():
    """Register all macro commands with FreeCAD."""
    macro_dir = _get_macro_dst_dir()
    for m in MACROS:
        cmd = _MacroCommand(os.path.join(macro_dir, m["macro"]))
        FreeCADGui.addCommand(m["name"], cmd)


def _unregister_commands():
    """Unregister all macro commands from FreeCAD."""
    for m in MACROS:
        try:
            FreeCADGui.removeCommand(m["name"])
        except Exception:
            pass


def _create_toolbar():
    """Create the JetCutter Tools toolbar with buttons for each macro."""
    # Check if toolbar already exists
    main_window = FreeCADGui.getMainWindow()
    existing_toolbars = main_window.findChildren("QToolBar")
    for tb in existing_toolbars:
        if tb.objectName() == TOOLBAR_NAME:
            return tb

    toolbar = main_window.addToolBar(TOOLBAR_NAME)
    toolbar.setObjectName(TOOLBAR_NAME)
    toolbar.setToolTip("JetCutter CAM workflow tools")

    for m in MACROS:
        toolbar.addAction(m["text"])
        # Connect button click to command
        cmd = FreeCADGui.Command(m["name"])
        toolbar.actionList()[-1].triggered.connect(cmd.Activated)

    return toolbar


def _remove_toolbar():
    """Remove the JetCutter Tools toolbar."""
    main_window = FreeCADGui.getMainWindow()
    toolbars = main_window.findChildren("QToolBar")
    for tb in toolbars:
        if tb.objectName() == TOOLBAR_NAME:
            main_window.removeToolBar(tb)
            tb.deleteLater()
            break


def install():
    """Install the extension: copy macros, register commands, create toolbar."""
    FreeCAD.Console.PrintMessage("Installing JetCutter Tools extension...\n")

    # Copy macros to user's Macro directory
    _copy_macros_to_user_dir()

    # Register commands
    _register_commands()

    # Create toolbar
    _create_toolbar()

    FreeCAD.Console.PrintMessage("JetCutter Tools extension installed.\n")


def uninstall():
    """Uninstall the extension: remove toolbar, unregister commands, clean up."""
    FreeCAD.Console.PrintMessage("Uninstalling JetCutter Tools extension...\n")

    # Remove toolbar
    _remove_toolbar()

    # Unregister commands
    _unregister_commands()

    # Remove macros from user's Macro directory
    _remove_macros_from_user_dir()

    FreeCAD.Console.PrintMessage("JetCutter Tools extension uninstalled.\n")
