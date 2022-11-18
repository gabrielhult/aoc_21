import os
print(os.getcwd())

values = []


def main():
    with open("aoc_3/aoc_3_values.txt", "r") as f:
        fh = f.read().split("\n")
    bit = 0
    a = int(oxygenRating(fh, bit), 2)
    print("This is our Oxygen generator rating: " + str(a))
    b = int(scrubberRating(fh, bit), 2)
    print("This is our C02 scrubber rating: " + str(b))

    print("The life support rating is: " + str(a * b))


#Oxygen generator rating
def oxygenRating(binary_list, bit): 
    if(len(binary_list) == 1):
        return binary_list[0]
    else:
        zero_list = []
        one_list = []
        zero_counter = 0
        one_counter = 0 
        for binary in binary_list:
            if(binary[bit] == "1"):
                one_counter += 1
                one_list.append(binary)
            else:
                zero_counter += 1
                zero_list.append(binary)
            
        if(one_counter >= zero_counter):
            return oxygenRating(one_list, bit+1)
        else:
            return oxygenRating(zero_list, bit+1)

#Oxygen generator rating
def scrubberRating(binary_list, bit): 
    if(len(binary_list) == 1):
        return binary_list[0]
    else:
        zero_list = []
        one_list = []
        zero_counter = 0
        one_counter = 0 
        for binary in binary_list:
            if(binary[bit] == "1"):
                one_counter += 1
                one_list.append(binary)
            else:
                zero_counter += 1
                zero_list.append(binary)
            
        if(one_counter < zero_counter):
            return scrubberRating(one_list, bit+1)
        else:
            return scrubberRating(zero_list, bit+1)

if __name__ == "__main__":
    main()

    