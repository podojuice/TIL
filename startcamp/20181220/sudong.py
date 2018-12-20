import requests
import random

draw_No = input('로또회차:')

a,b,c,d,e,f = input('수동입력(6 숫자를 띄어쓰기로 구분해 입력해주세요) :').split()

my_numbers=set([int(a),int(b),int(c),int(d),int(e),int(f)])

# def pick_lotto():
#     numbers = random.sample(range(1, 46), 6)
#     return numbers

# my_numbers = pick_lotto()
# print('자동', my_numbers)

#여기서 보면 return을 해줘야 픽 로또 함수가 뭐 뱉는 걸 알 수있음


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

real_numbers = get_lotto(draw_No)


print(draw_No , '회 당첨 숫자' , real_numbers)

# print(set([real_numbers['bonus']]))

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

result = am_i_lucky(my_numbers, real_numbers)

# real_numbers = get_lotto()
print(result)



