# 181219 수업정리

## 중요한 것들

애드 커밋 푸시

git add . 하면 내 상태를 잠깐 진정 시키는 거임. 아직 올린 상태 아님

커밋해야 사진을 찍는거고,

푸시해야 진정 깃에 사진 올라가는 거임.

git status 하면 뭐가 없어졌고 뭐가 바꼈고 알려줌.

git commit -m '~~'  (깃 커밋이고 -m 뒤에는 메세지 쓰는거임.)

git log - 사진첩임.



google momentum 확장프로그램 이거 내가 옛날부터 찾던거다 이거. 와 반가워



확장프로그램중에 json이랑 onetab배웟따. onetab은 탭 모아서 보게 해주는 것.

json은 프로그래밍언어 좀 보기 편하게 바꿔주는 거.

cloud9 / github 사이트 가입. 둘이 연동함.



둘다 유저네임 podojuice임.



'codecademy'에 로그인해서 html 기초에 대해서 수강해오기.(과제)



bootstrap(포폴이쁘게만드는곳)



https://my-portfolio-podojuice.c9users.io/index.html



내가 만든 포폴 사이트임 (부트스트랩으로)



마크다운으로 문서 이쁘게 쓸 수 있음



https://github.com/podojuice/podojuice.github.io 내 깃스타그램

https://podojuice.github.io/

깃헙에 호스팅한 내 포폴 사이트.

카카오 기술 블로그도 이걸로 만듬



```
git remote add origin https://github.com/podojuice/podojuice.github.io.git
```

이거 리모트 ...몰라

## 1. morning quiz 평균

오늘 수업의 중점은 먼저 평균 구하기.

```python
# 1. 평균을 구하시오



my_score = [79, 84, 66, 93]

my_average = sum(my_score, 0.0)/len(my_score) #이거 타입은 float여야함.

print(my_average)


your_score ={
    '수학':87,
    '국어':83,
    '영어':76,
    '도덕':100
}
# your_average #얘 역시 float 클래스여야.
your_score=your_score.values()
your_average = sum(your_score)/len(your_score)
print(type(your_score))
print(your_score)
print(your_average)
```



80.5
<class 'dict_values'>
dict_values([87, 83, 76, 100])
86.5



이런 결과값이 나온다. 인자를 다 더하는데, 그걸 float(실수)로 바꿔주고, len을 통해 인자 수를 구한 다음 나누면 평균이 나온다.

딕셔너리 value는 어떻게 할까?. 벨류를 빼가지고 더하고, 인자 수로 나눈다. 그러면 평균값 구하기가 됨. 밸류 뺀건 dict_values라는 클래스로 나옴. 이건 리스트가 아니다(??)



## 2. morning quiz 도시별 평균 온도

```python
cities={
    '서울':[-6,-10,5],
    '대전':[0,-5,2],
    '광주':[0,-5,10],
    '구미':[2,-2,9]
}


cities_tem=cities.values()   #cities라는 딕셔너리에 있는 벨류를 빼냄
list_tem=list(cities_tem)    #빼낸 밸류를 리스트화

var1=[0,1,2,3]   #리스트에 인자가 4개 이쓰니 인덱스를 직접 지정해줬음. 이거 따로 빼는 방법알면 좋을듯.
var2=cities.keys() # cities의 키를 빼냄.

var2=list(var2) #cities에서 빼낸 키를 리스트화

for i in var1:
    print(var2[i],':',round(sum(list_tem[i])/len(list_tem[i]),2))

    #cities의 키, 그리고 소숫점, 더하고, 인자 수로 나누면, 평균이 나온다!
```

cities가 저렇게 딕셔너리로 지정돼있으면, 어떻게 각 도시의 평균 온도를 구할 수 있을까? 가 핵심.



내가 짠 코드다. 먼저, cities에 있는 밸류 빼내고, 빼낸 밸류를 리스트화한다.



뭐 주석처리하고 쭉쭉써놨으니 이해는 되겄지만, 인덱스를 직접 내가 0,1,2,3으로 지정한게 아쉬울 따름. 그 외에는 잘 짠 것 같다.



### 가장 더운 날씨를 가진 곳, 가장 추운 날씨를 가진 곳 찾기(1차)

```python
ity_key=cities.keys() #역시 cities의 키를 뺌

city_list=list(city_key) # 리스트화

city_values=cities.values() #밸류 뺌

val1=list(city_values) # 리스트화
var=[0,1,2,3] # 아까처럼 인덱스 수 만큼 인덱스 지정

hot=[] #변수 리스트 생성

cold=[] #역시 변수 리스트 생성

for i in var:
    hot.append(max(val1[i]))

    #i 가 0~3을 돌면서 val1에 있는 cities의 밸류 중 max 값을 hotandcold에 저장.

for i in var:
    cold.append(min(val1[i]))

    #i 가 0~3을 돌면서 val1에 있는 cities의 밸류 중 min 값을 coldandhot에 저장.

print('Hottest:',city_list[hot.index(max(hot))])

#hot리스트에서 맥스 값의 인덱스를 다시 city_list에 넣으면, 가장 뜨거웠던 날이 존재했던 도시가 출력되겄쥬

print('Coldest:',city_list[cold.index(min(cold))])

#cold리스트에서 min 값의 인덱스를 다시 city_list에 넣으면, 가장 추웠던 날이 존재했던 도시가 출력되겄쥬


```

읽으면 뭔 소린 줄 알겠으나, 너무 코드가 더럽다. 인덱스 역시 따로 지정한 게 존ㄴ ㅏ별로.



### 가장 더운 날씨를 가진 곳, 가장 추운 날씨를 가진 곳 찾기(2차)



```python
cities_temp={
    '서울':[-6,-10,5],
    '대전':[0,-5,2],
    '광주':[0,-5,10],
    '구미':[2,-2,9]
}

city_key=cities_temp.keys()

city_list=list(city_key)

hot=[]
cold=[]

for key, value in cities_temp.items():
    hot.append(max(value))
    cold.append(min(value))

print('Hottest:', city_list[hot.index(max(hot))])
print('coldest:', city_list[cold.index(min(cold))])
```

선생님의 조언을 듣고 다시 만들어본 것. 이번엔 좀 나아진 것 같다.



cities_temp에서 키를 뺀다. 그리고 리스트화를 한다.



hot, cold라는 빈 리스트를 만들고,



for 문을 통해 키와 밸류를 기준으로 돌린다. value 중에 가장 큰 것을 hot리스트에 어팬드 한다. 역시 가장 낮은 온도를 cold에 어팬드한다.



프린트문을 통해서 각 도시 별 가장 높았던 온도 중에서도 가장 높은 온도의 인덱스를 city_list에 적용하면, 그 도시가 나오는 구조.



다 좋은데, 만약 중복되는 온도를 가진 도시가 있었다면 이 코드는 무용지물.



### morning quiz 선생님의 정답.



```python
# 3: 도시별 평균 온도
#출력값은 서울:?
#대전:?
#광주:?
#구미:?

cities_temp={
    '서울':[-6,-10,5],
    '대전':[0,-5,2,10],
    '광주':[0,-5,10],
    '구미':[2,-2,9]
}

for city, temperatures in cities_temp.items(): #키와 밸류를 한번에 꺼내려면 이런식으로 뒤에 items()를 적어주면 된다.!
    print(city , ':' + str(round(sum(temperatures)/len(temperatures),2)))


for city in cities_temp:
    temperatures = cities_temp[city] #얘는 밸류를 안꺼내고 키만 꺼냈으니, 이번 줄을 통해서 밸류를 따로 꺼내준다.
    avg_tempertures = round(sum(temperatures)/len(temperatures),2)
    print(city , avg_tempertures)
    print(city + ':' + str(avg_tempertures)) #str이랑 int랑 같이 쓸 수 없다나? 그래서 str로 바꿔준 것.
    print('{0}:{1}'.format(city, avg_tempertures)) #이거는 다 문자열 취급을 하되, 문자열안에 중괄호는 format 메서드를 통해서 함수에 활용가능


#4 도시중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳.
#Hottest:?? , coldest:??

#교수님 정답
#all_temp모든 기온을 모은다

all_temp=[]
for key, value in cities_temp.items():
    all_temp += value

print(all_temp)

highest = max(all_temp)
lowest = min(all_temp)
print(highest,lowest)

hottest =[]
coldest =[]

for key, value in cities_temp.items():
    if highest in value:
        hottest.append(key)
    if lowest in value:
        coldest.append(key)

#all_temp에서 higheset/lowest를 찾는다

#cities_temp에서 highest/lowest가 속한 도시를 찾는다. 

print('hottest',hottest)
print('coldest',coldest)

```

서울 :-3.67
대전 :1.75
광주 :1.67
구미 :3.0
서울 -3.67
서울:-3.67
서울:-3.67
대전 1.75
대전:1.75
대전:1.75
광주 1.67
광주:1.67
광주:1.67
구미 3.0
구미:3.0
구미:3.0
[-6, -10, 5, 0, -5, 2, 10, 0, -5, 10, 2, -2, 9]
10 -10
hottest ['대전', '광주']
coldest ['서울']



위에 코드 실행하면 저런 결과값이 나온다. 3번 문제는 저렇게 여러가지 방식으로 똑같은 결과를 낼 수 있다는 말이어서 저래 길게 썼다.



4번이 좀 어려운데, 4번을 보면 밸류를 한 리스트에 쭉 모은다. 그리고 모인 리스트 중에 가장 큰 값을 찾고, 그 값이 있는 딕셔너리의 키를 찾아 내가 지정한 리스트에 어팬드한 것.