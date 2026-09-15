---
title: "Parsing VASP and Gaussian's Output Files with Python"
date: "2026-09-13"
---

[![](https://colab.research.google.com/assets/colab-badge.svg)]()

# Objectives

- Sort all information in a text file and extract particular pieces of information;
- Open file and read in its contents line by line;
- Search for a particular string in a file;
- Manipulate strings and change data types;
- Print a new file.
  
# Parsing Computational Chemistry Output Files with Pymatgen

One of the most common tasks in research is analyzing data. Many computational chemistry programs output text files that include a large amount of information including text and data that you need to analyze. Often, we need to sort through the output file and identify particular pieces of information that are most important to us. In general, this is called __file parsing__.

Parsing is the process of uncovering the derivation, or derivation tree, of a string from a grammar. We want to get the parse tree because a lot of meaning is often encoded in the structure of the string. Parsing enables the retrieval of details, from text or files aiding in data handling, search functions and information retrieval.

# Pymatgen

[Pymatgen (Python Materials Genomics)](https://pymatgen.org/) is a robust, open-source Python library for material analysis. One of the main features is extensive input/output support, including support for VASP, ABINIT, CIF, Gaussian, XYZ and many other file formats. Pytmatgen is also integrated with the Materials Projects REST API, Crystallography Open Database and other external data sources.

# VASP

[VASP (The Vienna ab-initio simulation package)](https://vasp.at/wiki/Category:Theory) is a computer program for atomic scale materials modeling from first principle. VASP computes an approximate solution to the many-body Schrodinger equation to obtain [electronic ground state](https://vasp.at/wiki/Category:Electronic_ground-state_properties). In VASP, central quantities, like the one-electron orvitala, the electronic charge density, and the local potential are expressed in plane-wave basis using the [projector-augmented-wave (PAW)](https://vasp.at/wiki/Projector-augmented-wave_formalism) method. 

## VASP Output files

The main output file of VASP is the [OUTCAR](https://vasp.at/wiki/Category:Output_files). The [vasprun.xml](https://vasp.at/wiki/Vasprun.xml) contains similar information but in an xml format. Here is a comprehensive list of some output and input files:

- [__KPOINTS__](https://vasp.at/wiki/KPOINTS): The __KPOINTS__ file specifies the Bloch vectors (k points) used to sample the Brillouin zone. __KPOINTS__ play an important rule in discretizing the Brillouin zone of a crystal. A sufficently dense __KPOINTS__ mesh is critical for the precision of your DFT calculation, so make sure to the test the results for different meshes.

- [__vasprun.xml__](https://vasp.at/wiki/Vasprun.xml): The main output file in xml format.
  
- [__OUTCAR__](https://vasp.at/wiki/Category:Output_files): The Main output file, human-readable format.

- [__POSCAR__](https://vasp.at/wiki/POSCAR): This file is a mandatory VASP input file. It is a plain text file and contains at least the lattice, geometry and the ionic positions. Creating a __POSCAR__ file is often the starting point of VASP-supported research.

# Gaussian

Gaussian is a computer program to predict the energies, molecular structures, and vibrational frequencies of complex molecular systems and to anticipate their chemical properties.

## Gaussian Logfile

The [logfile](https://emleddin.github.io/comp-chem-website/Otherguide-gaussian-results.html) (`.log` or `.out`) contains all of the job information. A typical Gaussian Output file can see [here](https://www.cup.uni-muenchen.de/ch/compchem/basic/g03output.html).

>
This is example code for parsing VASP and Gaussian file formats using the Pymatgen Python library
>