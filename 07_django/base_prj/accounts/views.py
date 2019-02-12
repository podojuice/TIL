from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
# @login_required((login_url='/accounts/signin'))
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def index(request):
    return render(request, 'accounts/index.html')


def signin(request):
    # 이미 로그인 했는데, 다시 로그인을 하려 한다면,
    if request.user.is_authenticated:
        return redirect('accounts:index')
    # 로그인 시켜주세요
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # 검증 성공
            login(request, form.get_user()) # 로그인 하고

            if request.GET.get('next'): # 이전에 있던 페이지가 있다면 거기로 보내고
                return redirect(request.GET.get('next'))
            return redirect('accounts:index') # 없다면 우리가 지정한 페이지로 보낸다.
    # 로그인 화면 주세요
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {
        'form': form,
    })


def signout(request):
    logout(request)
    return redirect('accounts:index')
