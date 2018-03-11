from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}
    return render(request, 'posts/posts_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'posts/post_detail.html', context)