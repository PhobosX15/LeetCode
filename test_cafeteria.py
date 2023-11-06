import unittest
from Cafeteria import getMaxAdditionalDiners

class TestCafeteria(unittest.TestCase):
    def test_getMaxAdditionalDiners(self):
        self.assertEqual(getMaxAdditionalDiners(15, 2, 3, [11, 6, 14]), 1)
        self.assertEqual(getMaxAdditionalDiners(10, 1, 2, [2, 6]), 3)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()