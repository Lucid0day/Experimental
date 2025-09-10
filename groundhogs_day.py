"""
Lucid0day
09/09/25
Christian DeCoske
I hope you enjoy the creativity in this idea.
The purpose of this program is be able to alter its own code and 
run itself again. 
"""

import os
import sys

filename = os.path.abspath(__file__)
max_lines = 10  # maximum hello world lines

# Read current file
with open(filename, "r") as f:
    lines = f.readlines()

# Count existing hello world lines
hello_count = sum(1 for line in lines if line.strip() == 'print("hello world")')

# Append a new line if we haven't reached max
if hello_count < max_lines:
    lines.append('print("hello world")\n')
    with open(filename, "w") as f:
        f.writelines(lines)

# Print hello world
print("hello world")

# Restart the program so it executes with the updated file
os.execv(sys.executable, [sys.executable, filename])
