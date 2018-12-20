#강사님의 로또 함수 정리
import requests
import random

draw_No= input('로또회차입력:')

def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers

my_numbers = pick_lotto()
print('자동', my_numbers)

def get_lotto(X):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(X)
    response = requests.get(url)
    lotto_data = response.json()
    real_numbers =[]
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            real_numbers.append(value)
    bonus_number = lotto_data['bnusNo']
    lotto_king = {'numbers':real_numbers, 'bonus':bonus_number}
    return lotto_king

real_numbers = get_lotto(draw_No)



list_1 = [1,2,3,4,5,7]
dict_1 ={
    'numbers':[1,2,3,4,5,6],
    'bonus':7
} 

def am_i_lucky(pick, draw):
    match = set(pick) & set(draw['numbers'])
    if len(match) ==6:
        return('1등')
    elif len(match) ==5 and draw['bonus'] in pick:
        return('2등')
    elif len(match) ==5:
        return('3등')
    else:
        return('꽝')

print(am_i_lucky(my_numbers, real_numbers))



