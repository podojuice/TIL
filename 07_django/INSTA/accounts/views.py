from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from IPython import embed
from posts.forms import CommentModelForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {
            'form': form
        })
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('posts:post_list')
        else:
            return redirect('accounts:signup')


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:post_list')
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:post_list')
    # 사용자가 로그인 화면을 요청할 때!
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('posts:post_list')


def user_detail(request, username):
    user_info = User.objects.get(username=username)
    return render(request, 'accounts/user_detail.html', {
        'user_info': user_info,
        'comment_form': CommentModelForm(),
    })


@login_required
@require_POST
def toggle_follow(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)

    if receiver in sender.followings.all():
        sender.followings.remove(receiver)
    else:
        sender.followings.add(receiver)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))