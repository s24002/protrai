# 画像表示アプリ バージョン2.0
# dispImagekadai.py
# s24002
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(pash):

    # 画像を読み込んでモザイクに変換
    newImage = PIL.Image.open(pash).convert("L").resize((32,32)).resize((300, 300))
    
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel .configure(image = imageData)
    imageLabel.image = imageData
    lbl2 = tk.Label(text=path, font=("Helvetica", 16))
    lbl2.pack

def openfile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("520x400")

btn = tk.Button(text="ファイルを開く", command = openfile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()
