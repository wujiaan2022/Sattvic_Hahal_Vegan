from django.shortcuts import render


def menu(request):
    return render(request, 'menu/menu.html')


def dumplings(request):
    return render(request, 'menu/dumplings.html')


def setMenu(request):
    return render(request, 'menu/setMenu.html')
