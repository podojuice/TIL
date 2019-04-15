from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

# Create your models here.

class MagazineArticle(TitleDescriptionModel, TimeStampedModel):
    content = models.TextField()


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Writer(TimeStamp):
    name = models.CharField(max_length=100)


class Book(TimeStamp):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)

class Chapter(TitleDescriptionModel, TimeStampedModel):
    #이렇게 상속받으면, title, description, created, modified가 생긴다.
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
