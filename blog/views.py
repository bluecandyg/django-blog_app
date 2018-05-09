from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.modelforms import PostModelForm, PostForm, CommentForm
from .models import Post, Comment


# Create your views here.

# 글 목록 리스트
def post_list(request):
    # name = 'Django'
    # return HttpResponse('''
    # <h1>Hello {myname}</h1>
    # '''.format(myname=name))

    # QuerySet 사용해서 Post 글 목록 가져오기
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})

# 글 상세 조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 새글 등록 - ModelForm 사용
def post_new(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostModelForm()

    return render(request, 'blog/post_edit.html', {'form': form})


# 새글 등록 - 기본 From 사용
def post_new_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            # 방법1 : Post 객체 생성 후, save() 호출
            # post = Post()
            # post.author = request.user
            # post.title = form.cleaned_data['title']
            # post.text = form.cleaned_data['text']
            # post.published_date = timezone.now()
            #
            # # DB에 저장
            # post.save()

            # 방법2 : Post.objects.create() 호출
            post = Post.objects.create(author=request.user, title=form.cleaned_data['title'],
                                       text=form.cleaned_data['text'], published_date=timezone.now())

            return redirect('post_detail', pk=post.pk)
        else:
            form.errors
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

# 글 수정하기 - ModelForm 사용
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostModelForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})

# 글 삭제 하기
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return redirect('post_list')

# 댓글 등록하기
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# 댓글 승인하기
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)


# 댓글 삭제하기
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail', pk=post_pk)


