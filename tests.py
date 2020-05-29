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

    def test_additive_persistence(self):
        self.assertEqual(additive_persistence(1679583), 3, "should be 3")

        self.assertEqual(additive_persistence(123456), 2, "should be 2")


    def test_multiplicative_persistence(self):
        self.assertEqual(multiplicative_persistence(77), 4, "should be 4")

        self.assertEqual(multiplicative_persistence(123456), 2, "should be 2")

        self.assertEqual(multiplicative_persistence(4), 0, "should be 0")

if __name__ == '__main__':
    unittest.main()