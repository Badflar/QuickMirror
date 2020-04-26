import bpy

class QuickMirror_Panel_Object(bpy.types.Panel):
    bl_idname = "QuickMirror_Panel"
    bl_label = "QuickMirror Pannel"
    bl_info = "INFO"
    bl_category = "QuickMirror Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.operator('object.quick_mirror', text="Apply QuickMirror Modifier to selected object(s)")