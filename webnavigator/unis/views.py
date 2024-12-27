from django.shortcuts import render
from .models import Uni


def unis_list(request):
    unis = Uni.objects.all().order_by('-date')
    return render(request, 'unis/unis_list.html', {'unis': unis})


def uni_page(request, slug):
    uni = Uni.objects.get(slug=slug)
    return render(request, 'unis/uni_page.html', {'uni': uni})
