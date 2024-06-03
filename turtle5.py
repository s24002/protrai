# turtle.py

from turtle import * #タートルグラフィックスを使う準備

shape("turtle") # カメの登場

col = ["red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue"]
for i in range(20):
    color(col[i])
    circle(100) 
    left(35)
    
    
done() #おしまい

