# s24002
# おみくじプログラム　モジュール名「omikuji_tk.py」

import random # s24002
# すごくどうしようもないプログラム
root.geometry("700x500")
lbl = tk.Label(text="運試し")
lbl = tk.title("おみくじ")
kuji = ["大吉", "中吉", "小吉", "凶","大凶"]
print(random.choice(kuji))
