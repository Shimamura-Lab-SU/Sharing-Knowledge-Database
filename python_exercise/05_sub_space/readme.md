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

確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%0A">
が**確率分布関数**(Probability Distribution Function : PDF)
<img src="https://render.githubusercontent.com/render/math?math=%5Ctextstyle+p%28x%29%0A">
に従うとしたとき，

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cdisplaystyle+%5Cint_%7B%5Cinfty%7D%5E%7B%5Cinfty%7D+p%28x%29+dx+%3D+1%0A">

が成り立つ．


### 2. 平均・分散・共分散
時刻
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+n%0A">
の信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x_n">
における平均，分散，共分散は以下の通り計算されます．

#### 平均(期待値) ：    
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cdisplaystyle+%5Cbar%7Bx_n%7D+%3D+E%5Bx_n%5D+%3D+%5Cint+x_n+p%28x_n%29+dx_n+%5Csimeq+%5Cfrac%7B1%7D%7BN%7D%5Csum%5E%7BN-1%7D_%7Bi%3D0%7D+x_%7Bn-i%7D">

#### 分散 ：  
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+E%5B%28x_n-%5Cbar%7Bx%7D%29%5E2%5D+%5Csimeq+%5Cfrac%7B1%7D%7BN%7D%5Csum%5E%7BN-1%7D_%7Bi%3D0%7D+%28x_n+-+%5Cbar%7Bx%7D%29%5E2%0A">

#### 共分散 ：


## 無相関・独立

まず信号の無相関性・独立性について説明します．
２つの確率信号
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%28n%29%2C+y%28n%29%0A" >
が与えられたとき，**相互相関**は以下の式で計算できます．

    <img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AR%28%5Ctau%29+%3D+%5Cmathbb%7BE%7D%5Cleft%5B+x%28n%2B%5Ctau%29y%28n%29+%5Cright%5D+%3D+%5Cfrac%7B1%7D%7B2M%7D%5Csum%5E%7BM-1%7D_%7Bi%3D-M%7D+x%28n%2B%5Ctau%2Bi%29y%28n%2Bi%29%0A%5Cend%7Balign%2A%7D%0A" >

この相互相関値が以下のとき，２つの信号は無相関，あるいは独立であると言われます．

- 無相関：すべての<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctau%0A" >で<img src="https://render.githubusercontent.com/render/math?math=%5Ctextstyle+R%28%5Ctau%29%3D0%0A" >
- 独立：
といいます．






## 部分空間分解

