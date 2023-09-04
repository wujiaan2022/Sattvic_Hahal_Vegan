from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def aboutUs(request):
    return render(request, 'home/aboutUs.html')