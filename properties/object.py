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

OBJECT_TYPE = (
    ("NONE", "None", "Default blender object"),
    ("ROOM", "Room", "Room"),
    ("MASK", "Mask", "Mask"),
    ("BOUNDARIES", "Boundaries", "Boundaries"),
)

class TUNEUR_TypeProperties(bpy.types.PropertyGroup):
    type: bpy.props.EnumProperty(
        name="Type",
        items=OBJECT_TYPE,
        default="NONE"
    )

class TUNEUR_RoomProperties(bpy.types.PropertyGroup):
    mask: bpy.props.PointerProperty(
        name="Mask",
        type=bpy.types.Object
    )
    boundaries: bpy.props.PointerProperty(
        name="Boundaries",
        type=bpy.types.Object
    )

class TUNEUR_ObjectProperties(bpy.types.PropertyGroup):
    close_rooms: bpy.props.PointerProperty(type=TUNEUR_CloseRoomsProperties)
    type: bpy.props.PointerProperty(type=TUNEUR_TypeProperties)
    room: bpy.props.PointerProperty(type=TUNEUR_RoomProperties)