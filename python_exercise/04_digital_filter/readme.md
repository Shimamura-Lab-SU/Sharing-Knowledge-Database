# ディジタルフィルタ設計

ここでは，信号処理について勉強しましょう． 
まずは説明を読んで，練習問題に取り組みましょう．

   - 説明：信号処理 (このページ)
   - [練習問題4](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/04_digital_filter/exercise.md)

## ディジタルフィルタ

環境の情報をマイクロホンやカメラなどのセンサで取得したとき，それらの情報はアナログ信号に変換されます．
アナログ信号は，**A-D変換**を行ったのち，ディジタル処理を施し，**D-A変換**で，再びアナログ信号に戻すことにより，高精度に処理されます．
**ディジタル信号処理**とは，通常，そのA-D変換から，D-A変換までの間の行程を指します．
すでに，ディジタルに変換されたデ一タが与えられた，という前提において，データをいかに効果的に，かつ能率的に処理するかが，ディジタル信号処理の課題となります．

**ディジタルフィルタ**は，入力信号の周波数成分に変化を与えることにより，所望とされる処理を実現する回路です．
信号に含まれる雑音成分の除去は，ディジタルフィルタにおける，重要な役割のひとつとなっています．
ディジタルフィルタは，その構成法の違いから，**有限長インパルス応答(FIR : Finite Impulse Response)フィルタ**と，
**無限長インパルス応答(IIR : Infinite Impulse Response)フィルタ**に大別されます．
それぞれ以下の特徴があります．

- FIRフィルタ：常に安定．理想特性に近い周波数特性を実現するためには，回路規模が大きくなる．
- IIRフィルタ：小さい回路規模で良好な特性を得られるが，安定性を保証するための工夫が必要．

## FIRフィルタの周波数特性

今回はFIRフィルタの設計について取り上げます．
FIRフィルタの**周波数特性**は，図に示すような，**振幅特性**と**位相特性**からなります．
フィルタの**伝達関数**:
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+T%28z%29%0A">
を，

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%7D%0AT%28z%29+%3D+%5Csum_%7Bi%3D0%7D%5E%7BS%7D+h_c%28i%29+z%5E%7B-i%7D%0A%5Cend%7Balign%7D" >

とします．
ここで，
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+S" >
はフィルタの次数，
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+h_c(i)" >
はフィルタの係数，また
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+z" >
は，**Z変換**における複素数を表します．
上の式における複素数
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+z" >
を
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+z+%3D+e%5E%7Bj%5Comega%7D" >
とした場合が，**フーリエ変換**の変換式に対応します．
振幅特性
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+A%28%5Comega%29" >
，および 位相特性
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctheta%28%5Comega%29" >
は，
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+T%28e%5E%7Bj%5Comega%7D%29" >
を用いてそれぞれ

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%26A%28%5Comega%29+%3D+%5Cleft%7C+T+%5Cleft%28e%5E%7Bj%5Comega%7D%5Cright%29+%5Cright%7C+%5Cqquad+%5Cleft%28+%5Cbecause+%5C%3B+z+%3D+e%5E%7Bj%5Comega%7D+%5Cright%29%5C%5C%0A%26%5Ctheta%28%5Comega%29+%3D+%5Ctan%5E%7B-1%7D+%5Cfrac%7B%5CIm+%5Cleft%5B+T+%5Cleft%28e%5E%7Bj%5Comega%7D%5Cright%29+%5Cright%5D%7D%7B%5CRe+%5Cleft%5B+T+%5Cleft%28e%5E%7Bj%5Comega%7D%5Cright%29+%5Cright%5D%7D%0A%5Cqquad+%5Cleft%28+%5Ctan+%5Ctheta%28%5Comega%29+%3D+%5Cfrac%7B%5CIm+%5Cleft%5B+T+%5Cleft%28e%5E%7Bj%5Comega%7D%5Cright%29+%5Cright%5D%7D%7B%5CRe+%5Cleft%5B+T+%5Cleft%28e%5E%7Bj%5Comega%7D%5Cright%29+%5Cright%5D%7D+%5Cright%29%0A%5Cend%7Balign%2A%7D"> 

で与えられます．
ここで，
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5CRe" >
は，複素数の実部(Real Part)を，また
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5CIm" >
は，複素数の虚部(Imaginary Part)を表します．

フィルタの理想特性は，通過域で1，阻止域で0の振幅特性を有します．
図に**理想ローパスフィルタ**の振幅特性を表しています．

## FIRフィルタ設計

ここではFIRフィルタの設計法として

- フーリエ級数展開法
- 窓関数法

を紹介します．

### 1. フーリエ級数展開法

FIRフィルタの代表的な設計法は，次に挙げる**フーリエ級数展開法**です．
これにより，FIRフィルタの係数は，所望特性にあわせて決定されます．
1 [Hz]の**サンプリング周波数**を仮定した場合，通過域の**カットオフ周波数**を
<img src="https://render.githubusercontent.com/render/math?math=%5Ctextstyle+%5Comega_c" >
とすると，理想ローパスフィルタの**インパルス応答**
<img src="https://render.githubusercontent.com/render/math?math=%5Ctextstyle+h%28n%29" >
は，

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ah%28n%29+%3D+%5Cfrac%7B1%7D%7Bn%5Cpi%7D+%5Csin+%5Cleft%28+%5Comega_c+n+%5Cright%29+%5Cquad+%28-%5Cinfty+%3C+n+%3C+%2B%5Cinfty%29%0A%5Cend%7Balign%2A%7D" >

で与えられます．
したがって，この応答を有限長，すなわち，

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0An+%3D+-N%2C%5C%2C-%28N-1%29%2C%5C%2C%5Cdots%2C-1%2C%5C%2C0%2C%5C%2C1%2C%5C%2C%5Cdots%2CN-1%2C%5C%2CN%0A%5Cend%7Balign%2A%7D" >

の範囲に切りとることにより，FIRフィルタの係数は求められます．
しかし，このままでは，**因果性**を満たさないために，
<img src="https://render.githubusercontent.com/render/math?math=%5Ctextstyle+n" >
の正の方向に
<img src="https://render.githubusercontent.com/render/math?math=%5Ctextstyle+N" >
だけずらして，

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ah_c%28n%29+%3D+h%28n-N%29+%5Cquad+%28n+%3D+0%2C1%2C2%2C%5Cdots%2C2N%29%0A%5Cend%7Balign%2A%7D" >

とし，これを，フィルタ係数として用います．
> 因果性：  
> 一般に信号にフィルタ処理を行なう際に，現在の信号と過去の信号のみを利用し，未来の信号を利用しないよう設定します．
> これを因果性を満たす，と呼びます．

### 2. 窓関数法

FIRフィルタの周波数特性は，一般に**ギブス現象**と呼ばれる現象を含んでしまいます．
> ギブス現象：  
> フィルタの理想特性のように不連続な関数をフーリエ級数展開すると，不連続点の近くで元の関数値に収束せず、「角」が飛び出てしまいます．これをギブス現象と呼びます．

これを緩和するために，しばしば**窓関数**が用いられます．
たとえば，次の式で表される窓関数は，**ハミング窓**と呼ばれる窓関数です．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Aw%28n%29+%3D+0.5+%2B+0.5+%5Ccos+%5Cleft%28+%5Cfrac%7Bn%7D%7BN%7D%5Cpi+%5Cright%29+%5Cquad+%28-N+%5Cleq+n+%5Cleq+N%29%0A%5Cend%7Balign%2A%7D" >

この他，**ハニング窓** :

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Aw%28n%29+%3D+0.5+%2B+0.5+%5Ccos+%5Cleft%28+%5Cfrac%7Bn%7D%7BN%7D%5Cpi+%5Cright%29+%5Cquad+%28-N+%5Cleq+n+%5Cleq+N%29%0A%5Cend%7Balign%2A%7D" >

や，**バートレット窓** :

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Aw%28n%29+%3D+1+-+%5Cfrac%7B%7Cn%7C%7D%7BN%7D+%5Cquad+%28-N+%5Cleq+n+%5Cleq+N%29%0A%5Cend%7Balign%2A%7D" >

などといった窓関数もありますが，いずれにしても，因果性を満たすように，

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Aw_c%28n%29+%3D+w%28n-N%29+%5Cquad+%28n+%3D+0%2C1%2C2%2C%5Cdots%2C2N%29%0A%5Cend%7Balign%2A%7D" >

と補正したのち，フィルタ係数 : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+h_c%28n%29" >
に掛け合わせることにより，

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ah_%7Bcw%7D%28n%29+%3D+w_c%28n%29+h_c%28n%29%0A%5Cend%7Balign%2A%7D" >

として，フィルタ係数を用います．

## ハイパス・バンドパスフィルタ

時間信号 : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+g%28n%29" >
のフーリエ変換を，
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+G+%5Cleft%28e%5E%7Bj%5Comega%7D%5Cright%29" >
とします．
これを，ここでは

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AG+%5Cleft%28e%5E%7Bj%5Comega%7D%5Cright%29+%3D+%5Cmathcal%7BF%7D+%5Cleft%5B+g%28n%29+%5Cright%5D%0A%5Cend%7Balign%2A%7D" >

と表記することにします．
このようなフーリエ変換においては，次の**周波数シフト**の性質があります．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AG+%5Cleft%28e%5E%7Bj%28%5Comega-%5Comega_0%29%7D%5Cright%29+%3D+%5Cmathcal%7BF%7D+%5Cleft%5B+g%28n%29+%5Ccdot+e%5E%7Bj%5Comega_0+n%7D+%5Cright%5D%0A%5Cend%7Balign%2A%7D" >

この性質を利用すると，ローパスフィルタの係数 : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+h_%7B%5Cmathrm%7BLP%7D%7D%28n%29" >
を，次のように変形することにより，**バンドパスフィルタ**の係数 : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+h_%7B%5Cmathrm%7BBP%7D%7D%28n%29" >
が得られます．

<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ah_%7B%5Cmathrm%7BBP%7D%7D%28n%29+%3D+h_%7B%5Cmathrm%7BLP%7D%7D%28n%29+%5Ccdot+e%5E%7Bj%5Comega_0+n%7D%0A%5Cend%7Balign%2A%7D" >

ただし，ここでの
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+h_%7B%5Cmathrm%7BBP%7D%7D%28n%29" >
は，一般に複素数となります．
実部のみを取り出せば，任意の**中心周波数** : 
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Comega_0%0A" >
の，バンドパスフィルタの係数が得られます．
しかし，sin関数とcos関数の足し合わせによって得られる周波数シフトの特性は，
実部，すなわち，cos関数部のみを取り出すことにより，振幅値が 1/2 に減衰してしまうため，
係数値を，それぞれ2倍して用いることにより，振幅特性が保持されるという点に，注意する必要があります．

なお，**ハイパスフィルタ**は，上記の周波数シフトにおいて，
<img src="https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Comega_0+%3D+%5Cpi%0A" >
[rad/s] の場合に相当します．

# 練習問題

- [練習問題4](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/04_digital_filter/exercise.md)
