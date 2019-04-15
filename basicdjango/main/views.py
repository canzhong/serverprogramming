from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def brewers(request):
    return render(request, 'main/brewers.html')

def bucks(request):
    return render(request, 'main/bucks.html')

def marquette(request):
    return render(request, 'main/marquette.html')