# 11일 깃 basic

## basic workflow

```sh
$ git init

$ git status # 빨간색 확인

$ git add .

$ git status # 초록색 확인 초록색만 커밋 될거임.

$ git commit -m '짧고 간결하게 현재형'



#여기서 먼저 github나 bitbucket 등 remote repo를 생성했어야함. 

$ git push

$ git remote add origin <REMOTE REPO URL.git>

$ git push (-u origin master) # 첫번째만

# 다른 컴퓨터라면,

$ git clone <REMOTE REPO URL.git> # downloadZIP => .git 없음 ㅠ

# 작업 후

$ git add . && git commit -m 'MSG' && git push # 이렇게 해도 되고,

$ git add . ; git commit -m 'MSG' ; git push #이렇게 해도 됨. 근데 얘는 앞에서 에러나도 뒤에 진행이 되기 때문에 &&으로 가는 게 나음.





$ git pull
```

## Intermediate workflow

vim



less



.gitignore

안에 인식하기 싫은 놈 적어두면 git add할때 추가안해줌.



git add . 해서 올려버린 친구 다시 인식 안되게 하고 싶음. commit 안되게 내리게 하고 싶으면?

git rm --cached dummy.txt 하면 댐.



## Brancing and merging

master branch에서는 작업하는 곳이 아니다.

어디어디 브랜치에서 작업을 하고, 그걸 마스터에 merge만 하는 것.

모두가 협업할 때는, merge를 함부로하면 큰일이 날 거다. 그니까 request를 해주는 거다. 그럼 규칙에 따라 merge를 하는 것.



git branch ~~~ 하면 branch 생김

그리고 git cheakout ~~~ 하면 내가 만든브랜치로 갔ㅇ음.

그리고 브랜치에서 작업을 하고 git add .를 하고 커밋을 했음.

다시 마스터로 checkout하니까 거기서는 브랜치에서 수정한 것이 적용이 안돼있음.



git diff master 해보면 브랜치랑 master랑 얼마나 차이가 나는지 확인 가능



이제 merge해보자.



master가 사실 제일 중요하니까, master에서 branch를 소환해야함.

git merge ~~~



git checkout -b help-page 하면 help-page라는 브랜치를 만들고 이동해라 라는 의미.



브랜치에서는 커밋만 된다. 푸시는 안된다. 왜냐면 처음에 git push -u origin master를 했잖냐. 그러면 master에서만 푸시가 된다이거같은데



이렇게하고 깃헙 가면 request가 날아와있음. 이거 협업하는 깃헙이었으면 이제 남들이 허가를 내줘야되는거임. 문제 없으면 merge pull request 바로 받아줄 수 있음. 이제서야 합쳐졌음.



근데 문제는 원격에서, 깃헙에서는 머지가 됐는ㄷ, 로컬에서는 아직 머지가 안됨. 마스터로 나가서 git pull 하면 되는거임.



이래서 협업하는 경우에 github이 더 중요한 것. 거기서 머지하고 받으면 되는거니깐.