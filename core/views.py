from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import About, Contact
from .forms import ContactForm
from posts.models import Post


def about(request):
    about = About.objects.all()[0]
    context = {'about': about}
    return render(request, 'core/about.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Mesagem enviada com sucesso!')  # <-
        return redirect('contact')
    context = {'form': form}
    return render(request, 'core/contact.html', context)


def search(request):
    query = request.GET.get('q')
    page = request.GET.get('page', 1)
    posts = Post.objects.filter(Q(title__contains=query) | Q(content__contains=query))
    paginator = Paginator(posts, 4)
    posts = paginator.get_page(page)
    context = {'posts_list': posts}
    return render(request, 'core/search.html', context)


def tags(request, tag):
    page = request.GET.get('page', 1)
    posts = Post.objects.filter(tag__name__in=[tag])
    paginator = Paginator(posts, 4)
    posts = paginator.get_page(page)
    context = {'posts_list': posts, 'tag': tag}
    return render(request, 'core/tags.html', context)