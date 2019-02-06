import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from temper_prj import get_weather

air_key = 'FKCdgbAO7HrrHnLRueGT45kJ46LSeQZ3W6DH4cDlHj7fYP1G4a9lt5rk54MXSc9sTiobJcdfb8LZG7u1XSnPig%3D%3D'
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?sidoName=%EC%84%9C%EC%9A%B8&searchCondition=DAILY&pageNo=2&numOfRows=20&ServiceKey={air_key}'

raw_data = requests.get(url)

data = BeautifulSoup(raw_data.text, 'html.parser')

city = data.find_all("cityname")
pm10value = data.find_all("pm10value")
pm25value = data.find_all("pm25value")
datatime = data.find_all('datatime')

# PM 10 좋음 0~30 보통 ~ 80 나쁨 ~150 매우나쁨 150~
# PM 25 좋음 0~ 15 보통 ~ 35 나쁨 ~75 매우나쁨 76~

def pm10_check(location):
    for idx, i in enumerate(city):
        if location in i:
            idx= idx
            break
    pm10 = int(str(pm10value[idx])[11:-12])
    datatime = str(data.find_all('datatime')[idx])[21:26]

    if pm10 > 150:
        return f'{location}의 {datatime}시 미세먼지 수치는 {pm10}, \'매우나쁨\'입니다.'
    elif pm10 > 80:
        return f'{location}의 {datatime}시 미세먼지 수치는 {pm10}, \'나쁨\'입니다.'
    elif pm10 > 30:
        return f'{location}의 {datatime}시 미세먼지 수치는 {pm10}, \'보통\'입니다.'
    else:
        return f'{location}의 {datatime}시 미세먼지 수치는 {pm10}, \'좋음\'입니다.'
    
def pm25_check(location):
    for idx, i in enumerate(city):
        if location in i:
            idx= idx
            break
    pm25 = int(str(pm25value[idx])[11:-12])
    datatime = str(data.find_all('datatime')[idx])[21:26]
    if pm25 > 75:
        return f'{location}의 {datatime}시 초미세먼지 수치는 {pm25}, \'매우나쁨\'입니다.'
    elif pm25 > 35:
        return f'{location}의 {datatime}시 초미세먼지 수치는 {pm25}, \'나쁨\'입니다.'
    elif pm25 > 15:
        return f'{location}의 {datatime}시 초미세먼지 수치는 {pm25}, \'보통\'입니다.'
    else:
        return f'{location}의 {datatime}시 초미세먼지 수치는 {pm25}, \'좋음\'입니다.'
    
loca = '강남구'


print(pm10_check(loca), pm25_check(loca), get_weather(loca))