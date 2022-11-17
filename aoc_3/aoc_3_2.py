values = []

import os
print(os.getcwd())

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "aoc_3_values.txt")
fh = open(lines)

#Oxygen generator rating
zero_counter = 0
one_counter = 0

for binary in fh:
    if(binary[0] == 1):
        one_counter += 1
    else:
        zero_counter += 1

if(one_counter > zero_counter):
    print("To be continued")



    