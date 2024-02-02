from django.shortcuts import render
from The_Owner.models import *
from .models import *
from The_Investor.models import * 
from FM.models import *

def index(request):
    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()
    promo_requests = PromoRequest.objects.all()  # قم بتحميل طلبات الترويج
    return render(request, 'pages/index.html', {'projects': projects, 'categories': categories, 'promo_requests': promo_requests})


# def index(request):
#     # استرجاع كائنات Project وإرسالها إلى القالب
#     projects = Project.objects.all()
#     return render(request, 'pages/index.html', {'projects': projects} ,)


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

def addpost(request):
    return render(request, 'pages/addpost.html')

def promoreq(request):
    return render(request, 'pages/promoreq.html')

def update(request):
    return render(request, 'pages/update.html')

def condations(request):
    return render(request, 'pages/condations.html')

def invreq(request):
    return render(request, 'pages/invreq.html')
def ownpro(request):
    return render(request, 'pages/ownpro.html')

def project(request):
    return render(request, 'pages/project.html')

def prodesc(request):
    project = Project.objects.all()
    investment_request = InvestmentRequest.objects.all()
    return render(request, 'pages/prodesc.html', {'project': project,'investment_request': investment_request})



