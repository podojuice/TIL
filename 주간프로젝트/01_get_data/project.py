import requests

import os


#영진위에서 지난 10주차 영화 정보 긁기

KOBIS_key=os.getenv('KOBIS_KEY')


week = ['20181111', '20181118', '20181125', '20181202', '20181209', '20181216', '20181223', '20181230', '20190106', '20190113']

results={}
for i in week:
    URL = f'https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={KOBIS_key}&targetDt={i}&weekGb=0'
    raw_data = requests.get(URL)
    data = raw_data.json()
    data = data['boxOfficeResult']['weeklyBoxOfficeList']
    for j in range(10):
        
        results[data[j]['movieNm']] = {
        'movieCd' : data[j]['movieCd'],

        'audiAcc' : data[j]['audiAcc'],
        'date' : str(i)
        }


#긁어온 정보를 바탕으로 정보 적힌 boxoffice.csv파일 만들기.

import csv

f = open('boxoffice.csv', 'w+', encoding='utf-8', newline = '')

writer = csv.writer(f)

writer.writerow(
        ['영화 코드', '영화명', '누적 관객수', '기준일']
    )

f.close()


f = open('boxoffice.csv', 'a+', encoding='utf-8', newline = '')

writer = csv.writer(f)

for k, v in results.items():
    writer.writerow(
        [results[k]['movieCd'], k, results[k]['audiAcc'], results[k]['date']]
    )

f.close()


#movie_code 따로 정리.

movie_code=[]
for i in results:
    movie_code += [results[i]['movieCd']]


# 디테일한 정보를 받아오자. 딕셔너리 안에 url 통해 데이터 받아오고, 여러가지 정보를 저장한다.

detail_result = {}
for x in movie_code:
    detail_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={KOBIS_key}&movieCd={x}'

    detail_raw_data = requests.get(detail_url)
    detail_data=detail_raw_data.json()

    detail_data = detail_data['movieInfoResult']['movieInfo']

        

    detail_result[detail_data['movieNm']] = {
        'movieCd' : detail_data['movieCd'],
        'movieNm' : detail_data['movieNm'],
        'movieNmEn' : detail_data['movieNmEn'],
        'movieNmOg' : detail_data['movieNmOg'],
        'openDt' : detail_data['openDt'],
        'showTm' : detail_data['showTm'],
        'genres' : detail_data['genres'][0]['genreNm'],
        'directors' : detail_data['directors'][0]['peopleNm'],
        'watchGradeNm' : detail_data['audits'][0]['watchGradeNm'],
        'actors' : detail_data['actors']
    }

# 이번엔 movie.csv라는 데 세부 정보 저장한다. 배우 수가 적은 영화가 있어 배우 수마다 조건을 따로 줬다.

fd = open('movie.csv', 'w+', encoding='utf-8', newline = '')

writer_fd = csv.writer(fd)

writer_fd.writerow(['영화 코드', '영화명', '영문명', '원문명', '개봉일', '러닝타임', '장르', '감독', '등급', '배우1', '배우2', '배우3'])

f.close()

fd = open('movie.csv', 'a+', encoding='utf-8', newline = '')
writer_fd = csv.writer(fd)
for k in detail_result:
    if len(detail_result[k]['actors']) >= 3:
        writer_fd.writerow(
            [detail_result[k]['movieCd'], detail_result[k]['movieNm'], detail_result[k]['movieNmEn'], detail_result[k]['movieNmOg'], detail_result[k]['openDt'], detail_result[k]['showTm'], detail_result[k]['genres'], detail_result[k]['directors'], detail_result[k]['watchGradeNm'], detail_result[k]['actors'][0]['peopleNm'], detail_result[k]['actors'][1]['peopleNm'], detail_result[k]['actors'][2]['peopleNm'] ]
        )
    elif len(detail_result[k]['actors']) == 2:
        writer_fd.writerow(
            [detail_result[k]['movieCd'], detail_result[k]['movieNm'], detail_result[k]['movieNmEn'], detail_result[k]['movieNmOg'], detail_result[k]['openDt'], detail_result[k]['showTm'], detail_result[k]['genres'], detail_result[k]['directors'], detail_result[k]['watchGradeNm'], detail_result[k]['actors'][0]['peopleNm'], detail_result[k]['actors'][1]['peopleNm'] ]
        )
    elif len(detail_result[k]['actors']) == 1:
        writer_fd.writerow(
            [detail_result[k]['movieCd'], detail_result[k]['movieNm'], detail_result[k]['movieNmEn'], detail_result[k]['movieNmOg'], detail_result[k]['openDt'], detail_result[k]['showTm'], detail_result[k]['genres'], detail_result[k]['directors'], detail_result[k]['watchGradeNm'], detail_result[k]['actors'][0]['peopleNm'] ]
        )
    elif len(detail_result[k]['actors']) == 0:
        writer_fd.writerow(
            [detail_result[k]['movieCd'], detail_result[k]['movieNm'], detail_result[k]['movieNmEn'], detail_result[k]['movieNmOg'], detail_result[k]['openDt'], detail_result[k]['showTm'], detail_result[k]['genres'], detail_result[k]['directors'], detail_result[k]['watchGradeNm'], '' ]
        )

f.close()

#영화 이름이 담긴 리스트도 따로 정리했다.

movies = []
for i in detail_result:
    movies += [i]
    
movies

# 영진위 영화 대표 코드, 영화 썸네일 이미지 URL, 하이퍼 텍스트 링크, 유저 평점 등을 네이버에서 긁어왔다.

from time import sleep 

naver_uri = 'https://openapi.naver.com/v1/search/movie.json?query='


client_id = os.getenv('NAVER_ID')
client_secret = os.getenv('NAVER_SECRET')
headers = {
    'X-Naver-Client-Id': client_id, 
    'X-Naver-Client-Secret': client_secret

}

link_data = []

for y in range(len(movies)):
    res = requests.get(naver_uri + movies[y], headers = headers)
    link_data += [res.json()]

    sleep(0.05)

#긁어온 정보 중 movie_info라는 딕셔너리를 만들어 필요한 것만 정리했다.

movie_info = {}

for i in range(len(movies)):
    movie_info[link_data[i]['items'][0]['title']] = {
        'name': movies[i],
        'code' : movie_code[i],
        'link' : link_data[i]['items'][0]['link'],
        'image' : link_data[i]['items'][0]['image'],
        'userRating': link_data[i]['items'][0]['userRating']
        
    }

# movie_naver.csv에 필요한 정보 저장.

fl = open('movie_naver.csv', 'w+', encoding='utf-8', newline = '')

writer_fl = csv.writer(fl)

writer_fl.writerow(['영화 코드', '이미지 URL', '하이퍼텍스트 Link', '유저 평점'])

fl.close()


fl = open('movie_naver.csv', 'a+', encoding='utf-8', newline = '')

writer_fl = csv.writer(fl)
for i in movie_info:
    writer_fl.writerow([movie_info[i]['code'], movie_info[i]['image'], movie_info[i]['link'], movie_info[i]['userRating']])

fl.close()

#wb 옵션으로 영화 코드가 이름인 썸네일 이미지들을 현재 디렉토리에 저장.

for i in movie_info:
    img_data = requests.get(movie_info[i]['image']).content
    with open(movie_info[i]['code'] + '.jpg', 'wb') as f:
        f.write(img_data)