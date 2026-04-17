import bpy

class TUNEUR_OT_AddCloseRoom(bpy.types.Operator):
    bl_idname = "tuneur.add_close_room"
    bl_label = "Add Close Room"

    def execute(self, context):
        obj = context.object
        obj.tuneur.close_rooms.list.add()
        return {'FINISHED'}


class TUNEUR_OT_RemoveCloseRoom(bpy.types.Operator):
    bl_idname = "tuneur.remove_close_room"
    bl_label = "Remove Close Room"

    def execute(self, context):
        obj = context.object
        props = obj.tuneur
        props.close_rooms.list.remove(props.close_rooms.list_index)
        props.close_rooms.list_index = max(0, props.close_rooms.list_index - 1)
        return {'FINISHED'}