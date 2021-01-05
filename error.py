class PermutationError(Exception):
    """
    順列の計算が失敗した時に投げるエラー
    """

    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "順列の計算に失敗しました．" + self.msg

class CombinationError(PermutationError):
    """
    組み合わせの計算が失敗した時に投げるエラー
    """

    def __init__(self, msg):
        super().__init__(msg)
    
    def __str__(self):
        return "組み合わせの計算に失敗しました．" + self.msg

class ProbabilityError(CombinationError):
    """
    確率の計算が失敗した時に投げるエラー
    """

    def __init__(self, msg):
        super().__init__(msg)
    
    def __str__(self):
        return "確率の計算に失敗しました．" + self.msg