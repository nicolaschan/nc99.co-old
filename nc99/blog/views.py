from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
    posts = Post.objects.order_by('-timestamp')[:3]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog/post.html', context)
