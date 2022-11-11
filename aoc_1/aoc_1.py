values = []
increased = 0
 

for line in open('aoc_1_values.txt').readlines():
    values.append(line)
    print(line)

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
first_three = []
second_three = []
third_three = []


for elem in values:
    if elem == values[0]:
        first_three.append(elem);
    else:
        if len(first_three) % 3 != 0:
            first_three.append(elem)

        if len(second_three) % 3 != 0:
            second_three.append(elem)

        if len(third_three) % 3 != 0:
            third_three.append(elem)

        print(len(first_three))
        if len(first_three) % 3 == 0:
            if first_three[0] + first_three[1] + first_three[2] <  second_three[0] + second_three[1] + second_three[2]:
                increased += 1
                print("increased")
            first_three.clear()

        
        if len(second_three) % 3 == 0:
            if second_three[0] + second_three[1] + second_three[2] <  third_three[0] + third_three[1] + third_three[2]:
                increased += 1
            second_three.clear()

        if len(third_three) % 3 == 0:
            if third_three[0] + third_three[1] + third_three[2] <  first_three[0] + first_three[1] + first_three[2]:
                increased += 1
            third_three.clear()
print("Measurements increased", increased, "times!")






