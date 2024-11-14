import unittest

from structures import *
class TestFunctions(unittest.TestCase):

    def test_findErrorNums(self):
        self.assertEqual(findErrorNums([1, 2, 2, 4]), [2, 3])
        self.assertEqual(findErrorNums([1, 1]), [1, 2])

    def test_countPrimeSetBits(self):
        self.assertEqual(countPrimeSetBits(6, 10), 4)
        self.assertEqual(countPrimeSetBits(10, 15), 5)

    def test_sumIndicesWithKSetBits(self):
        self.assertEqual(sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1), 13)
        self.assertEqual(sumIndicesWithKSetBits([4, 3, 2, 1], 2), 1)

    def test_isAlienSorted(self):
        self.assertTrue(isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
        self.assertFalse(isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))

    def test_minimizedMaximum(self):
        self.assertEqual(minimizedMaximum(6, [11, 6]), 3)
        self.assertEqual(minimizedMaximum(7, [15, 10, 10]), 5)

    def test_longestWord(self):
        self.assertEqual(longestWord(["w", "wo", "wor", "worl", "world"]), "world")
        self.assertEqual(longestWord(["a", "banana", "app", "appl", "apply", "apple"]), "apple")

    def test_twoEditWords(self):
        self.assertEqual(twoEditWords(["word", "note", "ants"], ["wood", "joke", "moat"]), ["word", "note"])
        self.assertEqual(twoEditWords(["yes"], ["not"]), [])

    def test_numRollsToTarget(self):
        self.assertEqual(numRollsToTarget(1, 6, 3), 1)
        self.assertEqual(numRollsToTarget(2, 6, 7), 6)

if __name__ == '__main__':
    unittest.main()
