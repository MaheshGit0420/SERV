from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=999, blank=True, null=True)
    address = models.CharField(max_length=256, null=True)
    datetime = models.DateTimeField(blank=True)
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.title)


class EventRegistration(models.Model):
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.IntegerField(blank=True)
    event = models.CharField(max_length=64)
