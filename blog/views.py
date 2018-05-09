from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.modelforms import PostModelForm, PostForm
from .models import Post

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
            #print(form.cleaned_data)
            post = Post()
            post.author = request.user
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.published_date = timezone.now()

            # DB에 저장
            post.save()

            return redirect('post_detail', pk=post.pk)
        else:
            print(form.errors)
    else:
        form = PostForm()

    return  render(request, 'blog/post_form.html', {'form': form})



