import bpy

from ..helper import *

MASK_COLLECTION_NAME = "_masks"
MASK_DISCRIMINATOR = "-mask"

MASK_MATERIAL_NAME = "Mask"
MASK_MATERIAL_SHADE_MODE = "UNSHADED"

MASK_VISUAL_LAYER = [False] * 20
MASK_VISUAL_LAYER[1] = True
MASK_COLLISION_TYPE = "AREA"
MASK_COLLISION_SHAPE = "BOUNDARIES"
MASK_COLLISION_COLOR = (0.07, 0.413, 0.021, 0.42)

OBJECT_COLLISION_SHAPE = "TRIMESH"
OBJECT_COLLISION_TYPE = "STATIC_BODY"
OBJECT_GEOMETRY_CAST_SHADOW = "DOUBLE_SIDED"

def mask_collection():
    collection = bpy.data.collections.get(MASK_COLLECTION_NAME)
    if collection is None:
        collection = bpy.data.collections.new(MASK_COLLECTION_NAME)
        bpy.context.scene.collection.children.link(collection)
        
    return collection

def mask_material():
    mat = bpy.data.materials.get(MASK_MATERIAL_NAME)
    if mat is None:
        mat = bpy.data.materials.new(name=MASK_MATERIAL_NAME)
        mat.goblend.shade_mode = MASK_MATERIAL_SHADE_MODE
    return mat

class CreateMaskOperator(bpy.types.Operator):
    bl_idname = "tuneur.create_mask"
    bl_label = "Create Mask"

    def execute(self, context):
        obj = context.object
        if obj is None:
            return CANCELLED

        if obj.name.endswith(MASK_DISCRIMINATOR):
            return CANCELLED

        mask_col = mask_collection()
        mask_obj_name = obj.name + MASK_DISCRIMINATOR
        if bpy.data.objects.get(mask_obj_name) is not None:
            return CANCELLED

        mask = obj.copy()
        mask.data = obj.data.copy()
        mask.name = mask_obj_name

        mask.goblend.collision.has_collision   = True
        mask.goblend.collision.collision_shape = MASK_COLLISION_SHAPE
        mask.goblend.collision.collision_type  = MASK_COLLISION_TYPE
        mask.goblend.collision.color           = MASK_COLLISION_COLOR
        mask.goblend.layers                    = MASK_VISUAL_LAYER
        mask.active_material                   = mask_material()

        mask_col.objects.link(mask)

        obj.goblend.collision.has_collision   = True
        obj.goblend.collision.collision_shape = OBJECT_COLLISION_SHAPE
        obj.goblend.collision.collision_type  = OBJECT_COLLISION_TYPE
        obj.goblend.geometry.cast_shadow      = OBJECT_GEOMETRY_CAST_SHADOW

        return FINISHED