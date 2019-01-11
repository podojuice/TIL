# 플라스크 배우기

플라스크 설치 - bash 키고 



`student@M7037 MINGW64 ~/til/04_flask/first_app (master)                         
$ pip install flask`

pip install flask 해준다.



내가 지정한 디렉토리에 app.py만들어주고,



```python
from flask import Flask

app = Flask(__name__)

# 밑에 있는 @는 데코레이터라고 함. app은 객체고, route는 Flask라는 클래스 안에 있는 메서드.

@app.route('/')
def index():
    return 'Hi'

#서버가 죽었다. 대신 돌고 있다는 의미가 영어로 run임.
#
if __name__ == '__main__':
    app.run()
else:
    print('unknown')
```

이런 식으로 진행중임. 현재 9시 36분.



```python
__name__ 은 '__main__'임.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
    
앱 런에다가 디버그랑 호스트랑 포트 추가해줌.





```

이게 되니깐, 클래스 Flask를 상상해보자.

class Flask:
​    def run(self, debub=??, host='??', port=??)
​    
 이런 식으로 되어 있을까??? 아니다. 이것보다 더 많은 인자들이 들어오기 때무네.

**kwargs로 해결할 수 있다! 얘는 a = b 이런식으로 인자 주면 키는 a 값은 b 라느 식으로 딕셔너리형태로 정보를 넘겨준다.



bash에서 실행해주고 싶으면 같은 디렉토리에서, flask run 해주면 된다.



디버그모드 켜주니깐 app.py수정하면 바로 서버에 추가댐.



개발환경이랑 배포환경 바꿔주고 싶다면, 서버 껐다가, 



$ export FLASK_ENV='development' 해주면 된다.

이거는 FLASK_ENV 라는 데 development라는 문자열을 넣은 거임.

$ echo $FLASK_ENV 해보면
development 이렇게 결과가 나옴

export 하면 변수 세팅 하는거임.



$ $RUN_FLASK= ~~ 하면 뭐 넣는 거고

다시

$ RUN_FLASK= 하고 아무 것도 안 써주면 변수에 아무 것도 없는 걸루 바뀜





ascii pokemon 하면 텍스트로 만들어진 포켓몬 찾을 수 있음





앨리어스랑 같은 것. jupyter notebook을 jn으로 바꿨던 거랑 같음.



------------------------------------------------------

자 이제 주소가 바뀔 때마다 다른 이름이 들어오도록 하게 만들어보자.



```python
@app.route('/hi/<string:name>')
def hi(name):
    return f'hi! {name}'
```

이렇게 하면, hi 뒤에 무슨 글자를 적든 hi! 하고 그 뒤에 그 글자가 나오는 결과가 나옴.



예를 들어, 어떤 사이트에서 검색을 하면 뭐가 나온다 치면,



```python
@app.route('/keyword/<string:word>')
def keyword(word):
    search_results = DB.find(word)
```

이런 식으로 구성된 사이트일 것이다.

이런 걸 가능하게 해주는 것이 variable routing. 위 처럼 한느 거다.



