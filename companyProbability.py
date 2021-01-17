from error import PermutationError, CombinationError, ProbabilityError, ConstructorError
from mathUtil import calcPermutation, calcCombination

class CompanyProbability:
    """
    確率の計算を行うクラス
    """

    def __init__(self):
        pass

    def checkConstructor(self, deck, hit, look, upper):
        """
        deck>hit, deck>look, deck>upper, look>upperであるかをチェックする
        """
        # TODO:コンストラクタの条件チェック
        # deck < hit の場合などはエラー
        if deck < hit:
            raise ConstructorError()
        elif deck < look:
            raise ConstructorError()
        elif deck < upper:
            raise ConstructorError()
        elif look < upper:
            raise ConstructorError()

    def calcProbability(self, deck, hit, look, upper):
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
            self.checkConstructor(deck, hit, look, upper)
        except ConstructorError:
            raise ProbabilityError("入力が不正値です．")

        nohit = deck - hit

        probability_list = []
        upper_probability = 1

        # 分母の計算
        try:
            denominator = calcPermutation(deck, look)
        except PermutationError:
            raise ProbabilityError("denominator")

        for hit_count in range(upper):
            # 確率の計算
            try:
                combination = calcCombination(look, hit_count)
                hit_permutation = calcPermutation(hit, hit_count)
                nohit_permutation = calcPermutation(nohit, look - hit_count)
                probability = combination * hit_permutation * nohit_permutation / denominator
            except PermutationError:
                raise ProbabilityError("Permutation")
            except CombinationError:
                raise ProbabilityError("Combination")

            probability_list.append(probability)
            upper_probability = upper_probability - probability

        probability_list.append(upper_probability)
        return probability_list
