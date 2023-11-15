import unittest
from src.main import read_txt_file, possible_combinations_pairs


class TestWeddingTask(unittest.TestCase):
    def test_read_txt_file(self):
        test_input = "4\n1 2\n3 4\n5 6\n7 8"
        with open("test_input.txt", "w") as file:
            file.write(test_input)
        expected_output = [[1, 2], [3, 4], [5, 6], [7, 8]]
        result = read_txt_file("test_input.txt")

        self.assertEqual(result, expected_output)

    def test_calculate_marries_pairs(self):
        pairs_1 = [[1, 2], [2, 4], [3, 5]]
        result_1 = possible_combinations_pairs(pairs_1)
        self.assertEqual(result_1, 4)

        pairs_2 = [[1, 2], [2, 4], [1, 3], [3, 5], [8, 10]]
        result_2 = possible_combinations_pairs(pairs_2)
        self.assertEqual(result_2, 6)


if __name__ == '__main__':
    unittest.main()
