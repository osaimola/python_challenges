from challenges import *
import unittest


class TestBlock(unittest.TestCase):

    def test_block(self):
        self.assertEqual(block([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
        ]), 2, "should be 2")

        self.assertEqual(block([
        [1, 1, 1, 1],
        [2, 1, 1, 2],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        ]), 4, "should be 4")

if __name__ == '__main__':
    unittest.main()