import networkx as nx


def read_txt_file(input_file):
    pairs = []
    with open(input_file, "r") as file:
        num_pairs = int(file.readline().strip())
        for i in range(num_pairs):
            pair = list(map(int, file.readline().strip().split()))
            pairs.append(pair)
    return pairs


def possible_combinations_pairs(pairs):
    tribe_graph = nx.Graph()
    for pair in pairs:
        if len(pair) == 2:
            tribe_member_1, tribe_member_2 = pair
            tribe_graph.add_edge(tribe_member_1, tribe_member_2)

    counter = 0
    union = []
    connected_tribes = list(nx.connected_components(tribe_graph))
    tribe_counter = 0
    for tribe in connected_tribes:
        males = {member for member in tribe if member % 2 == 1}
        females = {member for member in tribe if member % 2 == 0}
        for other_tribe in connected_tribes[:tribe_counter] + connected_tribes[tribe_counter + 1 :]:
            other_males = {member for member in other_tribe if member % 2 == 1}
            other_females = {member for member in other_tribe if member % 2 == 0}
            for male in males:
                for female in other_females:
                    if f"{male}/{female}" not in union:
                        counter += 1
                        union.append(f"{male}/{female}")
            for female in females:
                for male in other_males:
                    if f"{male}/{female}" not in union:
                        counter += 1
                        union.append(f"{male}/{female}")
        tribe_counter += 1

    return counter, union


def generate_output(output_file, counter, pair_union):
    with open(output_file, "w") as file:
        file.write(f"{counter} (Possible pairs - {', '.join(pair_union)})")


if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"
    pairs = read_txt_file(input_filename)
    counter, union = possible_combinations_pairs(pairs)
    generate_output(output_filename, counter, union)
