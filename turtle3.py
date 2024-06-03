# turtle.py

from turtle import * #タートルグラフィックスを使う準備

shape("turtle") # カメの登場

col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    circle(100) #半径100の円を描くこと
    left(72) #左に72度曲がること
    
    
done() #おしまい

