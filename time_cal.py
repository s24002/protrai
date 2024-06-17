# s24002
# 現在の時刻と2024年のカレンダーを表示するプログラム
#

import calendar as cal
print(cal.month(2024,7))
import datetime
now = datetime.datetime.now()
print(now)
now.strftime("%Y年%m月%d日 %H:%M:%S")
