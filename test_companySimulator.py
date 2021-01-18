import unittest
from error import ArgumentError, ProbabilityError, CompanySimulatorError
from companySimulator import CompanySimulator

class CompanySimulatorTest(unittest.TestCase):
    def setUp(self):
        """
        setup function
        """
        self.simulator = CompanySimulator()

    def tearDown(self):
        """
        tearDown function
        """
        pass

    def test_checkArgument_deck_neg(self):
        with self.assertRaises(ArgumentError):
            self.simulator.checkArgument(-60, 26, 6, 2)

    def test_checkArgument_hit_neg(self):
        with self.assertRaises(ArgumentError):
            self.simulator.checkArgument(60, -26, 6, 2)

    def test_checkArgument_look_neg(self):
        with self.assertRaises(ArgumentError):
            self.simulator.checkArgument(60, 26, -6, 2)

    def test_checkArgument_upper_neg(self):
        with self.assertRaises(ArgumentError):
            self.simulator.checkArgument(60, 26, 6, -2)

    def test_checkArgument_deck_hit(self):
        with self.assertRaises(ArgumentError):
            self.simulator.checkArgument(60, 260, 6, 2)

    def test_checkArgument_deck_look(self):
        with self.assertRaises(ArgumentError):
            self.simulator.checkArgument(60, 26, 600, 2)

    def test_checkArgument_deck_upper(self):
        with self.assertRaises(ArgumentError):
            self.simulator.checkArgument(60, 26, 6, 200)

    def test_checkArgument_look_upper(self):
        with self.assertRaises(ArgumentError):
            self.simulator.checkArgument(60, 26, 6, 20)

    def test_calcProbability_success(self):
        self.assertEqual(self.simulator.calcProbability(6, 26, 34, 0, 36045979200), 0.026863769593475213)

    def test_calcProbability_look_count(self):
        with self.assertRaises(ProbabilityError, msg="Combination"):
            self.simulator.calcProbability(6, 26, 34, 20, 36045979200)

    def test_calcProbability_hit_count(self):
        with self.assertRaises(ProbabilityError, msg="Permutation"):
            self.simulator.calcProbability(6, 26, 34, 200, 36045979200)

    def test_calcProbability_no_lookcount(self):
        with self.assertRaises(ProbabilityError, msg="Permutation"):
            self.simulator.calcProbability(60, 26, 34, 2, 36045979200)

    def test_calcProbability_denominator_zero(self):
        with self.assertRaises(ProbabilityError, msg="denominator"):
            self.simulator.calcProbability(6, 26, 34, 2, 0)

    def test_calcExpectation_success(self):
        self.assertEqual(self.simulator.calcExpectation([0.0269, 0.1445, 0.8286]), 1.8)

    def test_calcExpectation_error(self):
        with self.assertRaises(CompanySimulatorError, msg="期待値の計算に失敗しました．"):
            self.simulator.calcExpectation(0.1)