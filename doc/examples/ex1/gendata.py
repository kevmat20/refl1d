"""
Generate Ni-film sample data files so that we can demonstrate file loading.
"""
import sys;
sys.path.insert(0,'../../..')
sys.path.insert(1,'../../../dream')
sys.path.insert(2,'../..')
from numpy.random import seed
from sitedoc import SEED
from refl1d.fitter import load_problem
from refl1d.snsdata import write_file

seed(SEED)
problem = load_problem('nifilm-tof.py')
for i,p in enumerate(problem.fitness.probe.probes):
    write_file('nifilm-tof-%d.dat'%(i+1), p, title="Simulated 100 A Ni film")
