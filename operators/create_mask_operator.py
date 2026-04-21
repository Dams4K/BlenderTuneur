import bpy

from ..helper import *

MASK_DISCRIMINATOR       = "-mask"
BOUNDARIES_DISCRIMINATOR = "-boundaries"

MASK_MATERIAL_NAME       = "Mask"
MASK_MATERIAL_SHADE_MODE = "UNSHADED"
MASK_VISUAL_LAYER        = [False] * 20
MASK_VISUAL_LAYER[1]     = True
MASK_CAST_SHADOW         = "OFF"
MASK_GI_MODE             = "DISABLED"


BOUNDARIES_AREA_COLLISION_NAME    = "Area"
BOUNDARIES_AREA_COLLISION_TYPE    = "AREA"
BOUNDARIES_AREA_COLLISION_SHAPE   = "BOUNDARIES"
BOUNDARIES_AREA_COLLISION_COLOR   = (0.07, 0.413, 0.021, 0.42)
BOUNDARIES_AREA_COLLISION_MASK    = [False] * 32
BOUNDARIES_AREA_COLLISION_MASK[0] = True
BOUNDARIES_AREA_COLLISION_LAYER   = [False] * 32
BOUNDARIES_CAST_SHADOW            = "OFF"
BOUNDARIES_GI_MODE                = "DISABLED"
BOUNDARIES_COLLISION_ONLY         = True

OBJECT_BODY_COLLISION_NAME  = "Body"
OBJECT_BODY_COLLISION_SHAPE = "TRIMESH"
OBJECT_BODY_COLLISION_TYPE  = "STATIC_BODY"
OBJECT_BODY_COLLISION_MASK  = [False] * 32
OBJECT_BODY_COLLISION_MASK[0]  = True
OBJECT_BODY_COLLISION_LAYER = [False] * 32
OBJECT_BODY_COLLISION_LAYER[1] = True

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

        if obj.name.endswith(BOUNDARIES_DISCRIMINATOR):
            return CANCELLED

        # MASK
        if not obj.tuneur.room.mask:
            mask_obj_name = obj.name + MASK_DISCRIMINATOR
            mask = obj.copy()
            mask.data = obj.data.copy()
            mask.name = mask_obj_name

            mask.goblend.collisions.list.clear()
            mask.goblend.collisions.index = 0

            mask.tuneur.type.type                 = "MASK"
            mask.goblend.layers                   = MASK_VISUAL_LAYER
            mask.goblend.geometry.cast_shadow     = MASK_CAST_SHADOW
            mask.goblend.geometry.gi_mode         = MASK_GI_MODE
            mask.active_material = mask_material()

            obj.users_collection[0].objects.link(mask)

            mask.parent = obj
            mask.matrix_parent_inverse = obj.matrix_world.inverted()

            obj.tuneur.room.mask = mask

        # OBJECT - Body
        index = len(obj.goblend.collisions.list)
        if not any(col.name == OBJECT_BODY_COLLISION_NAME for col in obj.goblend.collisions.list):
            obj.goblend.collisions.list.add()
            index += 1

            obj.goblend.collisions.list[index].name  = OBJECT_BODY_COLLISION_NAME
            obj.goblend.collisions.list[index].shape = OBJECT_BODY_COLLISION_SHAPE
            obj.goblend.collisions.list[index].type  = OBJECT_BODY_COLLISION_TYPE
            obj.goblend.collisions.list[index].layer = OBJECT_BODY_COLLISION_LAYER
            obj.goblend.collisions.list[index].mask  = OBJECT_BODY_COLLISION_MASK

        obj.tuneur.type.type = "ROOM"
        
        # BOUNDARIES
        if not obj.tuneur.room.boundaries:
            boundaries_obj_name = obj.name + BOUNDARIES_DISCRIMINATOR
            boundaries = obj.copy()
            boundaries.data = obj.data.copy()
            boundaries.name = boundaries_obj_name

            boundaries.goblend.collisions.list.clear()
            boundaries.goblend.collisions.index = 0

            boundaries.tuneur.type.type                  = "BOUNDARIES"
            boundaries.goblend.geometry.cast_shadow      = BOUNDARIES_CAST_SHADOW
            boundaries.goblend.geometry.gi_mode          = BOUNDARIES_GI_MODE
            boundaries.goblend.collisions.collision_only = BOUNDARIES_COLLISION_ONLY

            boundaries.goblend.collisions.list.add() # Area
            area_index = 0

            boundaries.goblend.collisions.list[area_index].name  = BOUNDARIES_AREA_COLLISION_NAME
            boundaries.goblend.collisions.list[area_index].shape = BOUNDARIES_AREA_COLLISION_SHAPE
            boundaries.goblend.collisions.list[area_index].type  = BOUNDARIES_AREA_COLLISION_TYPE
            boundaries.goblend.collisions.list[area_index].color = BOUNDARIES_AREA_COLLISION_COLOR
            boundaries.goblend.collisions.list[area_index].layer = BOUNDARIES_AREA_COLLISION_LAYER
            boundaries.goblend.collisions.list[area_index].mask  = BOUNDARIES_AREA_COLLISION_MASK

            obj.users_collection[0].objects.link(boundaries)

            boundaries.parent = obj
            boundaries.matrix_parent_inverse = obj.matrix_world.inverted()

            obj.tuneur.room.boundaries = boundaries


        obj.goblend.geometry.cast_shadow      = OBJECT_GEOMETRY_CAST_SHADOW

        return FINISHED