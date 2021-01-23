from django import forms
from .models import MarketingSubs


class MarketingEmailSubForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Your email here',
    }), label="")

    class Meta:
        model = MarketingSubs
        fields = ('email', )
