import bpy

class BasePanel:    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
class AUTOFK_PT_MainPanel(BasePanel, bpy.types.Panel):
    bl_label = "Auto Fake User"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self,context):
        
        props = context.scene.autofakeuser
        layout = self.layout
        
        row = layout.row()
        box = row.box()
        
        row = box.row()  
        row.prop(props, "toggle_on_off", text = "", icon = "FAKE_USER_ON" if props.toggle_on_off else "FAKE_USER_OFF")
        row.label(text="When Saving, automatically set Fake User to:" if props.toggle_on_off else "Enable Auto Fake User")
        
        if props.toggle_on_off: 
            box = layout.box()
            row = box.row()
            row.prop(props, "material_data_block")
            row = box.row()
            row.prop(props, "object_data_block")
            row = box.row()
            row.prop(props, "images_data_block")
 
        
        