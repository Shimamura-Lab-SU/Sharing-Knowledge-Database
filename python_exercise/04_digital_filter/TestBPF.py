from TestLPF import *                           		# TestLPF.py (ローパスフィルタ)を実行する
# 注意 : 表示されるグラフウィンドウを消すと以降のソースを実行できる．

##      フィルタ係数
omega_0 = 1/2 * np.pi                           		# バンドパスフィルタの中心周波数
h_lp    = h_cw                                  		# ローパスフィルタの係数をコピー
h_bp    = np.real(h_lp * np.exp(1j*omega_0*n))  		# 中心周波数の分だけ周波数シフト，ただし実部だけ取り出す．
h_bp    = 2 * h_bp                              		# 虚部を無視した分，２倍に

##      周波数特性
T_bp    = fft.fft(h_bp)                         		# フィルタの周波数特性(FFT)
A_bp    = np.abs(T_bp)                          		# フィルタの振幅特性
P_bp    = np.unwrap(np.angle(T_bp))             		# フィルタの位相特性

##      プロット１
fig, ax = plt.subplots(2, 1, constrained_layout=True)   # 2行1列のグラフウィンドウ作成
#   バンドパスフィルタの振幅特性
ax[0].plot(omega_n, A_bp)                       		# 横軸を omega_n として A_bp をプロット
ax[0].set_xlim(0, 1); ax[0].set_ylim(0, 1.25)   		# x軸，y軸の表示範囲を指定
ax[0].set_title('Amplitude Characteristics')				# 図のタイトル
ax[0].set_xlabel('Angular Frequency (×π)');  ax1[0].set_ylabel('Amplitude')
#   バンドパスフィルタの位相特性
ax[1].plot(omega_n, P_bp)                       		# 横軸を omega_n として P_bp をプロット
ax[1].set_xlim(0, 1); ax[1].set_ylim(-170,20)   		# x軸，y軸の表示範囲を指定
ax[1].set_title('Phase Characteristics')						# 図のタイトル
ax[1].set_xlabel('Angular Frequency (×π)');  ax1[1].set_ylabel('Phase [rad]')
plt.show()


