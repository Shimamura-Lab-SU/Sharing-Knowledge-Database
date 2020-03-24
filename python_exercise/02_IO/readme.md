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

# 音声ファイルの読み書き

音声の読み出し・書き込みにはpysoundfileモジュールを使用します．
まずはpysoundfileをimportしてください．
```@Python
import soundfile as sf		# OpenCVモジュールのimport
```

### 音声の読み込み
```@Python
wave_data, sampling_frequency = sf.read('sample.wav') # 戻り値：音声波形データ，サンプリング周波数
```

### 音声の書き込み
```@Python
sf.write('sample_output.wav',wav_data, fs)
```

# matplotlibの使い方
