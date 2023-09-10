from django.shortcuts import render


def index(request):
    return render(request, 'massage_salon/index.html')


def prices(request):
    return render(request, 'massage_salon/prices.html')


def about(request):
    return render(request, 'massage_salon/about.html')
