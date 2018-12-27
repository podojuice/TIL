import requests
import random
from random import sample

def am_i_lucky(my_numbers, real_numbers):
    match = set(my_numbers) & set(real_numbers['numbers'])
    bon=set([real_numbers['bonus']])

    if len(match) == 6:
        return('1등')
    elif len(match.intersection(match|bon)) == 6:
        return('2등')
    elif len(match) == 5:
        return('3등')
    elif len(match) == 4:
        return('4등')
    elif len(match) == 3:
        return('5등')
    else:
        return('꽝')

def pick_lotto():
    numbers = sample(range(1,46),6)
    return numbers

def get_lotto(draw_no):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(draw_no)
    response = requests.get(url)
    lotto_data = response.json()
    real_numbers =[]
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            real_numbers.append(value)
    bonus_number = lotto_data['bnusNo']
    data = {'numbers':real_numbers, 'bonus':bonus_number}
    luck=am_i_lucky(pick_lotto(), data)
    auto=str(pick_lotto())
    a=data['numbers']
    return (data, a)




print(a)
print(type(a['numbers']))
    
   #adfasdf