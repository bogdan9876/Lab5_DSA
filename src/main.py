def read_txt_file(filename):
    pairs = []
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        for i in range(n):
            pair = list(map(int, file.readline().strip().split()))
            pairs.append(pair)
    return pairs


def possible_combinations_pairs(pairs):
    first_tribe = set()
    second_tribe = set()
    count = 0

    first_tribe.update(pairs[0])
    for pair in pairs[1:]:
        if any(member in first_tribe for member in pair):
            first_tribe.update(pair)
        else:
            second_tribe.update(pair)

    for first_person in first_tribe:
        for second_person in second_tribe:
            if (first_person % 2 == 0 and second_person % 2 == 1) or (
                first_person % 2 == 1 and second_person % 2 == 0
            ):
                count += 1

    return count


def generate_output(filename, result):
    with open(filename, "w") as file:
        file.write(str(result))


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    pairs = read_txt_file(input_file)
    result = possible_combinations_pairs(pairs)
    generate_output(output_file, result)
