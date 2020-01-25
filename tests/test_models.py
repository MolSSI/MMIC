import sys

sys.path.insert(0, '..')

from models import input
import numpy
import os
from qcelemental import models

# Test input file
pdb_file = os.path.abspath('data/dialanine/dialanine.pdb')

docking_input_data = input.DockingInputData(
					Ligand='CCC', 
					Receptor=pdb_file
					)

from DockingImplementation.openbabel_component import OpenBabel
from DockingImplementation.grep_component import Grep
from DockingImplementation.autodock_prep_component import AutoDockPrep
from DockingImplementation.input_prep_component import MolSSIInputPrep

from config import TaskConfig


# Test MolSSIInputPrep
docking_input = MolSSIInputPrep.compute(docking_input_data)
docking_input.Receptor.write_pdb('tmp.pdb')

# Test for openbabel
obabel_input = input.OpenBabelInput(Input=pdb_file, OutputExt='pdbqt')
obabel_output = OpenBabel.compute(input_data=obabel_input)

#with open('test.pdbqt', 'w') as fp:
#	fp.write(obabel_output.FileContents)

# Test for grep
grep_input = input.GrepInput(Input=pdb_file, Pattern='REMARK')
grep_output = Grep.compute(input_data=grep_input)

#with open('test.grep', 'w') as fp:
#	fp.write(grep_output.FileContents)

# Test for AutodockPrep
# ADP = AutoDockPrep.compute(input_data=docking_input_data)
