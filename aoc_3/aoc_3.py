values = []

import os
print(os.getcwd())

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "aoc_3_values.txt")
fh = open(lines)

for line in fh.readlines():
    values.append(line)
    #print(line)

one_list = []
two_list = []
three_list = []
four_list = []
five_list = []
six_list = []
seven_list = []
eight_list = []
nine_list = []
ten_list = []
eleven_list = []
twelve_list = []

gamma_rate = ""
epsilon_rate = ""


for elem in values:
    one_list.append(elem[0])
    two_list.append(elem[1])
    three_list.append(elem[2])
    four_list.append(elem[3])
    five_list.append(elem[4])
    six_list.append(elem[5])
    seven_list.append(elem[6])
    eight_list.append(elem[7])
    nine_list.append(elem[8])
    ten_list.append(elem[9])
    eleven_list.append(elem[10])
    twelve_list.append(elem[11])

one_bit_counter = 0
zero_bit_counter = 0

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1 
    return decimal


def decodeList(binaryList):
    one_bit_counter = 0
    zero_bit_counter = 0
    global gamma_rate
    global epsilon_rate
    for elem in binaryList:
        if elem == "1":
            one_bit_counter += 1
        elif elem == "0":
            zero_bit_counter += 1

    if one_bit_counter > zero_bit_counter:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

    
decodeList(one_list)
decodeList(two_list)
decodeList(three_list)
decodeList(four_list)
decodeList(five_list)
decodeList(six_list)
decodeList(seven_list)
decodeList(eight_list)
decodeList(nine_list)
decodeList(ten_list)
decodeList(eleven_list)
decodeList(twelve_list)



gamma_rate = int(gamma_rate)
epsilon_rate = int(epsilon_rate)

gamma_rate = binaryToDecimal(gamma_rate)
epsilon_rate = binaryToDecimal(epsilon_rate)

print("Gamma:   ", gamma_rate)
print("Epsilon: ", epsilon_rate)

print(gamma_rate * epsilon_rate)



    