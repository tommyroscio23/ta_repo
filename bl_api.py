import bpy

# Load lab 1.1 project
bpy.ops.wm.open_mainfile(filepath="blender/lab_1_1.blend")

# Delete existing spheres
for obj in bpy.data.objects:
    if obj.type == "MESH":
        bpy.ops.object.delete()

# Create sphere
bpy.ops.mesh.primitive_uv_sphere_add(
    radius=2, enter_editmode=False, align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
)

# Save changes
bpy.ops.wm.save_mainfile()
