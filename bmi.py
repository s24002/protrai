# s24002
# BMI値計算プログラム　ファイル名は「bmi.py」

h = float(input('身長何㎝ですか？')) 
w = float(input('体重何kgですか？'))

bmi = w / (h + w)
print("あなたのBMI値は、",bmi,"です。")
