#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ex.1 基本的な関数の使い方
#
#       - time関数による時間計測を学ぶ
#       - forループの使い方を学ぶ
#       - print関数の使い方を学ぶ
#       - pythonのリストとnumpy.ndarrayの使い方を学ぶ

import time
import numpy as np

if __name__ == '__main__':

    ##----------------------------------------------------------------------------------
    ##
    ##  練習問題
    ##
    ##----------------------------------------------------------------------------------

    Ex_array = [31, 58, 20, 25, 57, 87, 44, 89, 81, 36, 63, 1, 43, 60, 49, 54, 68,
                71, 88, 94, 66, 48, 84, 77, 27, 51, 76, 90, 33, 18, 92, 5, 19, 32,
                41, 3, 40, 59, 93, 38, 45, 72, 95, 74, 11, 83, 97, 28, 35, 98, 62,
                67, 14, 16, 6, 70, 9, 52, 10, 80, 78, 12, 96, 8, 13, 22, 15, 47,
                0, 86, 73, 75, 4, 85, 21, 39, 46, 55, 17, 64, 82, 69, 99, 30, 23,
                42, 34, 56, 24, 7, 61, 26, 79, 91, 2, 29, 53, 65, 37, 50]

    print('Ex_array = {0}'.format(Ex_array))
    print('size : {0}'.format(len(Ex_array)))

    ##  練習問題1.
    ## ↑の配列Ex_arrayを(10,10)の行列に変形せよ．
    ##  このとき，forループ，内包表記，np.reshapeのそれぞれを用いた３種類の変形方法を試せ．
    ## ただし，破壊的な代入はせず新たな配列を作ること．

    ## forループの処理↓↓
    Ex_array_for = []
    for i in range(10):
        Ex_array_for.append(Ex_array[i * 10:(i + 1) * 10])

    print('Result of for :\n{0}\n'.format(Ex_array_for))

    ## 内包表記の処理↓↓
    #Ex_array_com = []
    Ex_array_com = [Ex_array[i * 10:(i + 1) * 10] for i in range(10)]

    print('Result of for :\n{0}\n'.format(Ex_array_com))

    ## reshapeの処理↓↓
    ## - np.array型で処理してください．
    ## - np.arrayとpythonのリストはどちらも行列(テンソル)を表現できますが，データ型が異なります．
    #Ex_array_res = np.array([])
    Ex_array_res = np.reshape(Ex_array, (10, 10))

    print('Result of reshape :\n{0}\n'.format(Ex_array_res))

    ## 変数の型の違いを確認しましょう．
    print('Var types :\n Ex_array = {0},\n Ex_array_for = {1},\n Ex_array_com = {2},\n Ex_array_res={3}\n'
          .format(type(Ex_array), type(Ex_array_for), type(Ex_array_com), type(Ex_array_res)))

    ##  練習問題2.
    ##  Ex_array_resを行方向に降順でソートし，表示せよ．
    ##  (ヒント) np.sort を使う．
    #Ex_sort = []

    ## sortの処理↓↓
    Ex_sort = np.sort(Ex_array_res, axis=1)
    print('Result of sort :\n{0}\n'.format(Ex_sort))

    ##  練習問題3.
    ##  Ex_array_sortから 50以上の要素を1，50未満の要素を0にせよ．
    ##  (ヒント) numpy の「要素の検索」あるいは「要素の置換」を使う．
    Ex_01 = Ex_sort
    Ex_01[Ex_01 < 50] = 0
    Ex_01[Ex_01 >= 50] = 1
    # Ex_01 = np.where(Ex_01 < 50,0,1) # 別解

    print('Result of 0 or 1 :\n{0}'.format(Ex_01))

    ##  応用問題1.
    ##  Ex_array を(7,16)のサイズに変形せよ．
    ##  ただし，足りない要素は0で埋める．
    ##  (ヒント) ndarray の resize を使う．

    A = np.array(Ex_array)
    A.resize((7, 16))
    print('Result of resize :\n{0}'.format(A))
