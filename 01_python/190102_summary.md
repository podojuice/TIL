# 190102

zzu.li/ss3_seat

--> 수정 가능한 우리 좌석표.



오전수업

주피터 설치,

```bash
student@M7037 MINGW64 ~
$ cd TIL

student@M7037 MINGW64 ~/TIL (master)
$ cd 01_python

student@M7037 MINGW64 ~/TIL/01_python (master)
$ git clone https://github.com/eduyu/jupyter_notebooks.git
Cloning into 'jupyter_notebooks'...
remote: Enumerating objects: 50, done.
remote: Counting objects: 100% (50/50), done.
remote: Compressing objects: 100% (46/46), done.
remote: Total 50 (delta 1), reused 50 (delta 1), pack-reused 0
Unpacking objects: 100% (50/50), done.

student@M7037 MINGW64 ~/TIL/01_python (master)
$ ls
190102_summary.md  jupyter_notebooks/

student@M7037 MINGW64 ~/TIL/01_python (master)
$ cd jupyter_notebooks/

student@M7037 MINGW64 ~/TIL/01_python/jupyter_notebooks (master)
$ ls -a
./  ../  .git/  python101-students/

student@M7037 MINGW64 ~/TIL/01_python/jupyter_notebooks (master)
$ rm -rf .git

student@M7037 MINGW64 ~/TIL/01_python/jupyter_notebooks (master)
$ ls -a
./  ../  python101-students/

student@M7037 MINGW64 ~/TIL/01_python/jupyter_notebooks (master)
$ jupyter notebook
[I 10:20:39.586 NotebookApp] Writing notebook server cookie secret to C:\Users\student\AppData\Roaming\jupyter\runtime\notebook_cookie_secret
[I 10:20:39.961 NotebookApp] Serving notebooks from local directory: C:\Users\student\TIL\01_python\jupyter_notebooks
[I 10:20:39.961 NotebookApp] The Jupyter Notebook is running at:
[I 10:20:39.961 NotebookApp] http://localhost:8888/?token=dc91131f89e1fa67c894db55519c127ac1035c2f0fc8a63e
[I 10:20:39.961 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 10:20:39.976 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///C:/Users/student/AppData/Roaming/jupyter/runtime/nbserver-4772-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=dc91131f89e1fa67c894db55519c127ac1035c2f0fc8a63e
[I 10:22:49.982 NotebookApp] Interrupted...
[I 10:22:49.982 NotebookApp] Shutting down 0 kernels

student@M7037 MINGW64 ~/TIL/01_python/jupyter_notebooks (master)
$ jupyter notebook

```

설치후 주피터로 노트북을 켰음. 노트북은 유태영 선생님 깃허브에서 복사해갓고 git clone함.