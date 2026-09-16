# Parsing VASP and Gaussian Output files with pymatgen
## Parsing molecule structure from gaussian.log

# We import the module load parse gaussian output files
from pymatgen.io.gaussian import GaussianOutput

# Reading the log file
gout = GaussianOutput("gaussian/tddft.log")

# Final structure
gout.final_structure

# Save structure data as CIF file
from pymatgen.core import Structure
structure = gout.final_structure

structure.to(filename="molecule_summary.xyz")