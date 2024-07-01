# s24002
# エントリーウィジェットで受け付けた金額を税込み(10%)価格として出力するプログラムを作成してください

import tkinter as tk # tkinterをtk と略して使用する
def dispLabel():
    # entryメゾットを使用して入力を受け付け変数aに格納
     a = entry.get()
     print(f"aは{type(a)}")
     lbl.config(text=f"{a}さんこんにちは")

# print("金額を入力してください")
# a = int(input())
# print(type(a))

root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200") # 画面の大きさを決める

lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font=('Helvetica', 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()


tk.mainloop()
