from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    context = {'posts_list': posts}
    return render(request, 'posts/posts_list.html', context)

def post_detail(request, slug):
    try:
        post = Post.objects.filter(Q(slug=slug) | Q(slug_en=slug))[0]
    except:
        raise Http404()
    context = {'post': post}
    return render(request, 'posts/post_detail.html', context)