from django.shortcuts import render, redirect
from .models import Posting, Comment


def posting_list(request):
    posts = Posting.objects.all()
    return render(request, 'board_ad/list.html', {'posts': posts})
    pass


def posting_detail(request, id):
    post = Posting.objects.get(id=id)

    return render(request, 'board_ad/detail.html', {'post': post})
