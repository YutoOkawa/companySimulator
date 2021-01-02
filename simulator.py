import math

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

def main():
    print("Welcome to Company Simulator!")

    # 1.必要な情報の入力
    deck = inputNumber("デッキの枚数:")
    hit_number = inputNumber("当たりの枚数:")
    open_number = inputNumber("めくる枚数:")
    upper_number = inputNumber("選べる上限枚数:")

    # 2.確率の計算
    probability_list = []
    # 分母の計算
    denominator = calcPermutation(deck, open_number)
    # 0 to upper-1 の確率の計算
    # {open}_C_{i} * ({hit}_P_{i} * {deck - hit}_P_{open - i} / {deck}_P_{open})
    for hit_count in range(upper_number):
        combination = calcCombination(open_number, hit_count)
        hit_permutation = calcPermutation(hit_number, hit_count)
        nonhit_permutation = calcPermutation(deck - hit_number, open_number - hit_count)
        probability = combination * hit_permutation * nonhit_permutation / denominator
        probability_list.append(probability)

    print(probability_list)

if __name__ == "__main__":
    main()