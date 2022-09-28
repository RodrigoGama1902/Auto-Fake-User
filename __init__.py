bl_info = {
    "name": "Auto Fake User",
    "description": "Automatically set Fake User to enabled data blocks when saving",
    "author": "Rodrigo Gama",
    "version": (0, 1, 0),
    "blender": (3, 2, 0),
    "location": "View3D",
    "category": "3D View"}


def register():
    from .addon.register import register_addon
    register_addon()


def unregister():
    from .addon.register import unregister_addon
    unregister_addon()