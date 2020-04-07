from django.http import HttpResponse
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
        request.session["dest1"] = request.POST.get("destinationn1")
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
        return render(request, 'Frontend/index.html', context)


def login(request):
    label = " "
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
                return render(request, 'Frontend/login.html', context)
        else:
            context = {
                'username': request.session.get("username", None),
                'trips': Trip.objects.filter(display=True),
                'destinations': Destinations.objects.filter(display=True),
                'deals': Deal.objects.all(),
                'operators': Tour_Operator.objects.all(),
                'label': "Account Not Exist"
            }
            return render(request, 'Frontend/login.html', context)
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(display=True),
        'destinations': Destinations.objects.filter(display=True),
        'deals': Deal.objects.all(),
        'operators': Tour_Operator.objects.all(),
        'label': " "
    }
    return render(request, 'Frontend/login.html', context)


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
            return render(request, 'Frontend/register.html', context)
        else:
            c = User.objects.create(U_Name=username, U_pswd=password, U_email=email)
            request.session["username"] = c.U_Name
            return redirect(reverse('index', ))
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(display=True),
        'destinations': Destinations.objects.filter(display=True),
        'deals': Deal.objects.all(),
        'operators': Tour_Operator.objects.all(),
        'label': " "
    }
    return render(request, 'Frontend/register.html', context)


def logout(request):
    request.session.clear()
    return redirect(reverse('index'))


def trips1(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"] = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(noOfDays=1)
    }
    return render(request, 'Frontend/trips.html', context)


def trips2(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"] = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(noOfDays__gt=1),
    }
    return render(request, 'Frontend/trips.html', context)


def trip(request, articalvalue):
    obj = Trip.objects.get(Trip_Id=articalvalue)
    reviews=Review.objects.filter(reviewFor=obj.T_Name)

    Trip_History.objects.get_or_create(Trip_Name=obj)
    abc = Trip_History.objects.get(Trip_Name=obj)
    abc.count = abc.count + 1
    abc.save()
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"] = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'revs':reviews,
    }
    return render(request, 'Frontend/trip.html', context)


def operator(request, articalvalue):
    obj = Tour_Operator.objects.get(Op_Id=articalvalue)
    obj1 = Trip.objects.filter(event_host=obj)


    Tour_Operator_History.objects.get_or_create(Tour_Operator_Name=obj)
    abc = Tour_Operator_History.objects.get(Tour_Operator_Name=obj)
    abc.count = abc.count + 1
    abc.save()

    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"] = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'trips': obj1
    }
    return render(request, 'Frontend/operator.html', context)


def blog(request):
    return render(request, 'Frontend/blog_single.html')


def blogs(request):
    return render(request, 'Frontend/blog.html')


def Places(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"] = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'destinations': Destinations.objects.all(),
    }
    return render(request, 'Frontend/places.html', context)


def place(request, articalvalue):
    obj = Destinations.objects.get(Des_Id=articalvalue)
    obj1 = Trip.objects.filter(Dest=obj)

    Destination_History.objects.get_or_create(Destination_Name=obj)
    abc= Destination_History.objects.get(Destination_Name=obj)
    abc.count=abc.count+1
    abc.save()

    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"] = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'trips': obj1
    }
    return render(request, 'Frontend/place.html', context)


def touroperator(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"] = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = {
        'username': request.session.get("username", None),
        'operators': Tour_Operator.objects.all(),
    }
    return render(request, 'Frontend/touroperators.html', context)


def search_results(request):
    if request.method == 'POST':
        radio = request.POST.get("radio")
        request.session["radio"] = radio
        request.session["dest1"] = request.POST.get("destinationn1")
        request.session["dest2"] = request.POST.get("destinationn2")
        request.session["dest3"] = request.POST.get("destinationn3")
        return redirect(reverse('search_results'))
    context = search_result(request)
    return render(request, 'Frontend/search_results.html', context)


def search_result(request):
    type = 0
    tripp = None
    destt = None
    oprr = None
    radio = request.session.get("radio", None)
    if radio == "form1":
        dest = request.session.get("dest1", None)
        type = 1
        tripp = Trip.objects.filter(T_Name__contains=dest)
        if Trip.objects.filter(T_Name__exact=dest).count() is not 0:
            obj = Trip.objects.get(T_Name=dest)
            abc = Trip_History.objects.get(Trip_Name=obj)
            abc.count = abc.count + 1
            abc.save()
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


def Subscribe_NewsLetter(request):
    EmailID = request.GET['EmailID']
    data = "Enter Email"
    if '@' in EmailID:
        if NewsLetterEmails.objects.filter(Email=EmailID).count() is 0:
            NewsLetterEmails.objects.create(Email=EmailID)
            data = "You have Subscribed for Newsletter"
        else:
            data = "You have Already Subscribed"
    else:
        data = "Enter valid Email"
    return HttpResponse(data)


def News_single(request):
    return render(request, 'Frontend/News_single.html')


def News(request):
    context = {
        'news': newsfeed.objects.all(),
    }
    return render(request, 'Frontend/News.html',context)

def Scrap(request):
    import requests
    urls=News_Sraping_Url.objects.all()
    for url in urls:
        main_url=url.url
        # main_url = "https://newsapi.org/v2/everything?q=tourism-Pakistan&apiKey=5cc0c4c87f07471b8aa8acf009fbbd10"
        open_bbc_page = requests.get(main_url).json()
        article = open_bbc_page["articles"]
        results = []
        for ar in article:
            abc = newsfeed.objects.create()
            abc.Title = ar["title"]
            a = ar["source"]
            abc.Source = a["name"]
            abc.date = ar["publishedAt"]
            abc.description = ar["description"]
            abc.url = ar["urlToImage"]
            abc.save()
    return redirect(reverse('index'))