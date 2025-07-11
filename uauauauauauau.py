from stl import mesh
import numpy as np

# Define 8 vertices of the cube
vertices = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
])

# Define the 12 triangles that make up the cube faces
faces = np.array([
    [0,3,1], [1,3,2],
    [0,4,7], [0,7,3],
    [4,5,6], [4,6,7],
    [5,1,2], [5,2,6],
    [2,3,6], [3,7,6],
    [0,1,5], [0,5,4]
])

# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, face in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[face[j]]

# Save to file
cube.save('cube.stl')
