import requests
import random

# draw_No = input('로또회차:')

def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers

my_numbers = pick_lotto()
# print('자동', my_numbers)

#여기서 보면 return을 해줘야 픽 로또 함수가 뭐 뱉는 걸 알 수있음!


#get_lotto()를 정의해보자



def get_lotto(draw_No):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(draw_No)
    response = requests.get(url)
    lotto_data = response.json()
    real_numbers =[]
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            real_numbers.append(value)
    bonus_number = lotto_data['bnusNo']
    lotto_king = {'numbers':real_numbers, 'bonus':bonus_number}
    return lotto_king

# real_numbers = get_lotto(draw_No)


# print(draw_No , '회 당첨 숫자' , real_numbers)

# print(set([real_numbers['bonus']]))

def am_i_lucky(my_numbers, real_numbers):
    myn=set(my_numbers)
    ren=set(real_numbers['numbers'])
    bon=set([real_numbers['bonus']])

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
    return am_i_lucky

# result = am_i_lucky(my_numbers, real_numbers)

# real_numbers = get_lotto()
# print(result)



