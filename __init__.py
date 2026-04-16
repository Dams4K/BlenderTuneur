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
    CreateMaskOperator,
    TUNEUR_PT_room_maker,
    TUNEUR_PT_ObjectSettings,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
if __name__ == "__main__":
    register()