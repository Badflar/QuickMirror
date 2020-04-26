import bpy
import mathutils 
from mathutils import Vector 

class QuickMirrorObject(bpy.types.Operator):
    bl_idname = "object.quick_mirror"
    bl_label = "QuickMirror"
    bl_info = "INFO"
    bl_description = "Origin to Center and Mirror Modifier w/ Clipping"

    def execute(self, context): 
        bpy.context.scene.cursor.location = Vector((0.0, 0.0, 0.0))
        bpy.context.scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))

        obj = bpy.context.active_object
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        mod = obj.modifiers.new('QUICK MIRROR', 'MIRROR')
        mod.use_clip = True
        
        for o in context.selected_objects:
            if o == obj:
                continue
            if o.type != 'MESH':
                continue

            mod = o.modifiers.get('QUICK MIRROR')
            if mod is None:
                mod = o.modifiers.new('QUICK MIRROR', 'MIRROR')
            mod.use_clip = True
                
        return {'FINISHED'}