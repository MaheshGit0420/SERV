from django.shortcuts import render, redirect
from . forms import UserRegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Account Successfully created for {username}!')
            form.save()
            return redirect("index")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
