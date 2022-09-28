#type:ignore
import bpy
              
class AUTOFK_AddonProps(bpy.types.PropertyGroup):
    
    toggle_on_off : bpy.props.BoolProperty()
    
    # Set Fake User to:
    material_data_block : bpy.props.BoolProperty(name = "Materials", default = True)
    object_data_block : bpy.props.BoolProperty(name = "Objects", default = True)
    images_data_block : bpy.props.BoolProperty(name = "Images", default = True)

    
    
    

    
    
