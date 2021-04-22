from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Event,EventRegistration
from . forms import EventRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def list_events(request):
    events = Event.objects.all()
    return render(request, 'events/list_events.html', {'events':events})

@login_required
def register_view(request, eve_id):
    username = request.user.username
    event = Event.objects.get(pk=eve_id)
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{username} Successfully Registered for {event}!')
            return redirect("list_events")
    else:
        form = EventRegistrationForm(initial={'username':username, 'event':event})
        return render(request, 'events/event_register.html', {'form':form})

# def leaders_view(request):
#         registrations = EventRegistration.objects.all()
#         users = User.objects.all()
#         redt = {}
#         for user in users:
#             EventRegistration.objects.get(username.__iexact==user.username)
#             redt[user]+=redt.get(user, 10)
#         print(redt['admin'])
#         return render(request, 'events/leaders.html', {'redt':redt})
