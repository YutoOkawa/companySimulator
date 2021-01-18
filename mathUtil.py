from error import PermutationError, CombinationError
from decimal import Decimal, ROUND_HALF_UP
import math

def calcPermutation(n, r):
    """
    順列(nPr)を計算する

    n<0, r<0, n<rの場合にPermutationErrorが発生する．

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
    try:
        permutation = math.factorial(n) // math.factorial(n - r)
    except ValueError:
        raise PermutationError("factorial")
    
    if permutation == 0:
        raise PermutationError("Zero Case")
    return permutation

def calcCombination(n, r):
    """
    組み合わせ(nCr)を計算する

    n<0, r<0, n<rの場合にCombinationErrorが発生する．

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
    try:
        combination = calcPermutation(n, r) // math.factorial(r)
    except PermutationError:
        raise CombinationError("Permutation")
    except ValueError:
        raise CombinationError("factorial")
    return combination

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