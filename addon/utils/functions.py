import bpy

def get_enabled_data_blocks() -> list:
    
    data_blocks = []
    
    props = bpy.context.scene.autofakeuser
    
    if props.material_data_block:
        data_blocks.append(bpy.data.materials)
    if props.object_data_block:
        data_blocks.append(bpy.data.objects)
    if props.images_data_block:
        data_blocks.append(bpy.data.images)
    
    return data_blocks
    
    
    