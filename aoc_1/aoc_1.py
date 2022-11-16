values = []
increased = 0


for line in open('/home/gult/advent_of_code_2k21/aoc_1/aoc_1_values.txt').readlines():
    values.append(int(line))
    #print(line)

#part 1    

""" for elem in range(len(values)):
    if elem == 0:
        #print("First element, don't check.")
        increased += 1
    else:
        if values[elem] > values[elem-1]:
            #print("now ", values[elem], " and before ", values[elem-1])
            increased += 1
print("Value increased", increased, "times!") """

#part 2
remaining_elements = len(values)


prev_depth_sum = sum(values[0 : 3])
count_inc = 0

for depth in range(1, len(values) - (3 - 1)):
    _depths_sum = sum(values[depth : depth + 3])

    if _depths_sum > prev_depth_sum:
        increased += 1
    
    prev_depth_sum = _depths_sum


print("Measurements increased", increased, "times!")






