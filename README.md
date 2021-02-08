# Congratulation!
第3回 Sekappyプログラミングチャレンジにて優秀賞をいただきました！

[マジック×プログラム 『冬のSekappyプログラミングチャレンジ』結果発表](https://sekappy.com/blog/2448)
# Magic: The Gathering company simulator!
デッキの一番上からカードをn枚めくり、条件に合うカードを手札に加えたり戦場に出したりする呪文(ex:《集合した中隊》・《上流階級のゴブリン、マクサス》など)による、当たりができる確率を計算する。
## Usage
### n枚めくり計算機の実行
```Bash
python main.py
```
### 入力例
```Bash
デッキの枚数:60
当たりの枚数:26
めくる枚数:6
選べる上限枚数:2

当たりが0枚めくれる確率：2.69%
当たりが1枚めくれる確率：14.45%
当たりが2枚以上めくれる確率：82.86%
当たりの期待値：1.80
```

## UnitTest
### テスト内容
* test_mathUtil.py - mathUtil.pyの単体テスト
* test_companySimulator - companySimulator.pyの単体テスト

### 例
```Bash
python -m unittest test_**.py
```
OR
```Bash
pytest 
```