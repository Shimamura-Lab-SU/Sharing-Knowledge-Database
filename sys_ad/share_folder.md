# Shareフォルダにアクセスできないときの対応

考えられる原因と対策を下に示します．
#### ONLY for Win10 !

## 原因１．Windowsアップデートのせい

Windowsのアップデートにより，ネットワークセキュリティ設定が勝手に変更された可能性があります．  
以下の方法で設定を変更してください．

  1．デスクトップの検索から「Windowsの機能の有効化または無効化」を検索して実行する．  
    <img src="https://cloud-work.jp/wp-content/uploads/2018/01/2018-01-14_153655.png" width="500px">

  2．ウィンドウから「SMB 1.0/CIFSファイル共有のサポート」という項目を探して，**チェックを入れる**．  
    <img src="https://cloud-work.jp/wp-content/uploads/2018/01/2018-01-14_153913.png" width="500px">

  3．OKをクリックすると，自動で設定が行われる．完了後，PCを再起動する．  
    <img src="https://cloud-work.jp/wp-content/uploads/2018/01/2018-01-14_154027.png" width="700px">