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


### 2. 平均・分散・共分散・相関係数

ここでは数学的な道具を説明します．
時刻
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n%0A">
の信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x_n">
における平均，分散，共分散，相関係数は以下の通り計算されます．

#### 平均(期待値) ：    
確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
の平均(期待値)は，取りうる値とその生起確率の積で計算されます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cdisplaystyle+%5Cbar%7Bx_n%7D+%3D+E%5Bx_n%5D+%3D+%5Cint+x_n+p%28x_n%29+dx_n+%5Csimeq+%5Cfrac%7B1%7D%7BN%7D%5Csum%5E%7BN-1%7D_%7Bi%3D0%7D+x_%7Bn-i%7D">

#### 分散 ：  

確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
の分散は以下の式で計算されます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Csigma%5E2+%3D+E%5B%28x_n-%5Cbar%7Bx%7D%29%5E2%5D+%5Csimeq+%5Cfrac%7B1%7D%7BN%7D+%5Csum_%7Bi%3D0%7D%5E%7BN-1%7D+%28x_n+-+%5Cbar%7Bx%7D%29%5E2%0A" >

#### 共分散 ：

共分散とは，２つの信号の関係性を表す指標です．
確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
と
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%0A">
の共分散は以下の式で計算されます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+Cov%28x%2Cy%29+%3D+E%5B%28x-%5Cbar%7Bx%7D%29%28y-%5Cbar%7By%7D%29%5D%0A" >

ちなみに，共分散には以下の関係が成り立ちます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+Cov%28x_n%2C+y_n%29+%3D+E%5Bx_ny_n%5D+-+E%5Bx_n%5DE%5By_n%5D%0A">

#### 相関係数：

相関係数とは２つの信号の**相関**を示すものです．
２つの信号の相関が大きいほど絶対値が大きくなり，小さいほど0に近づきます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cfrac%7BCov%28x_n%2C+y_n%29%7D%7B%5Csigma_x+%5Csigma_y%7D%0A" >


## 無相関・独立

まず信号間の独立・無相関について説明します．
独立・無相関は信号処理において特に重要な概念です．

２つの確率分布関数から生成される確率信号は，互いに**独立**になります．
例えば，異なる人から異なる文章・単語で発声される音声は，一般に(長時間見れば)独立となります．
これは人の声はそれぞれ異なる確率分布関数を持っているとモデル化できます(もちろん，同じ言葉を話している，
など特殊な状況であると独立ではなくなります)．
また同じく，音声と雑音も異なる確率分布関数を持ち，一般には独立になります．
画像分野においては，例えば口や目，鼻などの異なる形状を持つ構造(構造要素と呼んだりします)は互いに独立になります．
これを利用することで，音声の分離や雑音の除去，画像認識など，幅広い応用が実現できます．

無相関とは独立をカバーするより広い概念になります．
信号間の相関係数が0になることを**無相関**と呼びます．
独立な信号は一般に無相関になります．
ただし，無相関な信号は独立になるとは限りません．

詳しくは後で話します．


それでは無相関と独立の数学的定義について見ていきましょう．
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

#### 独立 ：

２つの確率信号が独立であるとき，**同時確率密度関数**
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p%28x%2C+y%29%0A" >
に以下の関係があります．

- <img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+p%28x%2C+y%29+%3D+p%28x%29p%28y%29%0A">

同時確率密度関数とは，２つの信号が同時刻で発生する値の確率を示した関数です．
これが，それぞれの確率分布関数の積になれば，独立になります．
独立であれば，無相関が成り立ちます．

### 独立と無相関の違い

独立と無相関の違いについて，同時確率密度関数から確認しましょう．
図は，






## 部分空間分解

