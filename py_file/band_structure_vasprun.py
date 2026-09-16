# Parsing VASP and Gaussian Output files with pymatgen
## Parsing band Structure data from vasprun.xml

# Load vasprun from pymatgen
from pymatgen.io.vasp import Vasprun, BSVasprun

# read the xml file
vasprun = Vasprun("vasp/vasprun.xml/vasprun.xml")

# Plot Band structure
from pymatgen.io.vasp import Vasprun, BSVasprun
from pymatgen.electronic_structure.plotter import BSPlotter

v = BSVasprun("vasp/vasprun.xml/vasprun.xml")
bs = v.get_band_structure(kpoints_filename="vasp/KPOINTS",line_mode=True)
plt = BSPlotter(bs)
plt.get_plot(vbm_cbm_marker=True,ylim=(-3,3))
plt.show()