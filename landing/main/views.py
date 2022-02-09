from django.shortcuts import render
from .models import Usertest


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def shop(request):
    return render(request, 'main/shop.html')

def test(request):
    return render(request, 'main/test.html')

def create_tcs(request):
    tcs = Usertest.objects.all()
    return render(request, 'main/create-tcs.html', {'title': 'Testcases', 'tcs': tcs})