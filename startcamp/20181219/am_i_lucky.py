import requests

import random

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json()

real_numbers =[]

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])

for key, value in lotto_data:
    if 'drwtNo' in key:
        real_numbers.append(value)
#우리는 보너스 넘버가 필요해!
bonus_number = lotto_data['bnusNo']
print(real_numbers)



numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)

print(sorted(my_numbers))
#우리는 리얼넘버 마이넘버 보너스 넘버가 있다.
#1등: my_numbers == real_numbers
#2등: 제일 어려움 real & my가, my의 나머지 하나가 bonus_number
#3등: real & my 가 5개가 같다.
#4등: real & my 가 4개가 같다.
#5등: real & my 가 3개가 같다.
#꽝

# for i in real_numbers.item():
#         if i in my_numbers:
#                 append(luckydraw)

# print(luckydraw)