# 第2回 演習問題

データの読み込み・書き込み関数をスクラッチして，使い方をマスターしよう！

## 練習課題

> - [ex2.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/ex2.py)
> - [ex2_blank.py](https://raw.githubusercontent.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/master/python_exercise/02_IO/ex2_blank.py)

練習課題では以下のデータの読み込み・書き込みを行います．また，画像の表示や音声波形の表示・スペクトログラムの表示を行います．

   - iris.csv  
     ユリの特徴を数値化したデータ列です．
   - lena.tiff　　(tiff：非圧縮画像形式)  
     レナ(女性)の画像です．   
   - sample.wav　　(wav：非圧縮音声形式)  
     男性の音声です．
     
途中，`npy`形式ファイルが出てきます．`npy`形式とは，データ列をバイナリ化して保存したファイル形式で，他の形式と比べて読み込みや書き込みが若干高速です．
深層学習の分野では，一般にデータをバイナリ化して保存します．

## 演習課題

> - [Problem2.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/Problem2.py)

演習問題では，音声を読み込んで，実際に音声処理をやってみましょう！
ここでは，**バイナリマスキングによる音源分離**を行います．

### 1. フレーム処理

フレーム処理は基本的な音声処理手順の１つです．
音声を短い時間区間(=**フレーム**)に分割して，フレームごとに音声に処理を加えます．
フレームの長さ(サンプル数)は，一般的に\underline{20～50ms}となるように設定します．

<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/framing.png" width="450px">  

### 2. ウィンドウィング (窓関数処理) とオーバーラップ

フレームごとに分割して処理された信号は，再び時系列につなぎ合わせることで音声信号として復元することが出来ます．
ただし，処理した信号をそのまま並べただけでは，フレーム間のつなぎ目で音声信号が不連続になる可能性があります．
信号が不連続になると，復元音声は耳障りで不快なものになります．
このフレーム間の不連続性を緩和するために，**ウィンドウィング**と**オーバーラップ**を行います．
図はウィンドウィングとオーバーラップの例です．各フレームに両端が滑らかに減衰するハミング窓を書けたあと，処理を加えます．
処理されたフレームは，半分ずつずらして加算(=ハーフオーバーラップ)して連続音声を復元します．

窓関数は山なりな形状をもつ関数で，フレーム分割された信号に掛け合わせることで両端をなめらかに減衰させることができます．
窓関数には形状が異なる数種類のものが存在し，音声信号処理においては一般にハミング窓(Hamming Window)やハニング窓(Hanning Winsow)が用いられます．

ハミング窓：  
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Aw%28n%29+%3D+0.54+%2B+0.46+%5Ccos+%5Cleft%28+%5Cfrac%7Bn%7D%7BN%7D%5Cpi+%5Cright%29+%5Cquad+%28-N+%5Cleq+n+%5Cleq+N%29%0A%5Cend%7Balign%2A%7D%0A" 
alt="\begin{align*}
w(n) = 0.54 + 0.46 \cos \left( \frac{n}{N}\pi \right) \quad (-N \leq n \leq N)
\end{align*}
">

ハニング窓：  
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Aw%28n%29+%3D+0.5+%2B+0.5+%5Ccos+%5Cleft%28+%5Cfrac%7Bn%7D%7BN%7D%5Cpi+%5Cright%29+%5Cquad+%28-N+%5Cleq+n+%5Cleq+N%29%0A%5Cend%7Balign%2A%7D%0A" 
alt="\begin{align*}
w(n) = 0.5 + 0.5 \cos \left( \frac{n}{N}\pi \right) \quad (-N \leq n \leq N)
\end{align*}
">

オーバーラップさせる割合はフレーム長の半分でなくても結構です．
3/4オーバーラップや7/8オーバーラップなど，オーバーラップの割合を増やしたやり方も存在し，音声信号処理では一般に7/8オーバーラップが最も音質がよいとされています．
ここで，3/4オーバーラップではフレームのシフト幅(=隣接フレームとの距離)はフレーム長の1/4になり，7/8オーバーラップではフレームのシフト幅はフレーム長の1/8になります．
すなわち\textbf{オーバーラップの割合が増加するほど，フレームのシフト幅は減少しますので注意です}．


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

### 4. バイナリマスキングによる音源分離

それでは音源分離の中で最も単純な手法である「バイナリマスクを用いた音源分離」の原理を学習しましょう．
今，図のように話者が２名いてマイクロホンが２つある状況を考えます．
Aさんに着目すると，Aさんの音声はマイクロホン１, マイクロホン２のどちらにも入力されます．
ただしAさんとマイクロホンとの距離は異なります．
ですので，近くにあるマイクロホン１に入力される音声のパワーは大きくなり，遠くにあるマイクロホン２に入力される音声のパワーは小さくなります．
一方でBさんの音声はその逆に，遠くにあるマイクロホン１に入力される音声のパワーは小さくなり，遠くにあるマイクロホン２に入力される音声のパワーは大きくなります．

この性質を利用して音源分離を行います．
マイクロホン
<img src=
"https://render.githubusercontent.com/render/math?math=%5Ctextstyle+i+%5C+%5C+%28i%3D1%2C2%29%0A" 
alt="i \ \ (i=1,2)">
に入力されるある時刻
<img src=
"https://render.githubusercontent.com/render/math?math=%5Ctextstyle+t%0A" 
alt="t">
のある周波数
<img src=
"https://render.githubusercontent.com/render/math?math=%5Ctextstyle+t%0A" 
alt="\omega">
における振幅スペクトルを
<img src=
"https://render.githubusercontent.com/render/math?math=%5Ctextstyle+X%5E%7B%28i%29%7D%28t%2C%5Comega%29%0A" 
alt="X^{(i)}(t,\omega)
">
と表現します．
WDOを仮定すると，$X^{(i)}(t,\omega)$はAさんあるいはBさんの音声の成分ということになります．
