
import unittest

from objutils.checksums import nibbleSum, lrc, rotatedXOR
from objutils.checksums import COMPLEMENT_NONE, COMPLEMENT_ONES, COMPLEMENT_TWOS, ROTATE_LEFT, ROTATE_RIGHT


class TestNiblleSums(unittest.TestCase):

    def testNibbleSumCase1(self):
        self.assertEquals(nibbleSum(range(10)), 45)

    def testNibbleSumCase2(self):
        self.assertEquals(nibbleSum(range(100)), 222)

    # check that s.split fails when the separator is not a string
    #with self.assertRaises(TypeError):
    #    s.split(2)


class TestLRCs(unittest.TestCase):

    def testLRCCase1(self):
        self.assertEquals(lrc(range(10), 8, COMPLEMENT_NONE), 45)

    def testLRCCase2(self):
        self.assertEquals(lrc(range(100), 8, COMPLEMENT_NONE), 86)

    def testLRCCase3(self):
        self.assertEquals(lrc(range(10), 8, COMPLEMENT_ONES), 210)

    def testLRCCase4(self):
        self.assertEquals(lrc(range(100), 8, COMPLEMENT_ONES), 169)

    def testLRCCase5(self):
        self.assertEquals(lrc(range(10), 8, COMPLEMENT_TWOS), 211)

    def testLRCCase6(self):
        self.assertEquals(lrc(range(100), 8, COMPLEMENT_TWOS), 170)

    def testLRCCase7(self):
        self.assertEquals(lrc(range(10), 16, COMPLEMENT_NONE), 45)

    def testLRCCase8(self):
        self.assertEquals(lrc(range(100), 16, COMPLEMENT_NONE), 4950)

    def testLRCCase9(self):
        self.assertEquals(lrc(range(10), 16, COMPLEMENT_ONES), 65490)

    def testLRCCase10(self):
        self.assertEquals(lrc(range(100), 16, COMPLEMENT_ONES), 60585)

    def testLRCCase11(self):
        self.assertEquals(lrc(range(10), 16, COMPLEMENT_TWOS), 65491)

    def testLRCCase12(self):
        self.assertEquals(lrc(range(100), 16, COMPLEMENT_TWOS), 60586)

    def testLRCCase13(self):
        self.assertEquals(lrc(range(10), 32, COMPLEMENT_NONE), 45)

    def testLRCCase14(self):
        self.assertEquals(lrc(range(100), 32, COMPLEMENT_NONE), 4950)

    def testLRCCase15(self):
        self.assertEquals(lrc(range(10), 32, COMPLEMENT_ONES), 4294967250L)

    def testLRCCase16(self):
        self.assertEquals(lrc(range(100), 32, COMPLEMENT_ONES), 4294962345L)

    def testLRCCase17(self):
        self.assertEquals(lrc(range(10), 32, COMPLEMENT_TWOS), 4294967251L)

    def testLRCCase18(self):
        self.assertEquals(lrc(range(100), 32, COMPLEMENT_TWOS), 4294962346L)


class TestRXORs(unittest.TestCase):

    def testRXORCase1(self):
        self.assertEquals(rotatedXOR(range(10), 8, ROTATE_LEFT), 74)

    def testRXORCase2(self):
        self.assertEquals(rotatedXOR(range(100), 8, ROTATE_LEFT), 66)

    def testRXORCase3(self):
        self.assertEquals(rotatedXOR(range(10), 8, ROTATE_RIGHT), 186)

    def testRXORCase4(self):
        self.assertEquals(rotatedXOR(range(100), 8, ROTATE_RIGHT), 3)

    def testRXORCase5(self):
        self.assertEquals(rotatedXOR(range(10), 16, ROTATE_LEFT), 74)

    def testRXORCase6(self):
        self.assertEquals(rotatedXOR(range(100), 16, ROTATE_LEFT), 66)

    def testRXORCase7(self):
        self.assertEquals(rotatedXOR(range(10), 16, ROTATE_RIGHT), 186)

    def testRXORCase8(self):
        self.assertEquals(rotatedXOR(range(100), 16, ROTATE_RIGHT), 3)

    def testRXORCase9(self):
        self.assertEquals(rotatedXOR(range(10), 32, ROTATE_LEFT), 74)

    def testRXORCase10(self):
        self.assertEquals(rotatedXOR(range(100), 32, ROTATE_LEFT), 66)

    def testRXORCase11(self):
        self.assertEquals(rotatedXOR(range(10), 32, ROTATE_RIGHT), 186)

    def testRXORCase12(self):
        self.assertEquals(rotatedXOR(range(100), 32, ROTATE_RIGHT), 3)


if __name__ == '__main__':
    unittest.main()

