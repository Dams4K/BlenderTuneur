import bpy

class TUNEUR_PT_ObjectSettings(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Tuneur Settings"
    bl_idname = "TUNEUR_PT_ObjectSettings"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object