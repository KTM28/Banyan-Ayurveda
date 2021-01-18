from django import forms


class ContactForm(forms.Form):
    """
    A form for contact page
    """

    full_name = forms.CharField(label=""
    )
    email = forms.EmailField(
        label=""
    )
    message = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "rows": 3,
        })
    )

    class Meta:
        fields = ['full_name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = ('Full Name')
        self.fields['email'].widget.attrs['placeholder'] = ('Your Email Address')
        self.fields['message'].widget.attrs['placeholder'] = ('Your Message')
