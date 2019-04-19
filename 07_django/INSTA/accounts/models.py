from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class User(AbstractUser):
#
#     def __str__(self):
#         return self.username

# 유저 모델이 확장될 수 있으니 개발 시작 전에 미리 위에 있는 코드를 직접 치고 시작해라. 라고 장고에서 추천하고 있다.

from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    followings = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followers',
        blank=True,
    )

    def __str__(self):
        return self.username
