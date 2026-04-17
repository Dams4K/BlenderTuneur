import bpy

from .panels import *
from .operators import *
from .properties import *

bl_info = {
    "name": "Tuneur",
    "author": "Dams4K",
    "version": (1, 0),
    "blender": (5, 1, 0),
    "dependencies": ["GoBlend"],
}

classes = (
    TUNEUR_UL_CloseRooms,

    TUNEUR_TypeProperties,
    TUNEUR_CloseRoomProperties,
    TUNEUR_CloseRoomsProperties,
    TUNEUR_ObjectProperties,

    TUNEUR_PT_room_maker,
    TUNEUR_PT_ObjectSettings,
    TUNEUR_PT_Type,
    TUNEUR_PT_CloseRoomsSettings,

    TUNEUR_OP_CreateMask,
    TUNEUR_OT_AddCloseRoom,
    TUNEUR_OT_RemoveCloseRoom,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Object.tuneur = bpy.props.PointerProperty(type=TUNEUR_ObjectProperties)

def unregister():
    del bpy.types.Object.tuneur

    for cls in classes:
        bpy.utils.unregister_class(cls)
    
if __name__ == "__main__":
    register()