import sys
sys.path.insert(0,'/home/felix/git/test/blase/')

from ase.build import molecule
from ase.visualize import view
from blase.tools import get_bondpairs, write_blender

atoms = molecule('C2H6SO')
atoms.center(vacuum  = 1.0)
camera_loc = atoms[3].position + [20, 0, 10]

kwargs = {'show_unit_cell': 0,
          'engine': 'CYCLES',# 'CYCLES', #'BLENDER_EEVEE' #'BLENDER_WORKBENCH'
          'camera_loc': camera_loc,  # distance from camera to front atom
          'camera_type': 'PERSP',  #  ['PERSP', 'ORTHO', 'PANO']
          'camera_lens': 100,  #
          'camera_target': atoms[4].position, #
          'ortho_scale': None, #
          'radii': 0.6,
          'bond_cutoff': 1.0,
          'light_loc': atoms[4].position+ [0, 0, 10],
          'light_type': 'SUN', # 'POINT', 'SUN', 'SPOT', 'AREA'
          'point_lights': [],  #
          'light_strength': 50,
          'gpu': False,
          'run_render': False,
          'display': False,
          'functions': [['draw_plane', {'size': 1000, 'location': (0, 0, -1.0)}]],
          'resolution_x': 1000,
          'num_samples': 20,
          # 'functions': [['draw_plane', {'size': 100, 'location': (0, 0, -0.0), 'color': (0.1, 0.1, 0.1, 1.0), 'material_style': 'mirror'}]],
          # 'outfile': 'figs/c2h6so-cycles',
          }
write_blender(atoms, **kwargs)