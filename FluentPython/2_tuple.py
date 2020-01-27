# 튜플 =/= 단순한 불변 리스트 but record

lax_coordinates = (33.95, -119.3)

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)


for country, _ in traveler_ids:
    print(country)


# tuple unpacking

latitude ,longitude = lax_coordinates

print(latitude, longitude)

print(divmod(20, 8))

t = (20, 8)

# *를 앞에 붙임으로써 t라는 tuple 자료형을 unpacking함
print(divmod(*t))


# 다른 용도의 *. 초과 항목을 잡기 위해 사용함

a, b, *rest = range(5)

print(a, b, rest)

a, b, *rest = range(2)

print(a, b, rest)

# 튜플이 record로 사용되기엔 애매하다. 그래서 고안된 것이 namedtuple

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)

print(tokyo.population, tokyo.coordinates, tokyo[1])

print(City._fields)

# 튜플은 불변 리스트로서의 역할도 어느정도 한다.

# 슬라이싱

l = list(range(10))

print(l)

l[2:5] = [20, 30]

print(l)

del l[5:7]

print(l)

l[3::2] = [11, 22]

print(l)

l[2:5] = [100]

print(l)


# 시퀀스의 복합 할당 ex) += , *=

# 시퀀스에 던더 iadd가 구현돼있음녀 이게 나오는데, 없ㅇ느면 던더 add가 나옴. 그러니까 차이가 있음.

# 가변 시퀀스일 경우 a의 값이 변경됨. 하지만, 뭐 그렇지 않을 수도 있따는 얘기.


# 가변, 불변 시퀀스에 *=를 써보자.

l = [1,2,3]

print(l, id(l))

l *=2

print(l, id(l))

t = (1,2,3)

print(t, id(t))

t*=2

print(t, id(t))


# list.sort() 와 sorted()

# sort()메서드는 None을 반환. 이거는 API의 관례. 내부적으로 만들고 새 리스트를 만들지 않았다는얘기.

# bisect 87p.



