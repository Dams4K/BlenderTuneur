import bpy

class TUNEUR_ObjectProperties(bpy.types.PropertyGroup):
    target: bpy.props.PointerProperty(
        name="Target",
        type=bpy.types.Object
    )