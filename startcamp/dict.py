my_info = {'name':'neo', 'job':'hacker', 'phone':'010-1234-1234', 'email': 'neo@hphk.kr'}

hphk = [
    {
        'name':'john',
        'email':'john@naver.com'
    },
    {
        'name': 'tak',
        'email':'tak@naver.com'
    },
    {
        'name':'neo',
        'email':'neo@naver.com'
    }
]

#여기서 neo의 email에 접근하려면?

p = hphk[2]
print(type(p))
print(p['name'])
