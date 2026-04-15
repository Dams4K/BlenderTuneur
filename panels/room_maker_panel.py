import bpy

class TUNEUR_PT_room_maker(bpy.types.Panel):
    bl_label = "Room Maker"
    bl_idname = "TUNEUR_PT_room_maker"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_category = "Room Maker"
    bl_label = "Room Maker"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.row().operator("tuneur.create_mask", text="Make")