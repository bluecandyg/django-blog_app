from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.modelforms import PostModelForm
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

# 새글 등록
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


