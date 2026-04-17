import bpy

class TUNEUR_UL_CloseRooms(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        text = item.target.name if item.target else "NONE"
        layout.label(text=text)

class TUNEUR_PT_CloseRoomsSettings(bpy.types.Panel):
    bl_space_type  = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label       = "Close Rooms"
    bl_idname      = "TUNEUR_PT_CloseRoomsSettings"
    bl_parent_id   = "TUNEUR_PT_ObjectSettings"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        props = obj.tuneur.close_rooms

        close_rooms_row = layout.row()
        close_rooms_row.template_list(
            "TUNEUR_UL_CloseRooms",
            "",
            props,
            "list",
            props,
            "list_index"
        )
        col = close_rooms_row.column(align=True)
        col.operator("tuneur.add_close_room", icon="ADD", text="")
        col.operator("tuneur.remove_close_room", icon="REMOVE", text="")

        if props.list:
            item = props.list[props.list_index]

            col = layout.column()
            col.prop(item, "target")
            col.prop(item, "show_mesh")

class TUNEUR_PT_ObjectSettings(bpy.types.Panel):
    bl_space_type  = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label       = "Tuneur Settings"
    bl_idname      = "TUNEUR_PT_ObjectSettings"
    bl_context     = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        props = obj.tuneur