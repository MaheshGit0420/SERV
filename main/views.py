from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request, 'main/index.html')
