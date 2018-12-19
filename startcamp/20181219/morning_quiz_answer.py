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
