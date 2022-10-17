# game関連で使うスクリプト集

普段ゲーム開始時に用意する個人的なスクリプト

### game_start.bat  
- game起動時に必要なショートカットを起動
- windowsサウンド変更 スピーカーからヘッドセットへ変更
- pythonで自動tweet

### game_end.bat
- taskkillコマンドで起動中のアプリを終了
- windowsサウンド変更　ヘッドセットからスピーカーへ変更
- pythonで自動tweet
    - 終了時にFirefoxの指定URLページを起動

### game_tweet.py
主に下記の記事を参考にして自動ツイートに成功。  
https://fuyutsuki.net/python-twitter-auto/

### changeSoundDevice.js
ワンクリックでWindowsのサウンドデバイスをスピーカーとイヤホンと変更できる。  
ノートパソコンなら不便に感じないがデスクトップだととても重宝する。  