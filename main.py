from companyProbability import CompanyProbability
from error import ConstructorError, ProbabilityError

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
            print("Error:", err)
            print("Retry input number.")
            continue
        break
    return number

def main():
    print("Welcome to Company Simulator!")
    company = CompanyProbability()

    while True:
        # 1.必要な情報の入力
        deck = inputNumber("デッキの枚数:")
        hit = inputNumber("当たりの枚数:")
        look = inputNumber("めくる枚数:")
        upper = inputNumber("選べる上限枚数:")

        # companyProbabilityクラスで確率の計算
        try:
            probability_list = company.start(deck, hit, look, upper)
        except ProbabilityError as error:
            print(error, "再度入力してください．")
            continue

        # companyProbabilityクラスで期待値の計算
        expectation = company.calcExpectation(probability_list)

        # 確率計算結果の表示
        for index, probability in enumerate(probability_list):
            if index != upper:
                print("当たりが{}枚めくれる確率：{:.2f}%".format(index, probability*100))
            else:
                print("当たりが{}枚以上めくれる確率：{:.2f}%".format(index, probability*100))
        print("当たりの期待値：{:.2f}".format(expectation))

if __name__ == "__main__":
    main()