def read_txt_file(filename):
    pairs = []
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        for i in range(n):
            pair = list(map(int, file.readline().strip().split()))
            pairs.append(pair)
    return pairs


def possible_combinations_pairs(pairs):
    tribes = [set(pairs[0])]
    counter = 0
    union = []

    for pair in pairs[1:]:
        for tribe in tribes:
            if any(member in tribe for member in pair):
                tribe.update(pair)
                break
        else:
            tribes.append(set(pair))

    tribes_amount = len(tribes)

    for first_tribe in range(tribes_amount):
        for second_tribe in range(first_tribe + 1, tribes_amount):
            for first_person in tribes[first_tribe]:
                for second_person in tribes[second_tribe]:
                    if (first_person % 2 == 0 and second_person % 2 == 1) or (
                        first_person % 2 == 1 and second_person % 2 == 0
                    ):
                        counter += 1
                        union.append(f"{first_person}/{second_person}")

    return counter, union


def generate_output(filename, result, union):
    with open(filename, "w") as file:
        file.write(f"{result} (Possible pairs - {', '.join(union)})")


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    pairs = read_txt_file(input_file)
    result, union = possible_combinations_pairs(pairs)
    generate_output(output_file, result, union)
