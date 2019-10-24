# What's Spectrogram-Viewer

wavファイルのスペクトルを**無料**で見るための最強ツール．
今のところ**wavファイル**のみ対応(たぶん今後も他の形式は実装しない)．

# How to Use

 - ### Drag & Dropでwavファイルの波形，スペクトログラムを表示
 - ### 拡大，縮小，移動，スナップショット機能あり
   詳しい使い方はこちらから [https://help.plot.ly/zoom-pan-hover-controls/](https://help.plot.ly/zoom-pan-hover-controls/)
 - ### トグルボタンから横軸の尺度，縦軸のスケールを変更可能
   - Time-Scale : 横軸を `時間[s]`か`サンプル数`か変更可能．
   - Frequency-scale : スペクトログラムの縦軸を `リニアスケール`か`対数スケール`か変更可能．
   <img src="https://github.com/Shimamura-Lab-SU/Sharing-Knowledge-Database/blob/master/options.png" width="150px">

# サーバー側の設定メモ

## インストールする Python パッケージ

- numpy
- ccfi
- pysoundfile
- librosa
- scipy
- dash
- dash-daq
- Flask
- gunicorn


## Webアプリの起動法

以下のコマンドを入力．
```
gunicorn -b [IP]:8000 spectrogram_plot:server
```
