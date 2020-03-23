#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ex.1 基本的な関数の使い方
#
#       - time関数による時間計測を学ぶ
#       - forループの使い方を学ぶ
#       - print関数の使い方を学ぶ
#       - ブレークポイント，対話型インタプリタの使い方を学ぶ

# ↓↓ モジュールのインポート
import time
# ↑↑ モジュールのインポートここまで

if __name__ == '__main__':

    ### ============================================
    ###
    ###      例題
    ###
    ### ============================================
    ##  ここでは，等比数列を計算しましょう！
    ##  - A = [1, 2, 4, 8, 16, 32, ...]

    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  1. forループを使った等比数列の計算
    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  - forループには'{}'や'end'は使用しません．処理したい行に「インデント」を入れる．
    ##  - 時間の取得にはtime.time()を用いる．

    A_1 = [1]  # 計算結果を入れるリストの作成
    start1 = time.time()  # 時間の取得

    # ↓↓ forループここから
    for i in range(100):  # range(n) : 0, 1, ..., n-1 の数列．for は数列から一つずつ取り出して i に代入している
        #   - x[-1] : 配列xの末尾
        x = 2 * A_1[-1]

        # 答えをリストの末尾に追加
        A_1.append(x)

    # ↑↑ forループここまで (インデントをforと同じ階層にする)
    finish1 = time.time()  # 時間の取得 (ここはforループで処理されない))

    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  2. 内包表記を使った等比数列の計算
    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    start2 = time.time()
    # ↓↓ 内包表記ここから
    A_2 = [2 ** a for a in range(100 + 1)]  # ** -> 指数
    # ↑↑ 内包表記ここまで
    finish2 = time.time()

    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  3. ターミナルに結果を表示
    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  - {i} : formatで指定した，i番目の変数を出力
    ##  - x[1:] : 配列xの2番目から最後までの要素
    print('Elasped Time (for loop) : {0}[s] \nElasped Time (comprehension) : {1}[s]\n'.format(finish1 - start1,
                                                                                            finish2 - start2))
    print('Result of for :\n{0}\n'.format(A_1[0:10]))  # x[0:10] : x[0]～x[9]
    print('Result of Comprehension :\n{0}'.format(A_2[0:10]))

    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  4. ブレークポイントを使って対話型インタプリタを使ってみる．
    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  - Pycharmでは行番号のすぐ右側をクリックするとブレークポイント(赤い●)をつけることができる．
    ##  - デバッグモードで実行(ミドリの虫マーク)すると，ブレークポイント手前の行で実行が一時停止する．

    #   表示用ローカル関数１
    def interpreter_ex1():
        print('Exercise Break Point & Interactive Interpreter')
        print('\nデバッグコンソールを立ち上げ，\n------------------------\nA_2\n------------------------\nと打ち込んで配列A_2の中身の一部を見てみましょう．')
        print('# Pycharmコンソール左側「Show Python Prompt」というボタンです．\n')
        return 0

    interpreter_ex1()
    print('←この行にブレークポイントを打ち込んでデバッグモードで実行してください．(行の左側に赤い●がつきます)\n')
    print('Finished !! (←ブレークポイント以降の行は表示されないはず) !!')


