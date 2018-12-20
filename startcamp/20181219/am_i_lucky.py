import requests

import random














url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)

lotto_data = response.json()

real_numbers =[]

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)
#우리는 보너스 넘버가 필요해!
bonus_number = [lotto_data['bnusNo']]
print('이번 회차의 번호 :', real_numbers)



numbers = list(range(1, 46))
my_numbers = random.sample(numbers, 6)

print('당신의 번호 :', my_numbers)
print('보너스 번호 :', bonus_number)

# # print(sorted(my_numbers))
# #우리는 리얼넘버 마이넘버 보너스 넘버가 있다.
# #1등: my_numbers == real_numbers
# #2등: 제일 어려움 real & my가, my의 나머지 하나가 bonus_number
# #3등: real & my 가 5개가 같다.
# #4등: real & my 가 4개가 같다.
# #5등: real & my 가 3개가 같다.
# #꽝

myn=set(my_numbers)
ren=set(real_numbers)
bon=set(bonus_number)

# myn={1,14,3,4,5,7}
# ren={1,2,3,4,5,6}



if len(myn.intersection(ren)) == 6:
    am_i_lucky ='1등'
elif len(myn.intersection(ren|bon)) == 6:
    am_i_lucky ='2등'
elif len(myn.intersection(ren)) == 5:
    am_i_lucky ='3등'
elif len(myn.intersection(ren)) == 4:
    am_i_lucky ='4등'
elif len(myn.intersection(ren)) == 3:
    am_i_lucky ='5등'
else:
    am_i_lucky ='꽝'

print('당신의 등수는 :', am_i_lucky)