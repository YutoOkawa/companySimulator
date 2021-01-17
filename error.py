class PermutationError(Exception):
    """
    順列の計算が失敗した時に投げるエラー
    """

    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "順列の計算に失敗しました．" + self.msg

class CombinationError(Exception):
    """
    組み合わせの計算が失敗した時に投げるエラー
    """

    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "組み合わせの計算に失敗しました．" + self.msg

class ProbabilityError(Exception):
    """
    確率の計算が失敗した時に投げるエラー
    """

    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return "確率の計算に失敗しました．" + self.msg

class ConstructorError(Exception):
    """
    コンストラクターの条件が合わなかった時に投げるエラー
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "入力値が不正です．" + self.msg

class CompanySimulatorError(Exception):
    """
    CompanySimulatorクラスのメソッド実行が失敗した時に投げるエラー
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "CompanySimulatorのメソッド実行が失敗しました．"