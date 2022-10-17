import time
import win32gui
import win32.lib.win32con as win32con
import subprocess
import os

def twitch_op():
    os.system("taskkill /im firefox.exe")
    time.sleep(1)

    # ファイルパスを指定して変数へ代入
    firefox = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    subprocess.Popen([firefox,"https://www.yahoo.co.jp/"])

    # アプリを右画面で開く
    time.sleep(2)
    hwnd = win32gui.GetForegroundWindow()
    win32gui.MoveWindow(hwnd, 2000, 50, 1600, 900, True)
    time.sleep(1)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE) 