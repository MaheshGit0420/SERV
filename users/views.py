from django.shortcuts import render, redirect
from . forms import UserRegisterForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user_email = form.cleaned_data['email']
            subject = "Welcome to SERV"
            message = f"Hi {username}, ThankYou for Registering with SERV"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_email,]
            messages.success(request, f'Account Successfully created for {username}!')
            form.save()
            send_mail(subject, message, email_from, recipient_list)
            return redirect("index")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
