from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import About, Contact
from .forms import ContactForm


def about(request):
    about = About.objects.all()[0]
    context = {'about': about}
    return render(request, 'core/about.html', context)


def contact(request):
    # import pdb
    # pdb.set_trace()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Mesagem enviada com sucesso!')  # <-
        return redirect('contact')
    context = {'form': form}
    return render(request, 'core/contact.html', context)