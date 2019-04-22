from django.db import models
from faker import Faker
from imagekit.models import ProcessedImageField
from django_extensions.db.models import TimeStampedModel
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

faker = Faker()


class Hashtag(models.Model):
    content = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.content



class Post(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    tags = models.ManyToManyField(Hashtag, blank=True, related_name='posts')

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            Post.objects.create(content=faker.text(130))


class Image(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
        blank=True,
        upload_to='posts/images',
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={'quality': 90, }
    )


class Comment(TimeStampedModel):
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
