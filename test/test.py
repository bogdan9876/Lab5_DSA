import unittest
from src.main import possible_combinations_pairs


class TestFunctions(unittest.TestCase):

    def test_possible_combinations_pairs_with_three_tribes(self):
        pairs = [(1, 2), (2, 4), (3, 5)]
        result, union = possible_combinations_pairs(pairs)
        self.assertEqual(result, 4)

    def test_possible_combinations_pairs_with_five_tribes(self):
        pairs = [(1, 2), (2, 4), (1, 3), (3, 5), (8,10)]
        result, union = possible_combinations_pairs(pairs)
        self.assertEqual(result, 6)

    def test_possible_combinations_pairs_zero_tribes(self):
        pairs = []
        result, union = possible_combinations_pairs(pairs)
        self.assertEqual(result, 0)

    def test_possible_combinations_pairs_only_boys(self):
        pairs = [(2, 4), (6, 8), (10, 12)]
        result, union = possible_combinations_pairs(pairs)
        self.assertEqual(result, 0)

    def test_possible_combinations_pairs_only_girls(self):
        pairs = [(1, 3), (5, 7), (9, 11)]
        result, union = possible_combinations_pairs(pairs)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
