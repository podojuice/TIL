#  190124 Django

오전. cmd 들어가서 choco install pycharm 했다. 그리고 깃헙 스튜던트 팩을 이용해 jetbrains에 가입했다. 무료로 뭔가를 받았따.



pycharm을 켰다. 세팅을 할 것인디, 



가입하는데만 30분 걸렸다. 이것저것 세팅해야하는데 다 놓쳤다.



ctrl alt s 누르면 세팅ㄴ ㅏ옴.



여기서 terminal 검색하고, 들어가서 cmd라고 돼 있는거를, c들어가서 programfiles 들어가서 git 들어가서 bin 들어가서 bash 선택하면 터미널 누를 때 bash가 자동으로 켜진다.

plugin 검색해서 들어가서 emmet everywhere 이랑 theme 검색해서 받아서 설치해라.

---------------

자 설치하는법 알앗으니까, 됐다. 자동화에 너무 익숙해지면 안좋으니 c9에서 해보자.



--------------------

### 장고 프로젝트 설치

```bash
podojuice:~/workspace $ django-admin startproject first_django

podojuice:~/workspace/FIRST_DJANGO $ python manage.py runserver $IP:$PORT
```

런 서버 하면 서버가 돈다. url 입력해서 보면, 에러메시지가 나온다. 호스트에게 allow 해주면 된다. 주소를 여기다 넣어주면 되는데,  그냥 allowed hosts에 '*' 추가해주면 만사ok다.

settings.py에서 해준거다. 또 세팅 py에서 language_code ko-kr로 바꿔주고, time_zone Asia/Seoul로 바꿔준다.

