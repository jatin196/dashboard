from django import forms
from .models import Email
from tinymce.widgets import TinyMCE

class EmailForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class  Meta:
        model = Email
        fields = ('to', 'subject', 'body')

