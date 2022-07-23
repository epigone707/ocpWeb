from ase import io
from ase.io import write
from ase.visualize import view
import os
import uuid

def visualize_extxyz(filename = 'CaAg.extxyz'):
    filepath = 'server/uploads/'
    print("visualize_extxyz(filename=",filename,")")
    catalyst = io.read(os.path.join(filepath, filename))
    
    visual_filename = str(uuid.uuid4()) + ".png"
    write(os.path.join(filepath, visual_filename), catalyst)
    # view(Cu, viewer='x3d')
    return visual_filename