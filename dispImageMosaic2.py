# s24002 dispImagekadai.py
# モノクロ画像に変換
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(pash):

    # 画像を読み込んでグレースケールに変換
    newImage = PIL.Image.open(pash).convert("L")\
    .resize((300, 300)).rotate(90)\
    .transpose(PIL.Image.FLIP_LEFT_RIGHT)\
    
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel .configure(image = imageData)
    imageLabel.image = imageData
    lbl2 = tk.Label(text=pash, font=("Helvetica", 16))
    lbl2.pack()

def openfile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)

root = tk.Tk()
root.geometry("600x450")

btn = tk.Button(text="ファイルを開く", command = openfile)
# lbl2=tk.Label(text="path")
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
# lbl2.pack()
tk.mainloop()
