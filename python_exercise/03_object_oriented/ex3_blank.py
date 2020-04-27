#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ex.3 関数定義とクラス定義
#
#       - 関数の定義を学ぶ
#       - クラスの定義を学ぶ
#       - 関数・クラスの使い方の違いを学ぶ

### ============================================
###
###      例題 1.
###
### ============================================
##  関数・クラスの定義方法について学びましょう！

##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##  1.   関数の定義
##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##  - def で関数を定義する．
#   - 処理内容は２つの引数の和．



##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##  2.   クラスの定義
##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   - クラスはインスタンス(=内部変数)やメソッド(=内部関数)を内包するオブジェクト．
#   - class で定義する．
#   - コントラクタ定義   ：コントラクタ(=__init__関数)内部でインスタンスを設定する．
#       ・self.sum = 0   ：累積和，初期値 0 にする．
#       ・self.count =0  ：累積数，初期値 0 にする．
#   - メソッド定義       ：メソッドは通常の関数と同様に定義される．ただし，第１引数をselfにする．
#       ・Accumulate     ：引数 b を累積値に加算する．
#       ・call           ：Accumulate_class 自身で呼ばれる処理．




if __name__ == '__main__':

    ### ============================================
    ###
    ###      例題 2.
    ###
    ### ============================================
    ##  関数・クラスを使ってみよう！

    Class1 = Accumulate_class()
    Class2 = Accumulate_class()

    Array = [1,2,3,4,5,6,7,8,9,10]

    #   累積和の計算
    sum_func = 0
    for x in Array:

        #   1. 関数を使った累積和



        #   2. クラスのメソッドを使った累積和
        #   - メソッド名を呼び出すには，「クラス名.メソッド名()」とする．



    #   callメソッドの使い方
    #   - 単に「クラス名()」ではcallメソッドが呼び出される．
    sum_class, cnt = Class1()

    #   表示
    print('= 練習課題：関数とクラスの定義・使い方 =\n')
    print('[1] 関数とクラスの計算結果')
    print('関数による計算結果           = {0}'.format(sum_func))
    print('クラスメソッドによる計算結果 = {0},  (カウント数={1})'.format(sum_class, cnt))
    print('\n[2] 実は「クラス名.インスタンス」で内部変数の値も参照できる．')
    print('クラスのsumインスタンス      = {0},  (countインスタンス={1})'.format(Class1.sum, Class1.count))
    print('別のクラスのsumインスタンス  = {0},  (countインスタンス={1})'.format(Class2.sum, Class2.count))
    print('\nクラスには，内部で変数を管理できるという強みがある．')
    print('上のように，別クラス間では内部変数も独立している．')