import bpy
import bmesh
import os

def export_convex_hull_points(obj, filepath):
    # Create a new bmesh and fill it with the object's mesh data
    bm = bmesh.new()
    bm.from_mesh(obj.data)

    # Create the convex hull
    bmesh.ops.convex_hull(bm, input=bm.verts)

    # Extract vertices from the convex hull
    vertices = [v.co.copy() for v in bm.verts]

    # Write to file
    with open(filepath, 'w') as f:
        f.write(f"shape_type: TYPE_HULL\n")
        for v in vertices:
            f.write(f"data: {v.x}\n")
            f.write(f"data: {v.y}\n")
            f.write(f"data: {v.z}\n")

    # Free the bmesh
    bm.free()

# Ensure the correct object is selected
obj = bpy.context.object

# Specify the export path
export_path =  os.path.join(bpy.path.abspath("//"), "monkey.convexshape")

# Export the convex hull points
export_convex_hull_points(obj, export_path)

print(f"Convex hull points exported to {export_path}")
