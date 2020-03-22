#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ex.2 ファイルの読み込み・書き込み
#
#       - csv, 音声, 画像ファイルの読み込み方法を学ぶ
#       - matplotlibの使い方を学ぶ
#       - バイナリファイル(npy)の保存・読み込み方法を学ぶ

# ↓↓ モジュールのインポート






# ↑↑ モジュールのインポートここまで

if __name__ == '__main__':

    ### ============================================
    ###
    ###      例題 1.
    ###
    ### ============================================
    ##  ここでは，様々なファイルの読み込みと表示をやってみましょう！

    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  1.   csvファイルの読み込み
    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  - pd.read_csv を用いたcsvファイルの読み込みを行う．
    ##  - 読み込んだcsvファイルはprint()で表示できる．

    #   (csvファイルのダウンロード) ← ローカルへ保存していたら必要なし
    import urllib.request
    urllib.request.urlretrieve('https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv',
                               'iris.csv')  # アイリスデータをwebからダウンロード

    #   csvファイルの読み込み・表示



    ##  ここまでで一度実行

    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  2.   wavファイルの読み込みと表示
    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  - sf.read でwavファイル読み込み，sf.writeでwavファイル書き込み．
    ##  - sg.stft で複素スペクトログラムに変換する．
    ##  - 対数振幅スペクトルを表示する．オーバーラップあり/なしでの違いを見てみよう．

    #   (wavファイルのダウンロード) ← ローカルへ保存していたら必要なし
    urllib.request.urlretrieve('https://raw.githubusercontent.com/julius-speech/segmentation-kit/master/wav/sample.wav',
                               'sample.wav')    # 男性の音声wavファイルをwebからダウンロード

    #   wavファイルの読み込み



    #   スペクトログラムに変換
    #   sg.stft の戻り値 -> (周波数，時間，スペクトログラム)





    #   波形の表示





    #   スペクトログラムの表示
    #   - 表示の際には，一般にスペクトログラムを対数振幅スペクトログラムに変換する
    #   オーバーラップなし

    #plt.figure('Spectrogram Low Resolution')
    #plt.imshow()
    # plt.xlabel('Time [s]'); plt.ylabel('Frequency [Hz]');


    #   ハーフオーバーラップ (↑とほぼ同じ．コピペして部分的に改変しよう)

    #plt.figure('Spectrogram High Resolution')
    #plt.imshow()
    #plt.xlabel('Time [s]');plt.ylabel('Frequency [Hz]')


    #plt.show()              #   ウィンドウの表示・固定 (ウィンドウを閉じるまで処理が一時停止)

    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  3.   jpgファイルの読み込みと表示
    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #   (wavファイルのダウンロード) ← ローカルへ保存していたら必要なし
    urllib.request.urlretrieve('https://www.ece.rice.edu/~wakin/images/lena512color.tiff', 'lena.tiff')

    #   画像ファイルの読み込み & 表示



    ### ============================================
    ###
    ###      例題 2.
    ###
    ### ============================================
    ##  データの保存&読み込みをやってみましょう！

    #   音声のwavファイルへの保存


    #   画像データの加工例 (grayscale化)


    #   画像のnpyファイルへの保存 & jpgファイルへの保存



    #   画像のnpyファイルの読み込み & jpgファイの読み込み



    #   画像の表示



