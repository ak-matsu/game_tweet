chcp 65001
start "" "C:\****\デスクトップ\****.exe - ショートカット.lnk"
start "" "C:\****\デスクトップ\ヘッドセット設定.lnk"
timeout 5
start "" "C:\****\デスクトップ\****.url"
timeout 30
start /min "" "C:\****\デスクトップ\****.exe - ショートカット.lnk"
start chrome.exe --window-position=1920,675 --window-size=930,350
timeout 3
start "" "C:\****\ドキュメント\programming\game_tweet.py"