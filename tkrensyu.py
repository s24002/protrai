# GUIで動くアプリを作ってみるよ

import tkinter as tk # まずこの行を書く必要があるよ

root = tk.Tk() #始まりのおまじない

root.geometry("2000x1500")# 運動のサイズを決める
root.title("アプリの練習") # ウィンドウのタイトルを決める
lbl = tk.Label(text="こんにちは世界") # いつもの
lbl.pack() # lblを配置させる必要があるよ

root.mainloop() # 終わりのおまじない
