# 第3回 演習問題

クラス・関数の定義と使い方について学習しましょう．

## 練習課題

> - [ex3.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/03_object_oriented/ex3.py)
> - [ex3_blank.py](https://raw.githubusercontent.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/master/python_exercise/03_object_oriented/ex3_blank.py)

## 演習課題

> - [Problem3.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/03_object_oriented/Problem3.py)

演習問題では，画像の雑音除去の雑音除去について勉強しましょう！
下の説明に目を通しつつ，課題に取り組みましょう．

---
## 画像の雑音除去

高感度なセンサで写真や映像を撮影するとき，光量が少ないとどうしてもザラザラとしたノイズが発生します．
これは画像処理分野では「ガウス性白色ノイズ」と呼ばれるもので，バックエンドのアプリケーション(例えば画像認識など)に悪い影響を与えてしまいます．
そのため，一般にはアプリケーションで画像を使用する前に，雑音除去技術を使用してガウス性白色ノイズを除去します．
ここでは，雑音除去技術の一つである「**スパース性に基づく画像復元**」を学んでいきましょう．

### 1. DCT基底による画像表現

みなさんが学習した**フーリエ級数展開**にあるように，あらゆる信号はsin波とcos波の組み合わせ(正確には線形和)で表現できます．下の式にあるように，sin波とcos波，それぞれで基本周波数 `ω` が与えられ，その整数倍の周波数 `kω` をもつ波の足し合わせで表現されます．

<img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;\large&space;x_n&space;=&space;\frac{a_0}{2}&plus;\sum^{\infty}_{k=1}&space;a_k&space;\sin&space;(k\omega)&space;&plus;&space;b_k&space;\cos&space;(k\omega)" title="\large x_n = \frac{a_0}{2}+\sum^{\infty}_{k=1} a_k \sin (k\omega) + b_k \cos (k\omega)" />



このフーリエ級数展開による信号の表現は，もちろん画像でも当てはまります．
ある画像の**バッチ**(画像の一部を方形で切り出したもの)を抽出すると，そのバッチは必ず２次元のsin波とcos波の線形和で表現できます．
２次元のsin波とは，横方向(x方向)と横方向(y方向)のそれぞれでsin波の値をもつ２次元データのことで，波面のような構造を持ちます．

さらに興味深いことに，sin波とcos波は互いに位相が90°ずれたものなので，位相をうまく調整すると，実際には２次元cos波のみの線形和で画像を表現することができます．
ただし，正確に画像を表現するにはcos波を無限に用意する必要がありますが(厳密には，周波数 `kω` において k→∞ まで考えないといけないということ)，
これは決して現実的ではありません．
コンピュータで画像を表現するためには，無限のcos波を用いることは避け，多少精度は劣化しても有限個のcos波で表現したいです．

そこで，
<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/masking.png" width="670px">  
