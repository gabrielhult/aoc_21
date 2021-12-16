values = []
increased = 0

import os
print(os.getcwd())

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "aoc_2_values.txt")
fh = open(lines)

for line in fh.readlines():
    #print(line.split())
    values.append(tuple(line.split()))
    print(tuple(line.split()))


hz_sum = 0
depth_sum = 0
aim_sum = 0
sum = 0

for elem in range(len(values)):
    if values[elem][0] == 'forward':
        hz_sum += int(values[elem][1])
        depth_sum = depth_sum + (int(values[elem][1]) * aim_sum)
        #print("temp aim ", aim_sum)
        #print("hz sum now ", hz_sum)
        #print("temp depth sum ", depth_sum)

    elif values[elem][0] == 'up':
        aim_sum -= int(values[elem][1])

    elif values[elem][0] == 'down':
        aim_sum += int(values[elem][1])
    

print("Horizontal sum: ", hz_sum)
print("Aim sum: ", aim_sum)
print("Depth sum: ", depth_sum)

sum = hz_sum * depth_sum
print("Total sum: ", sum)
