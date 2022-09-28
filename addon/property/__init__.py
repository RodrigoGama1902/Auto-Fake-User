import bpy

from .addon_props import AUTOFK_AddonProps

classes = (
    AUTOFK_AddonProps,
)

def register_props():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    
    bpy.types.Scene.autofakeuser = bpy.props.PointerProperty(type= AUTOFK_AddonProps)

def unregister_props():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
    del bpy.types.Scene.autofakeuser