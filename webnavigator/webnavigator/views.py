from django.shortcuts import render
from unis.models import Uni

def homepage(request):
    unis = Uni.objects.all().order_by('-date')
    return render(request, 'index.html', {'unis': unis})

def about(request):
    return render(request, 'about.html')