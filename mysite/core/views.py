from django.shortcuts import render
from django.http import JsonResponse
from mysite.core.models import Data


def home(request):
    return render(request, 'home.html')


def supervision(request):
    labels = ["8:00", "5:00", "4:00", "2:00"]
    data = [500, 200, 100, 50]

    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

