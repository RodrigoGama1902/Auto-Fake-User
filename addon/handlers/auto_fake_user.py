import bpy

from bpy.app.handlers import persistent

from ..utils.functions import get_enabled_data_blocks

@persistent
def enable_fake_user(scene):
    
    props = bpy.context.scene.autofakeuser
    
    if not props.toggle_on_off:
        return
    
    for data in get_enabled_data_blocks():
        print("Enabling Fake User for", data)
        
        for data_block in data:
            data_block.use_fake_user = True