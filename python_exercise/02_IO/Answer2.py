#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   Ex.2 ファイルの読み込み・書き込み
#
#       - csv, 音声, 画像ファイルの読み込み方法を学ぶ
#       - matplotlibの使い方を学ぶ
#       - バイナリファイル(npy)の保存・読み込み方法を学ぶ

import numpy as np
import soundfile as sf  # wavファイルを扱う際のモジュール
import scipy.signal as sg
import urllib.request

from matplotlib import pyplot as plt

if __name__ == '__main__':
    ##----------------------------------------------------------------------------------
    ##
    ##  練習問題
    ##
    ##----------------------------------------------------------------------------------
    ##  音源分離処理をやってみよう！

    #   (wavファイルのダウンロード) ← ローカルへ保存していたら必要なし
    #urllib.request.urlretrieve('https://raw.githubusercontent.com/julius-speech/segmentation-kit/master/wav/sample.wav', 'sample.wav')


    #   wavファイルの読み込み
    wav_data, fs = sf.read('stereo.wav')  # (データ, サンプリング周波数)
    x_l = wav_data[:,0]           # 左チャンネル
    x_r = wav_data[:,1]           # 右チャンネル

    #   フレーム分割 & FFT (ハーフオーバーラップ)
    #   - x_l, x_r を sg.stft で短時間FFTする．
    #   - セグメント長を 1024, オーバーラップを 512 に設定する．
    f, t, X_l = sg.stft(x_l, nperseg=2048, noverlap=int(2048*3/4))
    _, _, X_r = sg.stft(x_r, nperseg=2048, noverlap=int(2048*3/4))

    #   振幅情報だけを抽出
    #   - np.abs() で振幅を抽出する．
    Amp_l = np.abs(X_l)
    Amp_r = np.abs(X_r)

    #   スペクトログラム (処理前)
    Amp_l_log = 2 * np.log10(Amp_l+10**(-5))     # 対数振幅スペクトルに変換
    plt.figure('Spectrogram : 処理前')
    plt.imshow(Amp_l_log, aspect='auto', origin='lower', cmap='jet', interpolation='bilinear', extent=[t.min() / fs, t.max() / fs, fs * f.min(), fs * f.max()])
    plt.xlabel('Time [s]'); plt.ylabel('Frequency [Hz]'); plt.title('Origin (L)')

    #   スペクトログラムに対する音源分離処理
    Mask_l = []                         # 左チャンネルのマスク
    Mask_r = []                         # 右チャンネルのマスク
    for (amp_l, amp_r) in zip(Amp_l.T, Amp_r.T):  # Amp_lとAmp_rの各フレームのスペクトルを同時に取り出し

        # ↓↓ バイナリマスクの作成
        index_l = (amp_l  >= amp_r)		# 右チャンネルより左チャンネルの振幅が大きいとTrue
        index_r = (amp_r  >= amp_l)     # 左チャンネルより右チャンネルの振幅が大きいとTrue
        # index_* が True になる周波数の振幅 → そのまま
        # index_* が False になる周波数の振幅 → 0
        # ↑↑ バイナリマスクの作成

        # マスクを配列に入れる
        Mask_l.append(index_l)
        Mask_r.append(index_r)

    Mask_l = np.array(Mask_l).T   # numpy.arrayに変換 & 転置
    Mask_r = np.array(Mask_r).T   # numpy.arrayに変換 & 転置

    #   ↓↓ マスキング
    X_l_new = Mask_l * X_l
    X_r_new = Mask_r * X_r
    #   ↑↑ マスキング

    #   振幅スペクトル (表示用：左チャンネルだけ)
    A_l_new = np.abs(X_l_new)

    #   スペクトログラム (処理後)
    Amp_l_log_new = 2 * np.log10(A_l_new+10**(-5))  # 対数振幅スペクトルに変換
    plt.figure('Spectrogram : 処理後')
    plt.imshow(Amp_l_log_new, aspect='auto', origin='lower', cmap='jet', interpolation='bilinear', extent=[t.min() / fs, t.max() / fs, fs * f.min(), fs * f.max()])
    plt.xlabel('Time [s]'); plt.ylabel('Frequency [Hz]'); plt.title('Output (L)')
    plt.show()

    #   ↓↓ 逆FFTで波形に変換 & wav に保存
    _, x_l_new = sg.istft(X_l_new, fs=fs, noverlap=int(2048*3/4))
    sf.write('output_L.wav', x_l_new, fs)

    _, x_r_new = sg.istft(X_r_new, fs=fs, noverlap=int(2048*3/4))
    sf.write('output_R.wav', x_r_new, fs)
    #   ↑↑ 逆FFTで波形に変換 & wav に保存

    ##  応用問題1．
    ##  stftのフレーム長を2048，オーバーラップを2048 * 3/4 に設定して処理を行い，
    ##  音質の違いを聞いてみよう！
    
