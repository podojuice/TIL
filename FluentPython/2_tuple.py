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

# 불변 리스트로서의 튜플