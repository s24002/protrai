# s24002
# 現在の時刻と2024年のカレンダーを表示するプログラム
#

def time_cal():
    import detetime
    n = detetime.datetime.now
    d = n.strftime("%Y年%m月%d日 %H:%M:%S")
    import calender as cal
    c= cal.month(2024,7)
    print(d)
    print(c)
    return

