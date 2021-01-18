from error import PermutationError, CombinationError, ProbabilityError, ArgumentError, CompanySimulatorError
from mathUtil import calcPermutation, calcCombination, roundNumber

class CompanySimulator:
    """
    確率の計算を行うクラス
    """

    def __init__(self):
        pass

    def checkArgument(self, deck, hit, look, upper):
        """
        deck>hit, deck>look, deck>upper, look>upperであるかをチェックする
        不正値であれば、ArgumentErrorが発生する

        Parameters
        ----------
        deck : int
            デッキの枚数
        hit : int
            当たりの枚数
        look : int
            めくる枚数
        upper : int
            選べる上限枚数
        """
        # deck < hit の場合などはエラー
        if deck < 0 and hit < 0 and look < 0 and upper < 0:
            raise ArgumentError("negative number.")
        elif deck < hit:
            raise ArgumentError("deck < hit")
        elif deck < look:
            raise ArgumentError("deck < look")
        elif deck < upper:
            raise ArgumentError("deck < upper")
        elif look < upper:
            raise ArgumentError("look < upper")

    def calcProbability(self, look, hit, nohit, hit_count, denominator):
        """
        hit_count枚のあたりがめくれる確率を計算する
        probability = {open}_C_{i} * ({hit}_P_{i} * {nohit}_P_{open - i} / {deck}_P_{open})

        Parameters
        ----------
        look : int
            めくるカードの枚数
        hit : int
            当たりカードの枚数
        nohit : int
            当たりじゃないカードの枚数
        hit_count : int
            当選する枚数
        denominator : int
            計算する確率の分母

        Returns
        -------
        probability : float
            確率の計算結果
        """

        try:
            combination = calcCombination(look, hit_count)
            hit_permutation = calcPermutation(hit, hit_count)
            nohit_permutation = calcPermutation(nohit, look - hit_count)
            probability = combination * hit_permutation * nohit_permutation / denominator
        except PermutationError:
            raise ProbabilityError("Permutation")
        except CombinationError:
            raise ProbabilityError("Combination")
        return probability

    def calcExpectation(self, probability_list):
        """
        当たりの期待値を計算する

        Parameters
        ----------
        probability_list : list(float)
            確率のリスト

        Returns
        -------
        expectation : float
            期待値
        """
        expectation = 0
        try:
            for index, probability in enumerate(probability_list):
                expectation += index * probability
        except TypeError:
            raise CompanySimulatorError("期待値の計算に失敗しました．")
        expectation = roundNumber(expectation, '0.01')
        return expectation

    def start(self, deck, hit, look, upper):
        """
        probability = {open}_C_{i} * ({hit}_P_{i} * {nohit}_P_{open - i} / {deck}_P_{open})

        Parameters
        ----------
        deck : int
            デッキの枚数
        hit : int
            当たりの枚数
        look : int
            めくる枚数
        upper : int
            選べる上限枚数

        Returns
        -------
        probability_list : list(float)
            確率の計算結果
        """

        try:
            self.checkArgument(deck, hit, look, upper)
        except ArgumentError:
            raise CompanySimulatorError("入力が不正値です．")

        # 複数回計算する値の計算
        nohit = deck - hit
        try:
            denominator = calcPermutation(deck, look)
        except PermutationError:
            raise CompanySimulatorError("分母の計算に失敗しました．")

        probability_list = []
        upper_probability = 1
        for hit_count in range(upper):
            try:
                probability = self.calcProbability(look, hit, nohit, hit_count, denominator)
            except ProbabilityError:
                raise CompanySimulatorError("確率の計算に失敗しました．")
            upper_probability = upper_probability - probability
            probability_list.append(roundNumber(probability, '0.0001'))

        probability_list.append(roundNumber(upper_probability, '0.0001'))
        return probability_list