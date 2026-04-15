import bpy

MASK_COLLECTION_NAME = "_masks"
MASK_DISCRIMINATOR = "-mask"

def mask_collection():
    collection = bpy.data.collections.get(MASK_COLLECTION_NAME)
    if collection is None:
        collection = bpy.data.collections.new(MASK_COLLECTION_NAME)
        bpy.context.scene.collection.children.link(collection)
        
    return collection

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

        mask_col.objects.link(mask)

        return FINISHED