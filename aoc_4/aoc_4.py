
def read_input():
    with open("aoc_4/aoc_4_values.txt", "r") as f:
        data = f.read().split("\n")
        #print(data)
    return data

def part1(data):
    #Aquire all numbers for our Bingo sequence and remove it from data
    bingo_numbers = data[0]
    bingo_numbers.split(',') 
    #print("Our Bingo sequence:", bingo_numbers, "\n")
    data.remove(data[0])

    #Structure each bingo row correctly 
    bingo_rows = []
    bingo_bricks = []
    row_counter = 0
    for elem in data:
        if(elem != ''):
            bingo_rows.append(elem.split(' '))
        for row in bingo_rows:
            for number in row:
                if(number == ''):
                    row.remove(number)
    #print("Our Bingo rows:", bingo_rows)

    #Combine rows into bricks
    for row in bingo_rows:
        if(row_counter % 5 == 0):
            if(row_counter != 0):
                print(row_counter)
                bingo_bricks.append(temp_list)
            temp_list = []
        temp_list.append(row)
        row_counter += 1
        if(row_counter == 500):
            bingo_bricks.append(temp_list)

    #Play Bingo
    for number in bingo_numbers:
        current_brick = 0
        for brick in bingo_bricks:
            current_row = 0
            for row in brick:
                current_val = 0
                for value in row:
                    if(value == str(number)):
                        bingo_bricks[current_brick][current_row][current_val] = "x"
                    current_val += 1
                current_row += 1
            current_brick += 1

        #Check if a brick has won
        for brick in range(0, len(bingo_bricks)): #current_brick
            #Check if any row is filled
            for row in range(0, 5):
                #print(brick, row)
                #print(bingo_bricks[brick][row])
                if(bingo_bricks[brick][row].count("x") == 5):
                    print("BINGO! Save number drawn and brick for result")
            #Check if any column is filled
            #WIP

    #print(bingo_bricks)
    return



if __name__ == "__main__":
    data = read_input()
    part1(data)