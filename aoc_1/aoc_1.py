values = []
increased = 0
 

for line in open('aoc_1_values.txt').readlines():
    values.append(line)
    print(line)

#part 1    
"""
for elem in range(len(values)):
    if elem == 0:
        print("First element, don't check.")
        increased += 1
    else:
        if values[elem] > values[elem-1]:
            print("now ", values[elem], " and before ", values[elem-1])
            increased += 1
print("amount increased: ", increased)
"""

remaining_elements = len(values)
first_sum = 0
second_sum = 0
third_sum = 0
current_pair_count = 0  
new_pair_count = 0 

first_three_counter = 0

#part 2
for line in open('aoc_1_values.txt').readlines():
    values.append(line)
    #print(line)

for elem in range(len(values)):
    if first_three_counter == 0:
        first_sum += values[elem]
        first_three_counter += 1
    elif first_three_counter == 0:
        second_sum += values[elem]
        first_three_counter += 1
    elif first_three_counter == 2:
        third_sum += values[elem]
        first_three_counter += 1
