import bpy
import bmesh
import math
from mathutils import Vector
import os

def calculate_ccw_order(vertices):
    # Calculate the center of the vertices
    center = sum((v for v in vertices), Vector()) / len(vertices)
    
    # Sort vertices counter-clockwise around the center
    vertices_sorted = sorted(vertices, key=lambda v: math.atan2(v.y - center.y, v.x - center.x))
    return vertices_sorted

def export_convex_hull_points(obj, filepath):
    # Create a new bmesh and fill it with the object's mesh data
    bm = bmesh.new()
    bm.from_mesh(obj.data)

    # Create the convex hull
    convex_hull = bmesh.ops.convex_hull(bm, input=bm.verts)

    # Extract vertices
    vertices = [v.co.copy() for v in bm.verts]

    # Sort vertices counter-clockwise
    vertices_sorted = calculate_ccw_order(vertices)

    # Write to file
    with open(filepath, 'w') as f:
        for v in vertices_sorted:
            f.write(f"data: {v.x}\n")
            f.write(f"data: {v.y}\n")
            f.write(f"data: {v.z}\n")

    # Free the bmesh
    bm.free()

# Ensure the correct object is selected
obj = bpy.context.object

# Specify the export path
export_path =  os.path.join(bpy.path.abspath("//"), "file_name.convexshape")

# Export the convex hull points
export_convex_hull_points(obj, export_path)

print(f"Convex hull points exported to {export_path}")
