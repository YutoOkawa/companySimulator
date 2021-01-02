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

def main():
    print("Welcome to Company Simulator!")
    deck = inputNumber("デッキの枚数:")
    hit = inputNumber("当たりの枚数:")
    open = inputNumber("めくる枚数:")
    upper = inputNumber("選べる上限枚数:")

if __name__ == "__main__":
    main()