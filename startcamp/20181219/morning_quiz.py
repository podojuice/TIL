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


# # 3: 도시별 평균 온도
# #출력값은 서울:?
# #대전:?
# #광주:?
# #구미:?

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



#4 도시중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳.
#Hottest:?? , coldest:??

city_key=cities.keys() #역시 cities의 키를 뺌

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
