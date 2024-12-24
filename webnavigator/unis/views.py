from django.shortcuts import render


def unis_list(request):
    return render(request, 'unis/unis_list.html')
