# 部分空間分解 (工事中)

ここでは，信号解析手法の1つである部分空間分解について説明します．

## 信号処理の１課題

信号処理は


## 用語の定義

### 1. 信号の定義
まずは信号の性質について勉強しましょう．
ディジタル信号は，**確定信号**と**確率信号**の2種類に分類することができます．

- **確定信号**  
    過去のサンプルから，次のサンプルを予測することができる信号．音声の母音は周期信号となるため，確定信号である．  
    例：正弦波，音声の母音，画像のテクスチャ(布やビルなどの規則的な模様)

- **確率信号**  
    過去のサンプルから，次のサンプルを予測することができない信号．確率的にサンプル値が決定される信号のことを指す．  
    例：ガウス性白色信号，一様乱数，バブルノイズ(会話雑音)，音声の子音，画像のランダム模様(木に生えている葉っぱや砂地など)

音声処理や画像処理において，重要な成分の多くは確定信号で近似されます(音声の母音や画像の繰り返し成分)．
一方で不要な成分(=雑音)の多くは確率信号となります． 

<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/05_sub_space/signal.png" width="680px"> 

一般に確率信号は，ある**確率分布関数**(Probability Distribution Function : PDF)からランダムにサンプリングした信号列であると仮定できます．
例えばその確率分布関数が平均0の正規分布のとき，確率信号はガウス性白色雑音になります．

確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
が確率分布関数
<img src="https://render.githubusercontent.com/render/math?math=%5Ctextstyle+p%28x%29%0A">
に従うとしたとき，

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cdisplaystyle+%5Cint_%7B%5Cinfty%7D%5E%7B%5Cinfty%7D+p%28x%29+dx+%3D+1%0A">

が成り立ちます．
すなわち，あらゆる取りうる値の生起確率を足し合わせると，1になります．
これは，確率分布が連続分布でも離散分布でも成り立ちます．


### 2. 平均・分散・共分散
時刻
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n%0A">
の信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x_n">
における平均，分散，共分散は以下の通り計算されます．

#### 平均(期待値) ：    
確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
の平均(期待値)は，取りうる値とその生起確率の積で計算されます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cdisplaystyle+%5Cbar%7Bx_n%7D+%3D+E%5Bx_n%5D+%3D+%5Cint+x_n+p%28x_n%29+dx_n+%5Csimeq+%5Cfrac%7B1%7D%7BN%7D%5Csum%5E%7BN-1%7D_%7Bi%3D0%7D+x_%7Bn-i%7D">

#### 分散 ：  

確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
の分散は以下の式で計算されます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+E%5B%28x_n-%5Cbar%7Bx%7D%29%5E2%5D+%5Csimeq+%5Cfrac%7B1%7D%7BN%7D%5Csum%5E%7BN-1%7D_%7Bi%3D0%7D+%28x_n+-+%5Cbar%7Bx%7D%29%5E2%0A">

#### 共分散 ：

共分散とは，２つの信号の関係性を表す指標である．
確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
と
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%0A">
の共分散は以下の式で計算されます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+Cov%28x%2Cy%29+%3D+E%5B%28x-%5Cbar%7Bx%7D%29%28y-%5Cbar%7By%7D%29%5D%0A" >

ちなみに，共分散には以下の関係が成り立ちます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+Cov%28x_n%2C+y_n%29+%3D+E%5Bx_ny_n%5D+-+E%5Bx_n%5DE%5By_n%5D%0A">

## 無相関・独立

まず信号の無相関性・独立性について説明します．
２つの確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
と
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%0A">
が無相関，独立のとき，以下の式が成り立ちます．

#### 無相関 ：

２つの確率信号が無相関であるとき，

- <img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+E%5Bx_ny_n%5D+%3D+E%5BX_n%5DE%5By_n%5D+%0A" >

- <img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+Cov%28x_n%2C+y_n%29+%3D+0%0A">

が成り立ちます．








## 部分空間分解

