# s24002
# 沖縄県の推計人口のページより最新情報をスクレイピングするpythonコード
#　https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html

import requests
from bs4 import BeautifulSoup

uri ='https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

# 文字コードをshift_JISにエンコーディング
html.encoding = 'shift_JIS'

# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
for element in backnumber.find_all('img'):
    print(element)
