bingo_numbers = []


def main():
    with open("aoc_4/aoc_4_values.txt", "r") as f:
        lines = [entry.strip for entry in f.read().split("\n")]
        first_line = lines[0]
        bingo_numbers = [int(entry) for entry in first_line.split(",")]
    print(bingo_numbers)










if __name__ == "__main__":
    main()