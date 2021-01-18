from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import MarketingSubs
from .forms import MarketingEmailSubForm

def marketing_sub(request):
    """ News letter subscription view- if email exists in db 
        Send a message else saves the email """

    form = MarketingEmailSubForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            marketingsubs_qs = MarketingSubs.objects.filter(
                email=form.instance.email
            )
            if marketingsubs_qs.exists():
                messages.info(
                    request, 'You have already subscribed to our News Letter!'
                )
            else:
                email = request.POST["email"]
                new_subscription = MarketingSubs()
                new_subscription.email = email
                new_subscription.save()
                messages.success(
                    request, 'Thank you for Subscribing to our News letter'
                )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))