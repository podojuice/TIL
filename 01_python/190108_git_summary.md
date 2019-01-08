# git 사용법

15:10pm

c9 상에서 연습하고 있다.

git을 왜 쓰느냐



touch prj prj_1 prj_2 prj_final prj_final_real



이렇게 프로젝트 여러개 파일 계속 만들어나간다. 근데 마지막 플젝 파일이 읖어지면 그 전으로 돌아가야 하니까 전에 있던 파일을 냄겨두게 됨.

이렇게 버전을 관리하게 위해 존재하는 게 git이다.



git init

내가 있는 자리에 ~~ 를 달겠다

prj 디렉토리 만들고 그 안에 들어가서 git init 을 했더니 



Initialized empty Git repository in /home/ubuntu/workspace/prj/.git/



라고 나옴.

그러자 뒤에 숨김폴더 git이 생겼음. 버전 관리 시스템이.

이제 디렉토리가 아니고 repository가 됐다. 진화를 한 것. 다시 퇴화를 시키기 위해서는 .git을 지워주면 댄다.

rm -rf .git

이제 다시 그냥 디렉토리가 됐따.

repo로 다시 만들어준다.

which git 하면 내가 무슨 깃을 쓰고 있는 지 알려주는 거란다.



한 컴퓨터에 한 번만 해야되는 작업이 있다.

하지만 c9은 git 자동등록..



c9에서 무조건 home 디렉토리로 간 다음, cat .git 하면 

podojuice:~ $ cat .git
.gitconfig  .gitignore 

이렇게 나옴.

podojuice:~ $ cat .gitconfig 치면

[user]
​    name = hyungoo
​    email = hyungu0611@gmail.com
[core]
​    editor = nano
​    whitespace = off
​    excludesfile = ~/.gitignore
[advice]
​    statusuoption = false
[color]
​    ui = true
[push]
​    default = currentpodojuice:~ $

이렇게 나온다.



vim .gitconfig 로 들어가서 i 눌러서 편집모드로 바꾼다.



그리고 editor가 nano였는데, 이거를 vim으로 변경해줬다.

그리고 :w 치고 :q 쳤더니 나와졌다.





git status는 앞으로 많이 쓰게 될 것. 내 repo의 상태 물어보는 것.



prj 디렉토리 안에 txt 파일 하나 만들고 git status 물어봤더니,



On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        first_file.txt

nothing added to commit but untracked files present (use "git add" to track)



이렇게 대답해주네?



그래서 git add first_file.txt

해주고 다시 git status를 물어보니,



On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   first_file.txt

이렇게 착하게 알려준다.



podojuice:~/workspace/prj (master) $ git commit -m 'first commit'
[master (root-commit) 890d33d] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 first_file.txt
podojuice:~/workspace/prj (master) $ git status
On branch master
nothing to commit, working tree clean
podojuice:~/workspace/prj (master) $ 



커밋 하고 다시 status 물어보니, 바뀐 게 없댕



이제 git log 누르면,

podojuice:~/workspace/prj (master) $ git log
commit 890d33d795f995166ab91ca6722467cacce45687 (HEAD -> master)
Author: hyungoo <hyungu0611@gmail.com>
Date:   Tue Jan 8 06:43:56 2019 +0000

    first commit



이렇게 나옴. commit 뒤에 나오는 글자가 저장된 주소다. 커밋할 때 적었던 메시지가 밑에 first commit이라고 나온다.

add 하지 않고 commit 할 수는 없음.

commit 뒤에 붙는 -m 에 대해 이야기 해보자. 좋은 메시지는 내가 뭘 바꿨는지 상세히 명시해주는 것.



이제 로컬이랑 git hub랑 연동을 해보자. github에 repo 새로 만들고, 거기서 알려주는 거 다 입력하면 된다.

podojuice:~/workspace/prj (master) $ git remote add origin https://github.com/podojuice/learn_git_prj.git
podojuice:~/workspace/prj (master) $ git remote -v
origin  https://github.com/podojuice/learn_git_prj.git (fetch)
origin  https://github.com/podojuice/learn_git_prj.git (push)
podojuice:~/workspace/prj (master) $ git push -u origin master



하면 내 깃헙 아디랑 비번 입력하도록 나옴. 입력하면 청므으로 내 파일들이 올라가는 것!



자 이제 받는 걸 해보겠다

푸시 성공 후

집에서 이제 github에 있는 걸 다운받아보도록 하쟈

github 에 가서 연동하고자 하는 repo를 찾는다.  clone or download를 누르고 직접 다운로드를 하면 .git이 없기 때문에 연동이 안댄다??

`                                                                                
student@M7037 MINGW64 ~                                                         
$ git clone https://github.com/podojuice/learn_git_prj.git saffy_git            `



이렇게 하면 내 컴퓨터랑 내 깃헙 런 깃 프로젝트 리포랑 연동이 된다. 뒤에 붙은 saffy_git은 디렉토리 이름 이렇게 만들겠다 하는것.



bash 에서 code . 하면 비주얼스튜디오코드 켜짐. 여기서 수정하고 다시 git status 보면 달라져있는거 볼 수 잇음



자 여기서 새롱누 파일을 만들고 push를 했다. 하고서 다시 c9 상에서 뭘 수정을 하면 에라가 난다 이말이다. 여기서도 pull 을 해 줘야 집컴에서 수정하고 난 뒤 github에 올린 거를 다시 받아서 수정할 수 있다 이말이야



git pull 하면 잘 됐다~