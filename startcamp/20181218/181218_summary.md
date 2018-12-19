안녕하세요



# 181218 수업정리

## 1. 개발환경설정

* chocolatey 
* python -v 3.6.7
* git
  * 머시기 저기시 그렇다
* vscode
* chrome
* vscode 키고 컨트롤 `누른다. 그러면 터미날이 뜬다. 거기다가 python -i 를 입력한다. 그러면 파이썬하듯이 입력 가능하ㅏㄷ. 분할도 가능하다. 여기서 뭐 뭐시기 cd/ 이런거 입력해가지고 python first_python.py같이 입력해서 바로 실행해볼 수도 있다.
* 

## 2. list

### 리스트 만들기, 추출하기 등



```python
>>> mcu
[['ironman', 'captain'], ['xmen', 'deadpool'], ['spiderman']]
>>> family
['mom', 1.64, 'dad', 1.75, 'sister', 1.6]
>>> type(family)
<class 'list'>
>>> type(mcu)
<class 'list'>
>>> family[2]
'dad'
>>> family[5]
1.6
>>> family[-1]
1.6
>>> mcu[2]
['spiderman']
>>> mcu[0[1]]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> mcu[0]
['ironman', 'captain']
>>> mcu[0][1]
'captain'
>>> mcu[2][0]
'spiderman'
>>> disney = mcu[0]
>>> disney[1] = mcu[0][1]
>>> disney[1] == mcu[0][1]
True
>>> mcu[1][1]
'deadpool'
>>> range(1,46)
range(1, 46)
>>> print(range(1, 46))
range(1, 46)
>>> print(list(range(1,46))
...
... asfd
  File "<stdin>", line 3
    asfd
       ^
SyntaxError: invalid syntax
>>> exit()

student@M7037 MINGW64 ~/TIL/startcamp
$ python -i
Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = list(range(1,46))
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
>>> type(rnage(1,46))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rnage' is not defined
>>> type(range(1,46))
<class 'range'>
>>> type(list(range(1,46))
... )
<class 'list'>
>>> type(numbers)
<class 'list'>
>>> int('123')
123
>>> type(int)
<class 'type'>
>>> number = '123'
>>> number = int('123')
>>> type(number)
<class 'int'>
>>> s = int('abc')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'abc'
>>> int(True)
1
>>> int(False)
0
>>> float(100)
100.0
>>> int(100.0)
100
>>> str(100)
'100'
>>> bool(1)
True
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
>>> import random
>>> print(random.sample(numbers, 6))
[21, 42, 6, 26, 31, 19]
>>> print(random.sample(numbers, 6)).sort
[18, 28, 30, 21, 10, 39]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'sort'
'sort'
>>> print(random.sample(numbers, 6)).sort()
[14, 21, 10, 23, 41, 39]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>              'sort'
AttributeError: 'NoneType' object has no attribute
'sort'
>>> print(random.sample(numbers, 6)).sort
[13, 34, 35, 15, 40, 31]
Traceback (most recent call last):                 'sort'
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute  16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,'sort'                                             , 45]
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
>>> numbers = range(1, 100)                         16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,>>> numbers                                        , 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60range(1, 100)                                      3, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 8>>> numbers = list(range(1,100))
>>> numbers
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> numbers[5:10]
[6, 7, 8, 9, 10]
>>> numbers[5::20]
[6, 26, 46, 66, 86]
>>> numbers[2::2:20]
  File "<stdin>", line 1
    numbers[2::2:20]
                ^
SyntaxError: invalid syntax
>>> numbers[0:5]
[1, 2, 3, 4, 5]
```

리스트 공부 했읍니다. 리스트에서 인덱스 번호 0부터 시작한다는거. 리스트 안에 리스트 넣을 수 있다는거. 거기서 인자에 접근하는 방법. `쓰고 다시 닫으면 코드처럼 박스가 생김.

`afsdjlasf`

예를들면 위처럼 나옴.



` 세번치면 박스가 아예 생기고.



1. `[0]`처럼 인덱스 접근
2. `[1:10]`처럼 잘라내기



### 리스트 연산



```python
team = [
    'john',
    10000,
    'neo',
    100,
    'tak',
    40500
]

new_member =['js', 10]

team = team + new_member
print
#리스트끼리 덧셈 연산하면 맨 뒤에 그냥 들어가버림.
#n=0
#n= n+1
#위에 적은 두 줄의 코딩을 귀찮다고 한 줄로 줄여버린 거시 +=임.
#예를 들어 n+=1하면 n=n+1이 되는 것.
```

```python
#리스트에서 인자 제거하기

#여기서 팀은 ['john', 10000, 'neo', 100, 'tak', 40500, 'js', 10] 이렇게.

del(team[2])

print(team)

#이렇게 하면

student@M7037 MINGW64 ~/TIL/startcamp
$ python list1.py
['john', 10000, 100, 'tak', 40500, 'js', 10]

#여러개 지우려면 del(team[2:4]) 이런식으로 하면 된다. 
```



### 리스트 정렬

```python
scores = [45, 60, 78, 88]

high_score = max(scores)

lowest_score = min(scores)

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# full에 first와 second 를 합쳐서 저장

#full_sorted에 full를 정렬해서 저장

# *reverse_sorted에 full을 내림차순으로 정렬해서 저장

full = first + second


>>> asdf = sorted(full_sorted, reverse=True)
>>> asdf
[20.0, 18.0, 11.25, 10.75, 9.5]
>>> *reverse_sorted = asdf
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
>>> reverse_sorted = asdf
>>> reverse_sorte
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reverse_sorte' is not defined
>>> reverse_sorted
[20.0, 18.0, 11.25, 10.75, 9.5]
>>> asdf = sorted(reverse_sorted)
>>> asdf
[9.5, 10.75, 11.25, 18.0, 20.0]
>>> reverse_sorted
[20.0, 18.0, 11.25, 10.75, 

```

변수 앞에 *이 들어가면 안되는거 같은데.....







## 3. dict



```python
hphk = [
    {
        'name':'john'
        'email':'john@naver.com'
    },
    {
        'name': 'tak'
        'email'"'tak@naver.com'
    },
    {
        'name':'neo
        'email':'neo@naver.com'
    }
]

#여기서 neo의 email에 접근하려면?

p = hphk[2]
print(type(p))
print(p['name'])
```

dict는 컬리 브래스킷 {}여기에 넣음녀 되는거. 저렇게 줄 따로 쓰는거랑 한 줄에 쓰는거랑 결과는 같다. hphk는 리스트고 그 안에 있는 게 딕셔너리. 딕셔너리는 key : value로 구성돼있음. key로 value를 부를 수 있음. key에는 string하고 int float 다 들어가긴 함. 근데 key에는 보통 str이 들어감.

## 4. function

## 5. 메서드

메서드는 함수다! 다만 **[주어].동사()**의 형식으로 이루어지며, [주어] 자리에 오는 object들이 할 수 있는 행동(함수)들이다.

```python
>>> samsung = ['elec', 'sds', 's1'] # list
>>>
>>> samsung.index('sds')
1
>>> samsung.count('s1')
1
>>># index 저 요소가 몇번째 있느냐는거고, count는 저 요소가 리스트 안에 몇개 들어있냐는 거임. 저런 식으로 매소드 활용.
>>> lang = 'python'
>>> lang.capitalize()
'Python'
>>> lang
'python' # 첫글자 대문자화
>>>>>> lang.replace('on', 'off')
'pythoff' # on을 찾아 off로 바꿔라
#메서드 활용한다고 해서 원본이 덧씌워지진 않음. 아 물론 예외는 있음. 쓰면 서 외워야함. 대표적으로 sort()가 있음. 소트 쓰면 원본에도 영향이 감.
#append는 더하는 것. 얘는 기억하길.

>>> samsung.append('bio')
>>> samsung
['elec', 'sds', 's1', 'bio']
>>>

```

| str        | int  | list             | bool    | <-- class  |
| ---------- | ---- | ---------------- | ------- | ---------- |
| `'python'` | 100  | `['a', 3, True]` | `False` | <-- object |



### 6. 웹브라우저 키기

```python
import webbrowser

keywords = [
    'i', '1', '2', 'dkdlwmdnjs'
]

for keyword in keywords:
    url = 'https://www.google.com/search?&q=' + keyword
    webbrowser.open_new(url)


#이런식으로 하면 키워드 안에 들어있ㄴㄴ 글자드리 url에 추가되면서 구글이 바로 실행됨. 근데 두번째 인자가 검색이 안되는데 그 이유를 모르겟다.
```



### 7. 로또번호찾기

```python
import random #랜덤 임포트

numbers = list(range(1, 46)) # 45개 숫자 리스트로 만들기

my_numbers = random.sample(numbers, 6) #랜덤으로 뽑기. 중복 없이

print(sorted(my_numbers)) # 정렬해서 프린트.
```

pip -v

pip install requests를 파워셸에 하면 명령이 깔린다. 그걸 임포트함. import requests



```python
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

print(response.text)
```

그리고 url 찾아갖고 api에서 정보 가져와가지고 인증서는 검증 안받고 text만 추출. 시~발

```
print(response.text)
{"totSellamnt":76614176000,"returnValue":"success","drwNoDate":"2018-12-15","firstWinamnt":3144449125,"drwtNo6":45,"drwtNo4":30,"firstPrzwnerCo":6,"drwtNo5":33,"bnusNo":6,"firstAccumamnt":18866694750,"drwNo":837,"drwtNo2":25,"drwtNo3":28,"drwtNo1":2}
```

일케 나옴.

이제 '파싱' 해야함. 쓸모 있는 정보만 또 꺼내오ㅑ야함.

```python
>>> type(response.text)
<class 'str'>
>>> response.json()
{'totSellamnt': 76614176000, 'returnValue': 'success', 'drwNoDate': '2018-12-15', 'firstWinamnt': 3144449125, 'drwtNo6': 45, 'drwtNo4': 30, 'firstPrzwnerCo': 6, 'drwtNo5': 33, 'bnusNo': 6, 'firstAccumamnt': 18866694750, 'drwNo': 837, 'drwtNo2': 25, 'drwtNo3': 28, 'drwtNo1': 2}
>>> type(response.json())
<class 'dict'>
>>>
```

json을 사용했기 때문에 이제서야 쓸모가 있는 data가 됐다고 볼 수 있음.

이제 번호를 뽑자면,

```
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json()

real_numbers = [
    lotto_data['drwtNo1'],
    lotto_data['drwtNo2'],
    lotto_data['drwtNo3'],
    lotto_data['drwtNo4'],
    lotto_data['drwtNo5'],
    lotto_data['drwtNo6'],
]
```

이렇게 하면 번호 여섯개가 나온다~ 이말이야. 지금 real넘버가 딕셔너리라서말이야



저래하고 프린트 리얼 넘버하면 번호가 여섯개가 나온다. 근데 이건 좀 무식한 방법.  더 생각해보고 편한 방법을 찾아보자.

```python
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json() #json 통해서 쓸만한 데이터로 바꾼다.

real_numbers =[] # real_numbers라는 리스트 박스를 만들어 둔다.

for key in lotto_data: # key라는 것이 로또 데이터 안에 있다면 반복
    if 'drwtNo' in key: # drwtNo가 Key에 포함돼 있다면?
        real_numbers.append(lotto_data[key]) #로또데이터가 딕셔너리니까 []안에 key를 넣으면 value가 나옴. 이게 로또 번호니까 이걸 real_numbers에 append하면 되는 것. 6개 다 들어가게 됨.

print(sorted(real_numbers)) # 정렬까지 해서 real_numbers 6글자 뽑아 끝냄.
```

또 다른 방법.



```python
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json()

real_numbers =[]

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)

```

이번엔 for문에 key말고 value까지 한번에 끌고들어오는 모~습. 그래서 바로 value만 어팬드한것.



이제 내가 가진 넘버 3개. 마이 넘버 리얼 넘버 보너스 넘버를 가지고 내가 과연 몇등인지 비교분석하는 코드를 짜보세요(과제)



### 8. 날씨 찾아오기

다크스카이 접속, API 보러 들어가서 로그인. 

00ebc1052d5ab59784ec9067f1763825 내 다크스카이 키



json 크롬 확장 프로그램 설치함.



보기 쉬워짐.



url 얻었으면, 내가 보고 싶은 곳 위도 경도 알아내서 그 뒤에 적고.... 그거 있으면 준비물은 끝났다. 그거로 밑에 코딩.

```python
import requests

url = 'https://api.darksky.net/forecast/00ebc1052d5ab59784ec9067f1763825/37.502909,%20127.039859'

res = requests.get(url)
data = res.json()

print(data['currently']['summary'])
```



이렇게 하면 Mostly Cloudy라고 대답을 준다. 끝.

```python
from darksky import forecast

seoul = forecast('00ebc1052d5ab59784ec9067f1763825', 37.502909 , 127.039859)

print (seoul['currently']['temperature'])
print (seoul['currently']['summary'])
```

이게 이제 pip를 통해서 darkskylib를 받아서 forecast라는 명령어를 받아온 거임. 그래서 시키는대로 내 키, 위도, 경도를 입력해서 데이터를 받아오고, print를 통해서 내가 원하는 정보를 쏙 빼오는 결과를 내는거임. 이렇게 하면,



42.35
Partly Cloudy



이런 결과가 나옴.

### 8. github 아이디만들기, 잔디심기 기초



아이디 생성 후 오늘 했떤거 여차저차 저장 모르겠다 진짜로다가