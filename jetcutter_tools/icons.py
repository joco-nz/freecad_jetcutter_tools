"""Icon resource management for JetCutter Tools."""

import os

ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "macros")

ICON_NAMES = {
    "same-edges-as-highlighted": "same-edges-as-highlighted",
    "find-profiles": "FindProfiles",
}


def get_icon_path(name):
    """Return full path to an SVG icon by its registered name."""
    icon_map = {
        "same-edges-as-highlighted": "same-edges-as-highlighted.svg",
        "find-profiles": "FindProfiles.svg",
    }
    filename = icon_map.get(name)
    if not filename:
        return None
    return os.path.join(ICON_DIR, filename)


def register_icon_path():
    """Register the icon directory with FreeCAD's resource search path."""
    import FreeCADGui
    if os.path.isdir(ICON_DIR):
        FreeCADGui.addResourcePath(ICON_DIR)
