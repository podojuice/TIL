team = [
    'john',
    10000,
    'neo',
    100,
    'tak',
    40500
]

new_member =['js', 10]

team = team + new_member
print
#리스트끼리 덧셈 연산하면 맨 뒤에 그냥 들어가버림.
#n=0
#n= n+1
#위에 적은 두 줄의 코딩을 귀찮다고 한 줄로 줄여버린 거시 +=임.
#예를 들어 n+=1하면 n=n+1이 되는 것.

#리스트에서 인자 제거하기

del(team[2])

print(team)