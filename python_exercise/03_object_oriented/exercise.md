# 第3回 演習問題

クラス・関数の定義と使い方

## 練習課題

> - [ex3.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/03_object_oriented/ex3.py)
> - [ex4_blank.py](https://raw.githubusercontent.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/master/python_exercise/03_object_oriented/ex3_blank.py)

     
途中，`npy`形式ファイルが出てきます．`npy`形式とは，データ列をバイナリ化して保存したファイル形式で，他の形式と比べて読み込みや書き込みが若干高速です．
深層学習の分野では，一般にデータをバイナリ化して保存します．

## 演習課題

> - [Problem2.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/Problem2.py)

演習問題では，音声を読み込んで，実際に音声処理をやってみましょう！
ここでは，**バイナリマスキングによる音源分離**を行います．

### 1. フレーム処理

フレーム処理は基本的な音声処理手順の１つです．
音声を短い時間区間(=**フレーム**)に分割して，フレームごとに音声に処理を加えます．

<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/framing.png" width="450px">  

### 2. ウィンドウィング (窓関数処理) とオーバーラップ

処理した音声を，もとの連続音声に戻す際に，フレーム間のつなぎ目が不連続になることがあります．
このフレーム間の不連続性を緩和するために，**ウィンドウィング**と**オーバーラップ**を行います．
図はウィンドウィングとオーバーラップの例です．各フレームに両端が滑らかに減衰するハミング窓を書けたあと，処理を加えます．
処理されたフレームは，半分ずつずらして加算(=ハーフオーバーラップ)して連続音声を復元します．

<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/processing.png" width="580px">  

### 3. 周波数マスキング

さて，フレーム分割した音声にはどのような処理を加えるのでしょうか？
一つの例として，音声を周波数領域に変換し，いらない周波数成分を取り除くフィルタ処理をよく行います．

下は**周波数マスキング**を使ったフィルタ処理の例です．
まず入力のあるフレーム波形をFFTして複素数周波数スペクトルを算出します．
この複素数周波数スペクトルに対して，各周波数で 0 または 1 の値を設定した**周波数マスク**を用意します．
複素数周波数スペクトルと周波数マスクを互いに掛け合わせて不要な成分をマスキングします．
マスキング後の複素周波数スペクトルをIFFTすることで，処理後のフレーム波形を得ることができます．

<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/masking.png" width="670px">  

