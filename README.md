---
title: "Parsing VASP and Gaussian's Output Files with Python"
date: "2026-09-13"
---

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1V8eIcKkPiZPYpxBgEKTE9QiSL3tW3IRT?usp=sharing)

  
# Parsing Computational Chemistry Output Files with Pymatgen

One of the most common tasks in research is analyzing data. Many computational chemistry programs output text files that include a large amount of information including text and data that you need to analyze. Often, we need to sort through the output file and identify particular pieces of information that are most important to us. In general, this is called __file parsing__.

Parsing is the process of uncovering the derivation, or derivation tree, of a string from a grammar. We want to get the parse tree because a lot of meaning is often encoded in the structure of the string. Parsing enables the retrieval of details, from text or files aiding in data handling, search functions and information retrieval.

# Generic Text Parsing
We will use regular expressions for parsing text files (https://en.wikipedia.org/wiki/Regular_expression). A regular expressing (shortened as regex) is a sequence of characters that specifies a match pattern in text. Usually such patterns are used by [string-searching algorithms](https://en.wikipedia.org/wiki/String-searching_algorithm) for "find" or "find" and "replace" operations on strings, or for input validation. 

The workflow for parsing computational chemistry output files:

1. Find a unique pattern for the start of parsing segement (`SCF Done`, `Optimized Parameters`, `Mulliken charges`).
2. Find a pattern for the end of segment, a pattern of the final section.
3. Read the file (line by line).
4. Look for the line with start pattern (`in_section = True`).
5. Starting the parsing code until end pattern is encountered (extract and process data while the `in_section = True`).

## Parsing Gaussian file for Mulliken Energy

```python
# import regular expression module
import re

# We will parse the Mulliken Charges for all atoms
# Find the pattern
start_pattern = re.compile(r'Mulliken charges:')

# The pattern at the end
end_pattern = re.compile(r'Sum of Mulliken charges')

# Read the file
with open("gaussian/tddft.log") as f:
    lines = f.readlines()
```
<br>
We will use `re.match()` to check whether the line contains our start pattern.
<br>

```python
# Find line with start pattern of Mulliken charges
for idx, line in enumerate(lines): # loops over the lines
    if re.match(start_pattern, line.strip()):
        break
print(idx)
```
```
1401
```
<br>
To stop parsing we will again use `re.match()` to match the end pattern. We will apply lines to the list.
<br>

```python
# start parse lines
idx = idx + 2
line = lines[idx]

parsed_lines = []
while not(re.match(end_pattern, line.strip())):
    parsed_lines.append(line.strip())
    idx += 1
    line = lines[idx]
    
# Clean up the data
data =[]
for line in parsed_lines:
    clean_line = line.strip().split()
    data.append({"number": int(clean_line[0]), 
     "atom": clean_line[1], 
     "charge": float(clean_line[2])})

# Create a table with pandas
import pandas as pd

pd.DataFrame(data)

# save as CSV file
df = pd.DataFrame(data)
df.to_csv("parsing_MC.csv", index = False)

```

The parsed Gaussian output file for Mulliken charges can be seen in the CSV file [here](parsing_result/parsing_MC.csv).

# Parsing VASP and Gaussian Output files with pymatgen
We can also parse any text file created by VASP with pymatgen. Below is an example to parse the `vasprun.xml` output file.

## Parsing band Structure data from vasprun.xml

```python
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
```

<p align='center'>
<img src = "band_structure.svg" width = "300">  
</p>


## Parsing molecule structure from gaussian.log
The modules to parse gaussian are available in pymatgen. Other codes which can be parsed are listed here (https://pymatgen.org/pymatgen.html).

```python
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

``` 
The parsed Gaussian output file for final structure can be seen in the XYZ file [here](parsing_result/molecule_summary.xyz).
