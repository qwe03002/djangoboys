from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
  
def post_list(request):
    # posts 라는 쿼리셋 선언하면서 결과 받아옴
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    from django.shortcuts import render
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
