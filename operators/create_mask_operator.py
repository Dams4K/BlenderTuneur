import bpy

from ..helper import *

MASK_DISCRIMINATOR = "-mask"

MASK_MATERIAL_NAME       = "Mask"
MASK_MATERIAL_SHADE_MODE = "UNSHADED"
MASK_VISUAL_LAYER        = [False] * 20
MASK_VISUAL_LAYER[1]     = True
MASK_CAST_SHADOW         = "OFF"
MASK_GI_MODE             = "DISABLED"

OBJECT_AREA_COLLISION_NAME  = "Area"
OBJECT_AREA_COLLISION_TYPE  = "AREA"
OBJECT_AREA_COLLISION_SHAPE = "BOUNDARIES"
OBJECT_AREA_COLLISION_COLOR = (0.07, 0.413, 0.021, 0.42)
OBJECT_AREA_COLLISION_MASK  = [False] * 32
OBJECT_AREA_COLLISION_LAYER  = [False] * 32

OBJECT_AREA_COLLISION_MASK[0] = True

OBJECT_BODY_COLLISION_NAME  = "Body"
OBJECT_BODY_COLLISION_SHAPE = "TRIMESH"
OBJECT_BODY_COLLISION_TYPE  = "STATIC_BODY"
OBJECT_BODY_COLLISION_MASK  = [False] * 32
OBJECT_BODY_COLLISION_LAYER = [False] * 32

OBJECT_BODY_COLLISION_LAYER[1] = True
OBJECT_BODY_COLLISION_MASK[0]  = True

OBJECT_GEOMETRY_CAST_SHADOW = "DOUBLE_SIDED"

def mask_material():
    mat = bpy.data.materials.get(MASK_MATERIAL_NAME)
    if mat is None:
        mat = bpy.data.materials.new(name=MASK_MATERIAL_NAME)
        mat.goblend.shade_mode = MASK_MATERIAL_SHADE_MODE
    return mat

class TUNEUR_OP_CreateMask(bpy.types.Operator):
    bl_idname = "tuneur.create_mask"
    bl_label = "Create Mask"

    def execute(self, context):
        obj = context.object
        if obj is None:
            return CANCELLED

        if obj.name.endswith(MASK_DISCRIMINATOR):
            return CANCELLED

        mask_obj_name = obj.name + MASK_DISCRIMINATOR
        if bpy.data.objects.get(mask_obj_name) is not None:
            return CANCELLED

        # MASK

        mask = obj.copy()
        mask.data = obj.data.copy()
        mask.name = mask_obj_name

        mask.tuneur.type.type                 = "MASK"
        mask.goblend.layers                   = MASK_VISUAL_LAYER
        mask.goblend.geometry.cast_shadow     = MASK_CAST_SHADOW
        mask.goblend.global_illumination.mode = MASK_GI_MODE
        mask.active_material = mask_material()

        obj.users_collection[0].objects.link(mask)

        mask.parent = obj
        mask.matrix_parent_inverse = obj.matrix_world.inverted()

        # OBJECT

        obj.goblend.collisions.list.add() # Body
        obj.goblend.collisions.list.add() # Area

        index = len(obj.goblend.collisions.list)
        static_index = index-2
        area_index   = index-1

        obj.tuneur.type.type = "ROOM"

        obj.goblend.collisions.list[static_index].name  = OBJECT_BODY_COLLISION_NAME
        obj.goblend.collisions.list[static_index].shape = OBJECT_BODY_COLLISION_SHAPE
        obj.goblend.collisions.list[static_index].type  = OBJECT_BODY_COLLISION_TYPE
        obj.goblend.collisions.list[static_index].layer = OBJECT_BODY_COLLISION_LAYER
        obj.goblend.collisions.list[static_index].mask  = OBJECT_BODY_COLLISION_MASK

        obj.goblend.collisions.list[area_index].name  = OBJECT_AREA_COLLISION_NAME
        obj.goblend.collisions.list[area_index].shape = OBJECT_AREA_COLLISION_SHAPE
        obj.goblend.collisions.list[area_index].type  = OBJECT_AREA_COLLISION_TYPE
        obj.goblend.collisions.list[area_index].color = OBJECT_AREA_COLLISION_COLOR
        obj.goblend.collisions.list[area_index].layer = OBJECT_AREA_COLLISION_LAYER
        obj.goblend.collisions.list[area_index].mask  = OBJECT_AREA_COLLISION_MASK

        obj.goblend.geometry.cast_shadow      = OBJECT_GEOMETRY_CAST_SHADOW

        return FINISHED