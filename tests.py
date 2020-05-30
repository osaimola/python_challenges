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

class TestPersistence(unittest.TestCase):
    def test_additive_persistence(self):
        self.assertEqual(additive_persistence(1679583), 3, "should be 3")

        self.assertEqual(additive_persistence(123456), 2, "should be 2")


    def test_multiplicative_persistence(self):
        self.assertEqual(multiplicative_persistence(77), 4, "should be 4")

        self.assertEqual(multiplicative_persistence(123456), 2, "should be 2")

        self.assertEqual(multiplicative_persistence(4), 0, "should be 0")


class TestPilish(unittest.TestCase):
    def test_pilish(self):
        self.assertEquals(pilish_string("FORALOOP"), "FOR A LOOP")
        self.assertEquals(pilish_string("CANIMAKEAGUESS"), "CAN I MAKE A GUESS")
        self.assertEquals(pilish_string("CANIMAKEAGUESSNOW"), "CAN I MAKE A GUESS NOWWWWWWW")
        self.assertEquals(pilish_string("X"), "XXX")
        self.assertEquals(pilish_string("ARANDOMSEQUENCEOFLETTERS"), "ARA N DOMS E QUENC EOFLETTER SS")
        self.assertEquals(pilish_string(""), "")
        self.assertEquals(pilish_string("33314444155555999999999226666665555533355555888888889999999997777777999999999"), "333 1 4444 1 55555 999999999 22 666666 55555 333 55555 88888888 999999999 7777777 999999999")
        self.assertEquals(pilish_string("###*@"), "### * @@@@")
        self.assertEquals(pilish_string(".........."), "... . .... . .....")
        # Below, quoting Mike Keith
        self.assertEquals(pilish_string("NowIfallAtiredsuburbianInliquidunderthetreesDriftingalongsideforestssimm"), "Now I fall A tired suburbian In liquid under the trees Drifting alongside forests simmmmmmm")
        # Below, quoting Sir James Hopwood Jeans
        self.assertEquals(pilish_string("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYLECTURESINVOLVINGQUANTUMMECHANICSANDALLTHESECRETSOFTHEUNIVERSE"), "HOW I NEED A DRINK ALCOHOLIC IN NATURE AFTER THE HEAVY LECTURES INVOLVING QUANTUM MECHANICS")
        self.assertEquals(pilish_string("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYCODING"), "HOW I NEED A DRINK ALCOHOLIC IN NATURE AFTER THE HEAVY CODINGGG")

if __name__ == '__main__':
    unittest.main()