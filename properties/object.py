import bpy

class TUNEUR_CloseRoomProperties(bpy.types.PropertyGroup):
    target: bpy.props.PointerProperty(
        name="Target",
        type=bpy.types.Object
    )
    show_mesh: bpy.props.BoolProperty(name="Show Mesh", default=True)

class TUNEUR_CloseRoomsProperties(bpy.types.PropertyGroup):
    list: bpy.props.CollectionProperty(type=TUNEUR_CloseRoomProperties)
    list_index: bpy.props.IntProperty()

class TUNEUR_ObjectProperties(bpy.types.PropertyGroup):
    close_rooms: bpy.props.PointerProperty(type=TUNEUR_CloseRoomsProperties)