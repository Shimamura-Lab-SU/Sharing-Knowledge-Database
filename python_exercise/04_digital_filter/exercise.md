# 第4回練習問題

## 練習課題1：ローパスフィルタ設計

以下のコードをスクラッチしてローパスフィルタを設計しましょう．
カットオフ周波数 : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Comega_c%0A" >
，フィルタ係数の数 : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+2N%2B1%0A" >
（フィルタ次数）の値は任意に設定してください．
また窓関数を１つ選択し，同じカットオフ周波数，同じフィルタ係数の数をもつローパスフィルタを設計してください．
これらのフィルタの周波数特性(振幅特性・位相特性)をプロットし，結果を比較してください．

- [TestLPF.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/04_digital_filter/TestLPF.py)

## 練習課題2：バンドパス・ハイパスフィルタ設計

以下のコードをスクラッチしてバンドパス・ハイパスフィルタを設計しましょう．
中心周波数 : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Comega_0%0A" >
，フィルタ係数の数 : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+2N%2B1%0A" >
（フィルタ次数）の値は任意に設定してください．
また，ハイパスフィルタを設計してください．

- [TestBPF.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/04_digital_filter/TestBPF.py)

## 練習課題3：フィルタリング

複数の異なる周波数成分を有する，正弦波からなる信号

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ax%28n%29+%3D+%5Csum_%7Bi%3D1%7D%5E%7BP%7D+A_i+%5Csin+%5Cleft%28+2%5Cpi+f_i+n+%5Cright%29+%5Cqquad+%28%5Cbecause+%5C%3B+P+%5Cgeq+2%29%0A%5Cend%7Balign%2A%7D%0A" >

を生成してください．
ここで，
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+A_i%2C%5C%2Cf_i%5C%3B+%5Cquad+%28i%3D1%2C2%2C%5Cdots%2CP%29%0A" >
は，それぞれ，各正弦波の振幅と，周波数を表しています．
ただし，周波数
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+f_1" >
については，フィルタの通過域内になるように設定してください．

次に，生成した正弦波信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%28n%29">
に対して，練習課題1で設計した窓関数なしのローパスフィルタを用いて，フィルタリングを行い，出力信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%28n%29">
を生成してください．
そして，FFTを用いてフィルタの入出力における周波数成分を調べ，
時間領域におけるフィルタリング結果と比較してください．

- [TestFiltering.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/04_digital_filter/TestFiltering.py)
