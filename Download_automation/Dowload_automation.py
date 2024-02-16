from os import scandir

from shutil import move

source_dir = 'C:/Users/samue/Downloads'
dest_model_dir = 'C:/Users/samue/OneDrive/3D Models'

model_extensons = (".stl", ".3mf", ".STL", "3MF")

def move_models():
    with scandir(source_dir) as entries:
        for entry in entries:
            name = entry.name
            if name.endswith(model_extensons):
                move(entry, dest_model_dir)
                print(name)

move_models()
