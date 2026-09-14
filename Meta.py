# Meta.py - FreeCAD Extension metadata

Meta = {
    "author": "FreeCAD CAM community",
    "version": (1, 0, 0),
    "weekmap": "2026.09",
    "app": "Main",
    "icon": "",
    "color": None,
    "active": True,
    "needs_network": False,
    "needs_restart": False,
    "has_python": True,
    "hide": False,
    "can_be_disabled": True,
    "install": [
        {
            "type": "action",
            "action": "import jetcutter_tools.toolbar; jetcutter_tools.toolbar.install()",
            "enabled": True,
        },
    ],
    "uninstall": [
        {
            "type": "action",
            "action": "import jetcutter_tools.toolbar; jetcutter_tools.toolbar.uninstall()",
            "enabled": True,
        },
    ],
}
