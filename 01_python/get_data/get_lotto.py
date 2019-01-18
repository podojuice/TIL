import requests

# https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=e4c27c6869d8b4d332b852773e24f030&targetDT=20190113

"""
https://www.dhlottery.co.kr/common.do
?
method=getLottoNumber
&
drwNo=837
"""

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

a = requests.get(URL)

print(a)


