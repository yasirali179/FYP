from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from Frontend.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):

    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
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
    label=" "
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
                context = {
                    'username': request.session.get("username", None),
                    'trips': Trip.objects.filter(display=True),
                    'destinations': Destinations.objects.filter(display=True),
                    'deals': Deal.objects.all(),
                    'operators': Tour_Operator.objects.all(),
                    'label': "password Error"
                }
                return render(request,'Frontend/login.html',context)
        else:
            context = {
                'username': request.session.get("username", None),
                'trips': Trip.objects.filter(display=True),
                'destinations': Destinations.objects.filter(display=True),
                'deals': Deal.objects.all(),
                'operators': Tour_Operator.objects.all(),
                'label': "Account Not Exist"
            }
            return render(request,'Frontend/login.html', context)
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(display=True),
        'destinations': Destinations.objects.filter(display=True),
        'deals': Deal.objects.all(),
        'operators': Tour_Operator.objects.all(),
        'label': " "
    }
    return render(request,'Frontend/login.html',context)

def register(request):
    if request.session.get("username", None) is not None:
        return redirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get("ns_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        abc = User.objects.filter(U_Name__exact=username).count()
        if abc is not 0:
            context = {
                'username': request.session.get("username", None),
                'trips': Trip.objects.filter(display=True),
                'destinations': Destinations.objects.filter(display=True),
                'deals': Deal.objects.all(),
                'operators': Tour_Operator.objects.all(),
                'label': "Already Exist"
            }
            return render(request,'Frontend/register.html',context)
        else:
            c = User.objects.create(U_Name=username, U_pswd=password, U_email=email)
            request.session["username"] = c.U_Name
            return redirect(reverse('index',))
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(display=True),
        'destinations': Destinations.objects.filter(display=True),
        'deals': Deal.objects.all(),
        'operators': Tour_Operator.objects.all(),
        'label': " "
    }
    return render(request,'Frontend/register.html',context)


def logout(request):
    request.session.clear()
    return redirect(reverse('index'))


def trips1(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'trips' : Trip.objects.filter(noOfDays=1)
    }
    return render(request,'Frontend/trips.html',context)

def trips2(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'trips' : Trip.objects.all(),
    }
    return render(request,'Frontend/trips.html',context)
def trip(request,articalvalue):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'p': Trip.objects.get(Trip_Id=articalvalue)
    }
    return render(request,'Frontend/trip.html',context)

def operator(request,articalvalue):
    print(articalvalue)
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'p': Tour_Operator.objects.get(Op_Id=articalvalue)
    }
    return render(request,'Frontend/operator.html',context)


def blog(request):
    return render(request,'Frontend/blog_single.html')
def blogs(request):
    return render(request,'Frontend/blog.html')

def Places(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'destinations': Destinations.objects.all(),
    }
    return render(request, 'Frontend/places.html',context)

def place(request,articalvalue):
    obj=Destinations.objects.get(Des_Id=articalvalue)
    obj1=Trip.objects.filter(Dest=obj)
    print(obj1)
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'trips':obj1
    }
    return render(request, 'Frontend/place.html',context)

def touroperator(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'operators': Tour_Operator.objects.all(),
    }
    return render(request, 'Frontend/touroperators.html',context)

def search_results(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"]  = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context=search(request)
    return render(request,'Frontend/search_results.html',context)

def search(request):
    type = 0
    tripp = None
    destt = None
    oprr = None
    radio = request.session.get("radio", None)
    if radio == "form1":
        dest = request.session.get("dest1", None)
        type = 1
        tripp = Trip.objects.filter(T_Name__contains=dest)
    if radio == "form2":
        dest = request.session.get("dest2", None)
        type = 2
        destt = Destinations.objects.filter(Des_Name__contains=dest)
    if radio == "form3":
        dest = request.session.get("dest3", None)
        type = 3
        oprr = Tour_Operator.objects.filter(Operator_Name__contains=dest)
    context = {
        'username': request.session.get("username", None),
        'trips': tripp,
        'destinations': destt,
        'operators': oprr,
        'type': type,
    }
    return context



