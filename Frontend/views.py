from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from Frontend.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    usrname= request.session.get("username", None)

    context = {
        'username': usrname,
        'trips': Trip.objects.filter(display=True),
        'destination': Destinations.objects.filter(display=True),
    }
    if request.method == 'POST':
        username = request.POST.get("datepicker11")
        print(username)
    return render(request,'Frontend/index.html',context)


def login(request):
    if request.session.get("username", None) is not None:
        return redirect(reverse('index'))
    if request.method == 'POST':
        nsname = request.POST.get("ns_name")
        password = request.POST.get("password")
        abc = User.objects.filter(U_Name__iexact=nsname).count()
        if abc is not 0:
            d = User.objects.get(U_Name__iexact=nsname)
            if d.U_pswd == password:
                request.session["username"] = d.U_Name
                return redirect(reverse('index'))
            else:
                return render(request,'Frontend/login.html', {'label': "Password Error"})
        else:
            return render(request,'Frontend/login.html', {'label': "Account Not Exist"})
    return render(request,'Frontend/login.html')

def register(request):
    if request.session.get("username", None) is not None:
        return redirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get("ns_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        abc = User.objects.filter(U_Name__exact=username).count()
        if abc is not 0:
            return render(request,'Frontend/register.html', {'label': "Already Exist"})
        else:
            c = User.objects.create(U_Name=username, U_pswd=password, U_email=email)
            request.session["username"] = c.U_Name
            return redirect(reverse('index'))
    return render(request,'Frontend/register.html')


def logout(request):
    request.session.clear()
    return redirect(reverse('index'))


def trips(request):
    return render(request,'Frontend/trips.html')
def trip(request):
    return render(request,'Frontend/trip.html')
def blog(request):
    return render(request,'Frontend/blog_single.html')
def blogs(request):
    return render(request,'Frontend/blog.html')

def Dest(request):
    return render(request, 'Frontend/Dest.html')
def Destinatins(request):
    return render(request, 'Frontend/Destinatins.html')


def search_results(request):
    return render(request,'Frontend/search_results.html')


