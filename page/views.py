from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')

def deals(request):
    return render(request, 'pages/deals.html')

def reservation(request):
    return render(request, 'pages/reservation.html')

def login(request):
    return render(request, 'pages/login.html')    

def signIn(request):
    return render(request, 'pages/signIn.html')

def vir(request):
    return render(request, 'pages/vir.html')    
# Create your views here.