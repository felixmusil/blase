import sys, os

blase_path = os.environ['BLASE_PATH']
sys.path.insert(0,blase_path)


from ase.io import read
from ase.io.cube import read_cube_data
from blase.bio import Blase
from blase.btools import draw_cell, draw_atoms, draw_bonds, draw_polyhedras, draw_isosurface, bond_source, cylinder_mesh_from_instance, clean_default
import pickle
import argparse



def main(inputfile='blase.inp'):
    print('='*30)
    print('Running blender')
    print('='*30)
    with open(inputfile, 'rb') as f:
        images, kwargs = pickle.load(f)

    bobj = Blase(images, **kwargs)

    bobj.draw()
    for function in bobj.functions:
        name, paras = function
        getattr(bobj, name)(**paras)

    bobj.render()
    print('\n Finished!')

# to use argparse with blender
# https://medium.com/@andreasklostermann/turn-your-blender-scripts-into-command-line-applications-8a683e79bbb8
if __name__ == "__main__":
    arguments = sys.argv[sys.argv.index("--")+1:]
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("--inputfile", help="Name of the file containing the structure and parameters")
    args = parser.parse_args(arguments)

    main(args.inputfile)

    # main()