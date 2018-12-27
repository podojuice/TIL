# 1221 정리

지금 flask 활용법 배우는 중.
### 'http:// ide.c9.io/pododuice/startcamp'
#여기서 c9.io 여기까지가 DOMAIN이고 이 뒤는 ROUTE임.

#### $ flask run -h 0.0.0.0 -p 8080
#근데 그냥모드로 하면 수정하고 바로 볼 수 없음. 바로 보려면 $ export FLASK_ENV='development' 하고 다시 하면 개발자모드로 들어갈 수 있음.

### 파이선 실행하면 바로 서버 가동하기

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

이거 해놓으면 이 py 파일 실행하면 

$ flask run -h 0.0.0.0 -p 8080

이거 굳이 터미널에 입력하지 않아도 서버 가동 가능.





### 변수 따라 주소, 내용 바뀌게 하기

그러나 라우트 매번 모두 지정해줄 수 없음. 변수를 줘가지고 주소 바뀔 수 있또록...하는법

```python
@app.route('/ide/<string:username>/<string:workspace>')
def username_workspace(username, workspace):
    return "{}'s hot {}!":.format(username, workspace)
```

이렇게 스트링 유저네임 스트링 워크스페이스 변수이름 줌.



그러면 주소에 유저네임이랑 워크스페이스 아무거나 입력해도 됨.





### 사이트 만들기 계속.

c9 에 startcamp 폴더에 templates라는 폴더 만들고 그 안에 html 파일들 만든다. 그러면 app.py에서 html 가져올 수 있음. app.py에서는 from flask import해서 함수 render_template 해줘야 이 기능 쓸 수 있음.

```python
#_*_ coding: urf-8 -*- 맨 위에 이거 넣으면 한글 이슈... 뭐 오타난듯.

@app.route("/")
def index():
    lunch = random.choice(['20층', 'Diet'])
    return render_template('index.html', menu=lunch)

#랜덤 초이스 해서 런치에 넣음. 그 런치를 menu에 넣고, 그 메뉴는 인덱스로 돌아감. 인덱스에는 <h2>Lunch: {{menu}}</h2> 이게 입력되어 있음. 중괄호 두개 안에 app.py에서 넘어온 menu라는 변수를 넣어주면, app.py에서 랜덤으로 초이스 된 것이 입력돼서 다시 app.py로 넘어와 Lunch : ~~ 이런 결과가 나온다는 것.
```



## 자, 오늘 거 매우매우 어려웠다 잘 복습하자



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style>
        body{
            background-color: #93b875;
        }
    </style>
</head>
<body>
    <h1>로또 등수 확인</h1>
    <h2>회차: {{draw}}</h2>

        <p>
            선택 회차 로또 번호: {{pick}}, 보너스 번호 {{bonus}}</br>
            당신의 자동 번호: {{auto}}</br>
            당신의 등수는?: {{luck}} 
            새로고침 하시면 새로운 자동 번호를 보실 수 있읍니다
    
        </p>

    
</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Ping</title>
</head>
<body>
    
    <h1>로또 운세 측정기</h1>
    <h2>
        당신의 운세: {{lu}}
    </h2>
    <p>
        
    </p>
    <form action="/get_lotto">
        회차 입력: <input type="text" name="phone_number" placeholder="ex)837"/></br>
        <input type="submit" value="얍!"/>
    </form>
    
</body>
</html>
```

밑에 게 먼저다. 밑에 걸 먼저 적고,



app.py에서



```python
@app.route("/ping")
def ping():
    lu = random.choice(["좋음","조금 좋음", "나쁨", "조금 나쁨", "최악", "최고"])
    return render_template("ping.html", lu=lu)

def am_i_lucky(my_numbers, real_numbers):
    match = set(my_numbers) & set(real_numbers["numbers"])
    bon=set([real_numbers["bonus"]])

    if len(match) == 6:
        return("1등")
    elif len(match.intersection(match|bon)) == 6:
        return("2등")
    elif len(match) == 5:
        return("3등")
    elif len(match) == 4:
        return("4등")
    elif len(match) == 3:
        return("5등")
    else:
        return("꽝")

def pick_lotto():
    numbers = sample(range(1,46),6)
    return numbers

@app.route("/get_lotto")
def get_lotto():
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="+str(request.args.get("phone_number"))
    response = requests.get(url)
    lotto_data = response.json()
    real_numbers =[]
    for key, value in lotto_data.items():
        if "drwtNo" in key:
            real_numbers.append(value)
    bonus_number = lotto_data["bnusNo"]
    data = {"numbers":real_numbers, "bonus":bonus_number}
    luck=am_i_lucky(pick_lotto(), data)
    auto=(pick_lotto())
   
    return render_template(
        "lotto.html",
        pick=data["numbers"],
        bonus=data["bonus"],
        draw=str(request.args.get("phone_number")),
        luck=luck,
        auto=auto,
    )

```

이렇게만 있으면 돌아간다. 

맨 첫 화면을  app.route로 /ping으로 보낸다. /ping에서 정보 입력을 유도하고, 정보 입력을 한 걸 받아와서 request함수를 이용해가지고 그 숫자를 get_lotto에 넣는다. 

그러면 get_lotto에서 파이썬에서 주구장창해왔던 함수를 돌려가지고 정보를 저장해서 읽을 수 있도록 만든 뒤 lotto.html에 넘긴다. 



lotto.html은 받은 정보를 출력해준다.