from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods


def posting_list(request):
    posts = Posting.objects.all()
    return render(request, 'board_ad/list.html', {'posts': posts})


def posting_detail(request, post_id):

    post = get_object_or_404(Posting, id=post_id)
    comments = post.comment_set.all()

    return render(request, 'board_ad/detail.html', {
        'post': post,
        'comments': comments,


        })


def new_posting(request):
    if request.method == 'GET':
        return render(request, 'board_ad/new.html')
    else:
        post = Posting()
        post.title = request.POST.get('input_title')
        post.content = request.POST.get('input_content')
        post.save()
        return redirect('board_ad:posting_detail', post.id)


def update_posting(request, post_id):
    post = get_object_or_404(Posting, id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('board_ad:posting_detail', post.id)
    else:
        return render(request, 'board_ad/edit.html', {'post': post})


@require_http_methods(['POST'])
def delete_posting(request, post_id):
    post = get_object_or_404(Posting, id=post_id)
    post.delete()
    return redirect('board_ad:posting_list')

#comment - create
@require_http_methods(['POST'])
def create_comment(request, posting_id):
    comment = Comment()
    comment.content = request.POST.get('input_comment')
    comment.posting_id = posting_id
    comment.save()
    return redirect('board_ad:posting_detail', posting_id)


def delete_comment(request, posting_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('board_ad:posting_detail', posting_id)
