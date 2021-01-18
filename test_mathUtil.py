import unittest
from mathUtil import calcPermutation, calcCombination
from error import PermutationError, CombinationError

class MathUtilTest(unittest.TestCase):
    def setUp(self):
        """
        setup function
        """
        pass

    def tearDown(self):
        """
        tearDown function
        """
        pass

    def test_permutation_success(self):
        self.assertEqual(calcPermutation(3, 2), 6)

    def test_permutation_pos_pos(self):
        with self.assertRaises(PermutationError):
            calcPermutation(2, 3)
    
    def test_permutation_neg_neg(self):
        with self.assertRaises(PermutationError):
            calcPermutation(-2, -3)
    
    def test_permutation_pos_neg(self):
        with self.assertRaises(PermutationError):
            calcPermutation(2, -3)

    def test_permutation_neg_pos(self):
        with self.assertRaises(PermutationError):
            calcPermutation(-2, 3)

    def test_combination_success(self):
        self.assertEqual(calcCombination(3, 2), 3)

    def test_combination_pos_pos(self):
        with self.assertRaises(CombinationError):
            calcCombination(2, 3)

    def test_combination_neg_neg(self):
        with self.assertRaises(CombinationError):
            calcCombination(-2, -3)

    def test_combination_pos_neg(self):
        with self.assertRaises(CombinationError):
            calcCombination(2, -3)

    def test_combination_neg_pos(self):
        with self.assertRaises(CombinationError):
            calcCombination(-2, 3)