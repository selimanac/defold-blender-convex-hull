# Creating Convex Hull in Blender

This small script is tested with Blender 4.1.1. It might not work any older versions.  
You can find the example Blender project and Python Scripts in the `blender` [folder](https://github.com/selimanac/defold-blender-convexhull/tree/main/blender) of this repo.  
Defold project contains example [Convex hull](https://defold.com/manuals/physics-shapes/#convex-hull-shape) shapes.  


### Create Convex Hull in Blender:
- Load your model and prepare it for [importing Defold](https://defold.com/manuals/importing-models/#using-a-model).   
- Select the model/object and switch to `Edit Mode` (`Tab`).  

![Edit Mode](/.github/1.jpg?raw=true)

- Select all vertices (`A`).    

![Select all vertices](/.github/2.jpg?raw=true)

- Use the "Convex Hull" operation (press F3, search for "Convex Hull") or select "Mesh" -> "Convex Hull" from menu.   

![Convex Hull](/.github/3.jpg?raw=true)

### Export Convex Hull Points Using Python Script:

- Go to the Scripting tab or open a new `Text Editor` in Blender.  

![Text Editor](/.github/4.jpg?raw=true)


- Copy and paste [the script](https://github.com/selimanac/defold-blender-convexhull/blob/main/blender/convexshape.py) into the scripting editor.   
- Adjust the `export_path` variable to the desired file path where you want to save the exported convex hull data.   
- Ensure the correct object is **selected**.     
- Click the `Run Script` button in the scripting editor.  

![Run Scrip](/.github/5.jpg?raw=true)

This should correctly export the convex hull data to the specified file.  

```python

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
# Default is .blender file's folder
export_path =  os.path.join(bpy.path.abspath("//"), "file_name.convexshape")

# Export the convex hull points
export_convex_hull_points(obj, export_path)

print(f"Convex hull points exported to {export_path}")


```