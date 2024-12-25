from django.shortcuts import render
from .models import Uni
from django.http import HttpResponse

def unis_list(request):
    unis = Uni.objects.all().order_by('-date')
    return render(request, 'unis/unis_list.html', {'unis': unis})

def unis_page(request, slug):
    unis = Uni.objects.all().order_by('-date')
    return render(request, 'unis/unis_list.html', {'unis': unis})
