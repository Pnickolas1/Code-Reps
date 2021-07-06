import unittest
from scratch_file_1 import totalOccurrencesOfK


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(totalOccurrencesOfK([1, 2, 2, 2, 2], 2), 4, "Should be 4")

    def test_sum_tuple(self):
        self.assertEqual(totalOccurrencesOfK([1, 2, 2, 3, 3, 3, 3, 3], 3), 5, "Should be 5")

if __name__ == '__main__':
    unittest.main()