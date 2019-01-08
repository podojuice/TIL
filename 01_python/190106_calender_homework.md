보소, 1월 1일이 일요일에 시작하면, 끝은 언제 나나? 그걸 알아보자.



1월이 끝났다. 1부터 31까지 range 해서 7, 14, 21,  28에는 줄 띄기, 나머지는 그냥 띄어쓰기로 출력했다.



자 2월은 1월이 31일이니까, 딱 7씩 떨어지는 28일에서 뺀다. 그럼 3이 남지? 이걸 띄어쓰기 세개씩 곱하면 첫줄은 2자리수가 있을 수가 없으니까.. 일월화가 건너뛰어지게 된다. 알간? 이제 1234, 567891011 이렇게 진행되면 된다. 



자 3월인데, 여기서부터 또 다르다. 2월은 28일이니까 2월에 시작한 요일이랑 3월에 시작한 요일이 같아야 하는데, 3월에 시작하는 요일은 딱떨어진다그래서 월요일에 시작하는 게 아니거든.



1월에 이미 3일이 오바됐는데, 그걸 다시 3월에도 적용해줘야한단 말이지. 옘병



```python
month = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apl',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec',
      

}

date = {
    0: 28,
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
      

}

day = ['su', 'mo', 'tu', 'we', 'th', 'fr', 'sa']

```

```python
a=0

for j in range(1, 13):
    print(month[j])
    a += date[j-1]-28
    if a == 7:
        a = 0
    elif a < 8:
        a = a
    elif a < 15:
        a = a - 7
    elif a < 22:
        a = a - 14
    else:
        a = a - 21
    
    
    for i in range(7):

        print(day[i], end=' ')
        
    print()
    print('--------------------')
    print((a)*'   ', end='')
    for i in (range(1, date[j]+1)):
        if i == (7-a):
            print(i)
        elif i == (14-a):
            print(i)
        elif i == (21-a):
            print(i)
        elif i == (28-a):
            print(i)
        elif i == (35-a):
            print(i)
        elif i < 10:
            print(i, end='  ')
        else:
            print(i, end=' ')

    print()
    print()
```

