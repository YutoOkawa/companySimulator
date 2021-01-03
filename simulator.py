import math
from decimal import Decimal, ROUND_HALF_UP

def inputNumber(prompt):
    """
    数字の入力を促し、その数字を返す

    Parameters
    ----------
    prompt : str
        入力時に出力するprompt

    Returns
    -------
    number : int
        入力された数字
    """
    while True:
        print(prompt, end="")
        try:
            number = int(input())
        except ValueError as err:
            print("Error: ", end="")
            print(err)
            print("Retry input number.")
            continue
        break
    return number

def calcPermutation(n, r):
    """
    順列(nPr)を計算する

    Parameters
    ----------
    n : int
        順列対象物の総数
    r : int
        順列の数

    Returns
    -------
    permutation : int
        nPrの計算結果
    """
    permutation = math.factorial(n) // math.factorial(n - r)
    return permutation

def calcCombination(n, r):
    """
    組み合わせ(nCr)を計算する

    Parameters
    ----------
    n : int
        組み合わせ対象物の総数
    r : int
        組み合わせの数

    Returns
    -------
    combination : int
        nCrの計算結果
    """
    combination = calcPermutation(n, r) // math.factorial(r)
    return combination

def calcProbability(open_number, hit_number, nohit_number, hit_count, denominator):
    """
    今回求める確率を計算する
    probability = {open}_C_{i} * ({hit}_P_{i} * {nohit}_P_{open - i} / {deck}_P_{open})

    Parameters
    ----------
    open_number : int
        めくるカードの枚数
    hit_number : int
        当たりカードの枚数
    nohit_number : int
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
    
    combination = calcCombination(open_number, hit_count)
    hit_permutation = calcPermutation(hit_number, hit_count)
    nohit_permutation = calcPermutation(nohit_number, open_number - hit_count)
    probability = combination * hit_permutation * nohit_permutation / denominator
    return probability

def roundNumber(number, round_digits):
    """
    四捨五入した値を返す

    Parameters
    ----------
    number : int
        四捨五入対象の数字
    round_digits : str
        四捨五入する桁数の指定

    Returns
    -------
    round_number : int
        四捨五入後の数字
    """
    decimal_object = Decimal(str(number))
    round_number = decimal_object.quantize(Decimal(round_digits), rounding=ROUND_HALF_UP)
    return float(round_number)

def main():
    print("Welcome to Company Simulator!")

    # 1.必要な情報の入力
    deck_number = inputNumber("デッキの枚数:")
    hit_number = inputNumber("当たりの枚数:")
    open_number = inputNumber("めくる枚数:")
    upper_number = inputNumber("選べる上限枚数:")
    # no hitの計算
    nohit_number = deck_number - hit_number

    # 2.確率の計算
    probability_list = []
    upper_probability = 1
    # 分母の計算
    denominator = calcPermutation(deck_number, open_number)
    for hit_count in range(upper_number):
        probability = calcProbability(open_number, hit_number, nohit_number, hit_count, denominator)
        # probability_upper = 1 - Σprobability_i
        upper_probability -= probability
        probability_list.append(roundNumber(probability, '0.0001'))
    probability_list.append(roundNumber(upper_probability, '0.0001'))
    
    print("--------------確率計算結果--------------")

    # 3.当選確率の表示と期待値の計算
    expectation = 0
    for index, probability in enumerate(probability_list):
        expectation += index * probability
        if index != upper_number:
            print("当たりが{}枚めくれる確率：{:.2f}%".format(index, probability*100))
        else :
            print("当たりが{}枚以上めくれる確率：{:.2f}%".format(index, probability*100))
    print("当たりの期待値：{:.2f}".format(roundNumber(expectation, '0.01')))

if __name__ == "__main__":
    main()