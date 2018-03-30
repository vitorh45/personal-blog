from django.shortcuts import render
from .models import About


def about(request):
    about = About.objects.all()[0]
    context = {'about': about}
    return render(request, 'core/about.html', context)
