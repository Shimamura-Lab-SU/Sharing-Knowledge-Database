#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ex.2 ファイルの読み込み・書き込み
#
#       - csv, 音声, 画像ファイルの読み込み方法を学ぶ
#       - matplotlibの使い方を学ぶ
#       - バイナリファイル(npy)の保存・読み込み方法を学ぶ

# ↓↓ モジュールのインポート
import numpy as np
import pandas as pd                         # csvを扱う際のモジュール
import soundfile as sf                      # wavファイルを扱う際のモジュール
import scipy.signal as sg                   # 信号処理用ライブラリ scipy.signal
import cv2                                  # tifファイル(画像)を扱う際のモジュール
from matplotlib import pyplot as plt        # 表示用モジュール
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

    #   irisデータの
    from sklearn.datasets import load_iris
    iris = load_iris()
    urllib.request.urlretrieve('https://raw.githubusercontent.com/YosukeSugiura/datamining-excercise/master/3_classification/iris.csv',
                               'iris.csv')  # アイリスデータをwebからダウンロード

    #   csvファイルの読み込み・表示
    csv_data = pd.read_csv('iris.csv')
    print(csv_data)

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
    wav_data, fs = sf.read('sample.wav')  # (データ, サンプリング周波数)
    t = np.arange(wav_data.size) / fs

    #   スペクトログラムに変換
    #   sg.stft の戻り値 -> (周波数，時間，スペクトログラム)
    f_x, t_x, X1 = sg.stft(wav_data, fs=fs, nperseg=1024, noverlap=0)       # オーバーラップなし
    _, _, X2     = sg.stft(wav_data, fs=fs, nperseg=1024, noverlap=512)     # ハーフオーバーラップ
    X1_amp       = np.abs(X1)       # 振幅を計算
    X2_amp       = np.abs(X2)       # 振幅を計算

    #   波形の表示
    plt.figure('Waveform')
    plt.plot(t, wav_data)
    plt.xlabel('Time [s]'); plt.ylabel('Amplitude')
    plt.xlim([0, t[-1]])    # x[-1] : 配列 x の最後の要素

    #   スペクトログラムの表示
    #   - 表示の際には，一般にスペクトログラムを対数振幅スペクトログラムに変換する
    #   オーバーラップなし
    X1_log = 2 * np.log10(X1_amp)               # 対数振幅スペクトログラムに変換
    plt.figure('Spectrogram Low Resolution')
    plt.imshow(X1_log, aspect='auto', origin='lower', cmap='jet', interpolation='bilinear', extent=[t_x.min(), t_x.max(), f_x.min(), f_x.max()])
    plt.xlabel('Time [s]'); plt.ylabel('Frequency [Hz]')
    plt.title('Spectrogram without overlap')

    #   ハーフオーバーラップ (↑とほぼ同じ．コピペして部分的に改変しよう)
    X2_log = 2 * np.log10(X2_amp)  # 対数振幅スペクトログラムに変換
    plt.figure('Spectrogram High Resolution')
    plt.imshow(X2_log, aspect='auto', origin='lower', cmap='jet', interpolation='bilinear', extent=[t_x.min(), t_x.max(), f_x.min(), f_x.max()])
    plt.xlabel('Time [s]');plt.ylabel('Frequency [Hz]')
    plt.title('Spectrogram with half overlap')

    plt.show()              #   ウィンドウの表示・固定 (ウィンドウを閉じるまで処理が一時停止)

    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ##  3.   jpgファイルの読み込みと表示
    ##  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #   (wavファイルのダウンロード) ← ローカルへ保存していたら必要なし
    urllib.request.urlretrieve('https://www.ece.rice.edu/~wakin/images/lena512color.tiff', 'lena.tiff')

    #   画像ファイルの読み込み & 表示
    tif_data = cv2.imread('lena.tiff')          # 画像読み込み
    cv2.imshow('Color Image',tif_data)          # 画像表示

    ### ============================================
    ###
    ###      例題 2.
    ###
    ### ============================================
    ##  データの保存&読み込みをやってみましょう！

    #   音声のwavファイルへの保存
    sf.write('sample_output.wav',wav_data, fs)

    #   画像データの加工例 (grayscale化)
    img_gray = cv2.cvtColor(tif_data, cv2.COLOR_BGR2GRAY)

    #   画像のnpyファイルへの保存 & jpgファイルへの保存
    np.save('saved_image.npy', img_gray)        # npyファイル(ロスレス)：数値行列や音声データでもOK
    cv2.imwrite('saved_image.jpg', img_gray)    # jpgファイル(ロス)

    #   画像のnpyファイルの読み込み & jpgファイの読み込み
    load_data = np.load('saved_image.npy')
    jpg_data = cv2.imread('saved_image.jpg')

    #   画像の表示
    cv2.imshow('Npy Image',load_data)
    cv2.imshow('JPG Image',jpg_data)
    cv2.waitKey(0)
