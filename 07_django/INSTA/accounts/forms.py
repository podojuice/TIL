from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
# 순서대로 회원 가입, 회원 정보 수정, 로그인 관련 폼.


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'email', )

