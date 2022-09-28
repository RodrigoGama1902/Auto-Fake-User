import bpy

from .auto_fake_user import enable_fake_user

def register_handlers():
    bpy.app.handlers.save_pre.append(enable_fake_user)

def unregister_handlers():
    bpy.app.handlers.save_pre.remove(enable_fake_user)