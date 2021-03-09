from django.contrib import admin
from . models import Event,EventRegistration

class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'datetime', 'address', 'description']

class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['event','username']

admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
