# 停電時のメールサーバの停止・起動について

現在，研究室のメール(@sie.ics.saitama-u.ac.jp)に関する設定は，研究室内に設置したメールサーバで直接に，一元的に管理しています(学科のサーバで管理してないので，技官さんは関係ありません)．停電時には，メールサーバから設定をいじってください．

## 何をすればいい？

当研究室ではメール用ソフトウェアとして **Postfix** を使用しています．
大学停電時には，Postfixを停止させ，電源をオフにしてください．
また復電後は早急にサーバを立ち上げ，Postfixを起動させてください．

## サーバの停止・起動方法



### 1. メールサーバの停止

まずターミナル(CentOSでは"端末"という名称)を立ち上げ，root権限でログインしてください．
次に，`/etc/init.d/postfix stop`でpostfixを停止してください．

```
[sys_ad@ ~]$ su                                 < Enter, ルートアカウントでログイン
Password:　                                     < rootアカウントのパスワードを入力
[root@ ~]$ /etc/init.d/postfix stop             < Enter, Postfixを停止
Shutting down postfix:　　　　[　OK　]
```
※ "<" 以降はコメント．入力しないでね．

### 2. メールサーバの起動

同じくターミナル(CentOSでは"端末"という名称)を立ち上げ，root権限でログインしてください．
次に，`/etc/init.d/postfix start`でpostfixを起動してください．
最後に，`/etc/init.d/postfix reload`でpostfixの設定ファイルを再読み込みします．

```
[sys_ad@ ~]$ su                                 < Enter, ルートアカウントでログイン
Password:　                                     < rootアカウントのパスワードを入力
[root@ ~]$ /etc/init.d/postfix start            < Enter, Postfixを起動
Starting postfix::　　　      　[　OK　]
[root@ ~]$ /etc/init.d/postfix reload           < 設定のリロード
```
※ "<" 以降はコメント．入力しないでね．

以下のコマンドでpostfixの状態を確認できます．

```
[sys_ad@ ~]$ /etc/init.d/postfix status         < Enter, 状態を確認
master(ID:~~~~)は起動中．
```
※ "<" 以降はコメント．入力しないでね．


### 3. 他の Postfix に関する命令

ターミナルで実行します．基本的にルート権限でしか命令を実行できません．

- **`/etc/init.d/postfix status`** : Postfix の状態を確認
- **`/etc/init.d/postfix start`** : Postfix を起動
- **`/etc/init.d/postfix stop`** : Postfix を停止
- **`/etc/init.d/postfix restart`** : Postfix を再起動
- **`/etc/init.d/postfix reload`** : Postfix の設定ファイルを再読み込み
