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