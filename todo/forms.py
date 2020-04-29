from django import forms
from .models import Task

class TodoForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.SelectDateWidget)
    class Meta:
        model = Task
        fields = ['title', 'desc', 'deadline']