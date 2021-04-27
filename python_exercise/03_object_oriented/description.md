# クラス・関数の定義と使い方


クラスは関数や変数を内包できる**オブジェクト**です．
特に，以下の場合には関数ではなくクラスを使うと便利です．
 - 関数に初期値を設定したいとき
 - 内部変数がほしいとき

### コンストラクタ

初期化関数のこと．`__init__`で定義する．コンストラクタ内部でクラスの内部変数を定義する．

### クラス継承

クラスに新たな内部変数を追加したいとき，あるいはメソッドの一部を変更したいとき，クラス継承を行なうことができる．

例：  
~~~
   # 元のクラス
   class Base_class:
   
       def __init__(self, init='カレー'):
           self.food = init # 初期値の定義
           
       def like(self) :
           print('好きな食べ物は{0}です．'.format(self.food))

　# 継承クラス (継承元クラス：Base_class)
   class New_class(Base_class):
       
       # 今回，initはBase_classから継承する．
       
       # 新たなメソッドを追加
       def dislike(self) :
           print('嫌いな食べ物は{0}です．'.format(self.food))
           
  Food1 = Base_class(init='ラーメン')
　Food2 = New_class(init='ブロッコリー')
 
  Food1.like() # Base_classのlikeメソッドを実行
　Food2.like() # New_classのlikeメソッドを実行
　Food2.dislike() # New_classのdislikeメソッドを実行
~~~

# 練習課題

> - [ex3.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/03_object_oriented/ex3.py)
> - [ex3_blank.py](https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/03_object_oriented/ex3_blank.py)
