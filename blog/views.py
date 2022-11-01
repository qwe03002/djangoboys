from time import time

from blog.forms import PostForm
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
  
def post_list(request):
    # posts 라는 쿼리셋 선언하면서 결과 받아옴
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    from django.shortcuts import render
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
    if request.method == "POST":
        # request.POST : 화면에서 사용자가 입력한 내용들이 담겨있다.
        form=PostForm(request.POST)
        if form.is_valid(): # 폼이 유효하다면
            # 임시 저장하여 post 객체를 리턴받는다.
            post=form.save(commit=False)
            post.author = request.user
            # 실제 저장을 위해 작성일지를 설정한다.
            post.published_date=timezone.now()
            post.save() # 데이터를 실제로 저장한다.
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm()
    # return 문은 else: 와 같은 레벨이어야 함!!
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm(instance=post)
    
    return render(request, 'blog/post_edit.html', {'form':form})