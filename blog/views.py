def post_list(request):
    from django.shortcuts import render
    return render(request, 'blog/post_list.html', {})

