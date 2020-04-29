from django.shortcuts import render, HttpResponseRedirect
from .models import Email
from django.core.mail import send_mail
from .forms import EmailForm
from django.conf import settings

def send(request):

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['email'])
            subject = form.cleaned_data['subject']
            to = []
            to.append(form.cleaned_data['to'])
            body = form.cleaned_data['body']
            send_mail(subject=subject, from_email=settings.EMAIL_HOST_USER, message=body, recipient_list=to, fail_silently=False)
            return render(request, 'home.html', {})
    form = EmailForm()
    return render(request, 'send.html', {'form':form})