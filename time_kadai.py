# s24002
# labelの使い方と時計の表示方法
# 実行が確認出来たら時間を表示させる「時計アプリ」を作ってみたいと思います
# 時計アプリはモジュール名「time_kadai.py」で作成します
#

import datetime
import tkinter as tk # GUIでアプリを作ることができるモジュール


# 時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m%d日　%H時%M分%S秒")
    #
    lbl.config(text=current_time)
    root.after(1000,update_time)

# tkinterのウィンドウを作成
root = tk.Tk() # 初めのおまじない

root.title("あまり見ない時計")
#　
lbl = tk.Label()
lbl.config(text="", font=("Helvetica, 100"))
lbl.pack()
# 関数の呼び出し
update_time()
    
root.mainloop() # 終わりのおまじない
