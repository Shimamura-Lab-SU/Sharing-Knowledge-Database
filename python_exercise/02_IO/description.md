# 第２回 Pythonの基本的な関数の使い方

- [CSVファイルの読み出し・書き込み](#CSVファイルの読み書き)
- [Imageファイルの読み出し・書き込み](#画像ファイルの読み書きと表示)
- [音声ファイルの読み出し・書き込み](#音声ファイルの読み書き)
- [matplotlibの使い方](#matplotlibの使い方)

# CSVファイルの読み書き

CSVファイルの読み書きを行う方法はいくつかありますが，その中でもpandasモジュールを使う方法を紹介します．
まずはpandasをimportしてください．
```@Python
import pandas as pd			# pandasモジュールのimport
```

### csvファイルの読み込み
```@Python
csv_data = pd.read_csv('input.csv')	# csvファイルの読み出し
```

### csvファイルの書き込み
```@Python
csv_data.to_csv('output.csv')		# csvファイルの書き込み
```

# 画像ファイルの読み書きと表示

画像の読み出し・表示・書き込みにはOpenCVモジュールを使用します．
まずはOpenCVをimportしてください．
```@Python
import cv2			# OpenCVモジュールのimport
```

### 画像の読み込み
```@Python
image = cv2.imread('image.tiff')
```

### 画像の書き込み
```@Python
cv2.imwrite('image.tiff', image)
```

### 画像の表示
```@Python
cv2.imshow('Window Name',image) 
```
<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/image.jpg" width="380px">

# 音声ファイルの読み書き

音声の読み出し・書き込みにはpysoundfileモジュールを使用します．
まずはpysoundfileをimportしてください．
```@Python
import soundfile as sf        # OpenCVモジュールのimport
```

### 音声の読み込み
```@Python
wave_data, sampling_frequency = sf.read('sound.wav') # 戻り値：音声波形データ，サンプリング周波数
```

### 音声の書き込み
```@Python
sf.write('output.wav',wav_data, fs)
```

# matplotlibの使い方

グラフを表示したいときには，matplotlibモジュールを使います．

### グラフの表示

例として，音声を読み込んで音声波形をプロットします．
```@Python
import pmatplotlib.pyplot as plt      # pmatplotlib.pyplotモジュールのimport
import soundfile as sf                # OpenCVモジュールのimport

wave_data, sampling_frequency = sf.read('sound.wav') # 音声読み込み

plt.figure('Window Name')             # figureウィンドウの作成
plt.plot(wave_data)                   # グラフのプロット
plt.show()                            # グラフの表示
```
<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/waveform.jpg" width="380px">

### スペクトログラムの表示

音声を表現するもう一つの方法に**スペクトログラム**があります．
まず，音声波形を短い区間(=**フレーム**)に区切って，フーリエ変換します．この処理を**短時間フーリエ変換(STFT)** と呼びます．
STFTに絶対値したもの(=**振幅スペクトル**)を時系列で並べたものをスペクトログラムと呼びます．

スペクトログラムは以下のスクリプトで表示できます．
```@Python
import pmatplotlib.pyplot as plt      # pmatplotlib.pyplotモジュールのimport
import soundfile as sf                # OpenCVモジュールのimport
import scipy.signal as sg             # scipy.signalモジュールのimport

wave_data, sampling_frequency = sf.read('sound.wav') # 音声読み込み

# 短時間フーリエ変換
f, t, X = sg.stft(wave_data, nperseg=1024)  # 戻り値：周波数ビン，時間，複素スペクトログラム
X = np.abs(X)                         # 絶対値して振幅スペクトルを計算する

# スペクトログラムのプロット
plt.figure('Spectrogram')             # figureウィンドウの作成
plt.imshow(X, origin='lower', cmap='jet') # スペクトログラムのプロット
plt.show()                            # グラフの表示
```
<img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/python_exercise/02_IO/spec.png" width="580px">
