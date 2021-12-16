values = []
increased = 0

import os
print(os.getcwd())

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "aoc_2_values.txt")
fh = open(lines)

for line in fh.readlines():
    values.append(line)
    print(line)


hz_sum = 0
depth_sum = 0

for elem in range(len(values)):
    if values[elem] == 
