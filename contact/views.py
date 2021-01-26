# import os

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm
from profiles.models import UserProfile
from django.contrib.auth.models import User


def contact(request):
    """A view to display contact page and form"""
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            user_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    f"Message from {full_name}, <{user_email}>",
                    message,
                    user_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                return redirect('contact_success')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            user_name = User.objects.get(username=request.user)
            user_email = profile.user.email
            contact_form = ContactForm(initial={
                'email': user_email,
                'full_name': user_name,
                })
        else:
            contact_form = ContactForm()
    context = {
            'contact_form': contact_form,
            'api_key': settings.GOOGLE_MAP_API_KEY,
        }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """
    A view to inform user that the message was successfully sent
    """
    return render(request, 'contact/contact_success.html')
