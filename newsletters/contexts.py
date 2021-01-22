from django.conf import settings
from .forms import MarketingEmailSubForm
""" function to display the email Subcription form across the site """
def sub_form_display(request):
    sub_form = MarketingEmailSubForm
    context = {
        'sub_form':sub_form
    }
    return context