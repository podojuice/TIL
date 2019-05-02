from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Post, Image, Hashtag
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from .forms import PostModelForm, ImageModelForm, CommentModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest


@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
    if request.method == 'POST':
        # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
        post_form = PostModelForm(request.POST)
        # Data 검증을 한다.
        if post_form.is_valid():

            # 통과하면 저장한다.
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()

            #create hashtag
            content = post_form.cleaned_data.get('content')
            words = content.split() #띄어쓰기 기준 split
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = Hashtag.objects.get_or_create(content=word)
                    post.tags.add(tag[0])
                    if tag[1]:
                        messages.add_message(request, messages.SUCCESS, f'{tag[0]} 태그를 처음으로 추가하셨서요') # 태그가 처음 만들어졌을 경우


            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()

            return redirect('posts:post_list')
        else:
            # 실패하면, 다시 data 입력 form 을 준다.
            pass
    # GET 방식으로 요청이 오면,
    else:
        post_form = PostModelForm()
    image_form = ImageModelForm()
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,

    })


@require_GET
def post_list(request):
    posts = Post.objects.all()
    user = request.user
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'user': user,
        'comment_form': comment_form,
    })


@login_required
@require_http_methods(['POST'])
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentModelForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
    # FIXME else:




@login_required
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user: # 지금 수정하려는 포스트 작성자가 요청 보낸 사람이라면,
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                #update hashtag
                post.tags.clear()
                # create hashtag
                content = post_form.cleaned_data.get('content')
                words = content.split()  # 띄어쓰기 기준 split
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = Hashtag.objects.get_or_create(content=word)
                        post.tags.add(tag[0])
                        if tag[1]:
                            messages.add_message(request, messages.SUCCESS,
                                                 f'{tag[0]} 태그를 처음으로 추가하셨서요')  # 태그가 처음 만들어졌을 경우
                return redirect('posts:post_list')

        else:
            post_form = PostModelForm(instance=post)
        return render(request, 'posts/form.html', {
            'post_form': post_form
        })
    # 작성자와 요청 보낸 유저가 다르다면,
    else:
        return redirect('posts:post_list')


# def create_like(request, post_id):
#     user = request.user
#     post = get_object_or_404(Post, id=post_id)
#     post.like_users.add(user)

@login_required
@require_http_methods(['POST'])
def toggle_like(request, post_id):
    if request.is_ajax():
        user = request.user
        post = get_object_or_404(Post, id=post_id)
        is_active = True
        # if post.like_users.filter(id=user.id): ORM 버전. 밑에 건, 걍 파이썬문법 버전.
        if user in post.like_users.all():
            post.like_users.remove(user)
            is_active = False
        else:
            post.like_users.add(user)
            is_active = True
        return JsonResponse({
            'likeCount': post.like_users.count(),
            'is_active': is_active

        })
    else:
        return HttpResponseBadRequest()

@require_GET
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(Hashtag, content=tag_name)
    posts = tag.posts.all()
    return render(request, 'posts/list.html', {
        'posts': posts,
    })