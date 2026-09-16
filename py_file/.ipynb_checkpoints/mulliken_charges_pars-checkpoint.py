# This is example code for parsing VASP and Gaussian file formats using the Pymatgen Python library
## Generic text Parsing Gaussian file for Mulliken Energy

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

# Find line with start pattern of Mulliken charges
for idx, line in enumerate(lines): # loops over the lines
    if re.match(start_pattern, line.strip()):
        break
print(idx)

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