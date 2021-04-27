import numpy as np					            						# Numpyモジュールを読み込み
import numpy.fft as fft                         		# Numpyのfftライブラリを読み込み
import matplotlib.pyplot as plt		            			# matplotlibのpyplotライブラリを読み込み

N       = 100                                   		# フィルタ次数(=2N+1)を決めるパラメータ
n       = np.arange(2*N+1)                      		# 添字列 ( 0 <= n <= 2N+1 )
omega_c = np.pi / 4					            						# カットオフ周波数(Radian)
omega_n = 2 * n / (2*N+1)                       		# 正規化角周波数列 ( 0 <= omega_n <= 2 )

####  窓関数を用いない ローパスフィルタ   ####
##      フィルタ係数
h_c = np.zeros([2*N+1])                         		# フィルタ係数の配列
for i in range(2*N+1):                          		# フィルタ係数をsinc関数で定義
    if i != N:
        h_c[i] = 1/ np.array(np.pi * (i-N)) * np.sin(omega_c * (i-N))
    else:
        h_c[i] = omega_c / np.pi

##      周波数特性
T_c     = fft.fft(h_c)                          		# フィルタの周波数特性(FFT)
A_c     = np.abs(T_c)                           		# フィルタの振幅特性
P_c     = np.unwrap(np.angle(T_c))              		# フィルタの位相特性

##      プロット１
fig1, ax1 = plt.subplots(2, 1, constrained_layout=True)	# 2行1列のグラフウィンドウ作成
#   ローパスフィルタ(窓関数なし)の振幅特性
ax1[0].plot(omega_n, A_c,'r')                   		# 横軸を omega_n として A_c をプロット
ax1[0].set_xlim(0, 1); ax1[0].set_ylim(0, 1.25) 		# x軸，y軸の表示範囲を指定
ax1[0].set_title('Amplitude Characteristics')
ax1[0].set_xlabel('Angular Frequency (×π)');  ax1[0].set_ylabel('Amplitude')
#   ローパスフィルタ(窓関数なし)の位相特性
ax1[1].plot(omega_n,P_c,'r')                    		# 横軸を omega_n として P_c をプロット
ax1[1].set_xlim(0, 1); ax1[1].set_ylim(-80,0)   		# x軸，y軸の表示範囲を指定
ax1[1].set_title('Phase Characteristics')
ax1[1].set_xlabel('Angular Frequency (×π)');  ax1[1].set_ylabel('Phase [rad]')

####  窓関数を用いた ローパスフィルタ  ####
##      フィルタ係数
w       = 0.54 + 0.46 * np.cos( (n-N) * np.pi / N ) # 窓関数 (ハミング窓)
h_cw    = w * h_c

##      周波数特性
T_cw    = fft.fft(h_cw)                         		# フィルタの周波数特性(FFT)
A_cw    = np.abs(T_cw)                          		# フィルタの振幅特性
P_cw    = np.unwrap(np.angle(T_cw))             		# フィルタの位相特性

##      プロット２
fig2, ax2 = plt.subplots(2, 1, constrained_layout=True)	# 2行1列のグラフウィンドウ作成
#   ローパスフィルタ(窓関数あり)の振幅特性
ax2[0].plot(omega_n, A_cw)                      		# 横軸を omega_n として A_cw をプロット
ax2[0].set_xlim(0, 1); ax2[0].set_ylim(0, 1.25) 		# x軸，y軸の表示範囲を指定
ax2[0].set_title('Amplitude Characteristics')				# 図のタイトル
ax2[0].set_xlabel('Angular Frequency (×π)');  ax1[0].set_ylabel('Amplitude')
#   ローパスフィルタ(窓関数あり)の位相特性
ax2[1].plot(omega_n, P_cw)                      		# 横軸を omega_n として P_cw をプロット
ax2[1].set_xlim(0, 1); ax2[1].set_ylim(-90,0)   		# x軸，y軸の表示範囲を指定
ax2[1].set_title('Phase Characteristics')						# 図のタイトル
ax2[1].set_xlabel('Angular Frequency (×π)');  ax1[1].set_ylabel('Phase [rad]')
plt.show()

