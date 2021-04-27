from TestLPF import *                           		# TestLPF.py (ローパスフィルタ設計)を実行する
# 注意 : 表示されるグラフウィンドウを消すと以降のソースを実行できる．

import scipy.signal as sg                       		# Scipyのsignalライブラリを読み込み，sgと名付ける

##      合成正弦波信号の作成
x       = 1.0*np.sin(np.pi/6*n) + 0.5*np.sin(np.pi/2*n)   # 正弦波の周波数：π/6，π/2
##      信号の時間領域におけるフィルタリング
y       = sg.convolve(h_cw,x)                   		# 時間領域でフィルタ係数を畳み込み
M_x = len(x); M_y = len(y)
T_x     = fft.fft(x, 2*M_x)                     		# 入力信号 x のFFT
A_x     = np.abs(T_x)                           		# フィルタの振幅特性
P_x     = np.unwrap(np.angle(T_x))              		# フィルタの位相特性
T_y     = fft.fft(y, 2*M_y)                     		# 出力信号 x のFFT
A_y     = np.abs(T_y)                           		# フィルタの振幅特性
P_y     = np.unwrap(np.angle(T_y))              		# フィルタの位相特性
##      信号の周波数領域におけるフィルタリング
yf      = fft.ifft(fft.fft(x, 2*M_x) * fft.fft(h_cw, 2*M_x))	# 周波数領域でフィルタ係数を乗算
yf      = np.real(yf)                           		# FFT -> IFFT での虚数成分誤差を除去

omega_nx = 2 * np.arange(2*M_x) / (2*M_x)						# 正規化角周波数 (A_x表示用)
omega_ny = 2 * np.arange(2*M_y) / (2*M_y)						# 正規化角周波数 (A_y表示用)

##      プロット１
fig1, ax1 = plt.subplots(2, 1, constrained_layout=True)  # 2行1列のグラフウィンドウ作成
#   入力信号の振幅特性
ax1[0].plot(omega_nx, A_x)                      		# 横軸を omega_nx として A_x をプロット
ax1[0].set_xlim(0, 1)                           		# x軸の表示範囲を指定
ax1[0].set_title('Amplitude Characteristics for Input')
ax1[0].set_xlabel('Angular Frequency (×π)');  ax1[0].set_ylabel('Amplitude')
#   出力信号の振幅特性
ax1[1].plot(omega_ny, A_y)                      		# 横軸を omega_ny として A_y をプロット
ax1[1].set_xlim(0, 1)																# x軸の表示範囲を指定
ax1[1].set_title('Amplitude Characteristics for Output')	# 図のタイトル
ax1[1].set_xlabel('Angular Frequency (×π)');  ax1[1].set_ylabel('Amplitude')

##      プロット２
fig2, ax2 = plt.subplots(2, 1, constrained_layout=True)  # 2行1列のグラフウィンドウ作成
#   入力信号波形
ax2[0].plot(x)
ax2[0].set_xlim(0, 2*N)															# x軸の表示範囲を指定
ax2[0].set_title('Waveform for Input')
ax2[0].set_xlabel('Angular Frequency (×π)');  ax2[0].set_ylabel('Value')
#   出力信号波形(時間領域フィルタリング)
ax2[1].plot(y)
ax2[1].set_xlim(0, 2*N)															# x軸の表示範囲を指定
ax2[1].set_title('Waveform for Output')							# 図のタイトル
ax2[1].set_xlabel('Angular Frequency (×π)');  ax1[1].set_ylabel('Value')

##      プロット３
fig3, ax3 = plt.subplots(2, 1, constrained_layout=True)  # 2行1列のグラフウィンドウ作成
#   入力信号波形
ax3[0].plot(x)
ax3[0].set_xlim(0, 2*N)															# x軸の表示範囲を指定
ax3[0].set_title('Waveform for Input')							# 図のタイトル
ax3[0].set_xlabel('Angular Frequency (×π)');  ax1[0].set_ylabel('Value')
#   出力信号波形(周波数領域フィルタリング)
ax3[1].plot(yf)
ax3[1].set_xlim(0, 2*N)															# x軸の表示範囲を指定
ax3[1].set_title('Waveform for Output')							# 図のタイトル
ax3[1].set_xlabel('Angular Frequency (×π)');  ax1[1].set_ylabel('Value')

plt.show()