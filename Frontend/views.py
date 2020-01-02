from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from Frontend.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    type=0
    tripp=None
    destt=None
    oprr=None
    if request.method == 'POST':
        radio = request.POST.get("radio")
        print(radio)
        if radio == "form1":
            dest = request.POST.get("destinationn1")
            date = request.POST.get("datepicker11")
            type=1
            tripp=Trip.objects.filter(T_Name__contains="dest")
        if radio == "form2":
            dest = request.POST.get("destinationn2")
            date = request.POST.get("datepicker12")
            type=2
            destt=Destinations.objects.filter(T_Name__contains="dest")
        if radio == "form3":
            dest = request.POST.get("destinationn3")
            date = request.POST.get("datepicker13")
            type=3
            oprr=Tour_Operator.objects.filter(T_Name__contains="dest")
        context = {
            'username': request.session.get("username", None),
            'trips': tripp,
            'destinations': destt,
            'operators': oprr,
            'type': type,
        }
        return render(request, 'Frontend/search_results.html',context)
    else:
        context = {
            'username': request.session.get("username", None),
            'trips': Trip.objects.filter(display=True),
            'destinations': Destinations.objects.filter(display=True),
            'deals': Deal.objects.all(),
            'operators': Tour_Operator.objects.all(),
        }
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
            return redirect(reverse('index',))
    return render(request,'Frontend/register.html')


def logout(request):
    request.session.clear()
    return redirect(reverse('index'))


def trips(request):
    trips=Trip.objects.all()
    context = {

        'username': request.session.get("username", None),
        'trips' : Trip.objects.all()
    }
    return render(request,'Frontend/trips.html',context)
def trip(request):
    return render(request,'Frontend/trip.html')
def blog(request):
    return render(request,'Frontend/blog_single.html')
def blogs(request):
    return render(request,'Frontend/blog.html')

def Places(request):
    context = {
        'username': request.session.get("username", None),
        'destinations': Destinations.objects.all(),
    }
    return render(request, 'Frontend/places.html',context)

def place(request):

    return render(request, 'Frontend/place.html')

def touroperator(request):
    context = {
        'username': request.session.get("username", None),
        'operators': Tour_Operator.objects.all(),
    }
    return render(request, 'Frontend/touroperators.html',context)

def search_results(request):
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(display=True),
        'destinations': Destinations.objects.filter(display=True),
        'deals': Deal.objects.all(),
        'operators': Tour_Operator.objects.all(),
        'type':'1',
    }
    return render(request,'Frontend/search_results.html',context)


