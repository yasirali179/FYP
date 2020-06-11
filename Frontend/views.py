import json
import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView

from Frontend.models import *
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from Frontend.recommender import recommend
from Frontend.serializers import UserSerializer
from rest_framework import status

from babel.dates import format_date


def index(request):
    #recommend(dest_id=3, num=5)
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(display=True),
        'destinations': Destinations.objects.filter(display=True),
        'deals': Deal.objects.all(),
        'operators': Tour_Operator.objects.all(),
    }
    return render(request, 'Frontend/index.html', context)


def OneDay(request):
    trips=Trip.objects.filter(noOfDays=1, active=True, Departure_Date__gte=datetime.datetime.now().date())
    for t in trips:
        t.startDate=format_date(t.Departure_Date, locale='en')
        t.save();
    context = {
        'username': request.session.get("username", None),
        'trips':trips,
    }
    return render(request, 'Frontend/trips.html', context)


def MultipleDays(request):
    trips = Trip.objects.filter(noOfDays__gt=1,active=True,Departure_Date__gte=datetime.datetime.now().date())
    for t in trips:
        t.startDate = format_date(t.Departure_Date, locale='en')
        t.save();
    context = {
        'username': request.session.get("username", None),
        'trips': trips,
    }
    return render(request, 'Frontend/trips.html', context)


def trip(request, articalvalue):
    obj = Trip.objects.get(Trip_Id=articalvalue)

    Trip_History.objects.get_or_create(Trip_Name=obj)
    abc = Trip_History.objects.get(Trip_Name=obj)
    abc.count = abc.count + 1
    abc.save()

    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'revs':TripReview.objects.filter(reviewFor=obj.Trip_Id),
    }
    return render(request, 'Frontend/trip.html', context)


def operator(request, articalvalue):
    obj = Tour_Operator.objects.get(Op_Id=articalvalue)
    obj1 = Trip.objects.filter(event_host=obj)
    Tour_Operator_History.objects.get_or_create(Tour_Operator_Name=obj)
    abc = Tour_Operator_History.objects.get(Tour_Operator_Name=obj)
    abc.count = abc.count + 1
    abc.save()
    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'trips': obj1,
        'revs': TourCompanyReview.objects.filter(reviewFor=obj.Op_Id),
    }
    return render(request, 'Frontend/operator.html', context)


def blog(request):
    return render(request, 'Frontend/blog_single.html')


def blogs(request):
    return render(request, 'Frontend/blog.html')


def Places(request):
    abc=Destinations.objects.all()
    for a in abc:
        a.Total_Trips=Trip.objects.filter(Dest=a).count()
        a.save();
    context = {
        'username': request.session.get("username", None),
        'destinations':abc,
    }
    return render(request, 'Frontend/places.html', context)


def place(request, articalvalue):
    obj = Destinations.objects.get(Des_Id=articalvalue)
    obj1 = Trip.objects.filter(Dest=obj)

    Destination_History.objects.get_or_create(Destination_Name=obj)
    abc= Destination_History.objects.get(Destination_Name=obj)
    abc.count=abc.count+1
    abc.save()
    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'trips': obj1,
        'revs': DestincationReview.objects.filter(reviewFor=obj.Des_Id),
    }
    return render(request, 'Frontend/place.html', context)


def touroperator(request):
    abc=Tour_Operator.objects.all()
    for a in abc:
        a.Total_Trips=Trip.objects.filter(event_host=a).count()
        a.save();
    context = {
        'username': request.session.get("username", None),
        'operators':abc,

    }
    return render(request, 'Frontend/touroperators.html', context)



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

def tripScrap(request):
    TripScrap.objects.all().delete()
    my_url = 'https://pakistantourntravel.com/tours/hunza-valley-tour-package/'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "wpb_column vc_column_container vc_col-sm-4"})

    for container in containers:
        print(container.div.h2.a.text)
        price = container.findAll("div", {"class": "ts-teaser-text ts-teaser-auto"})
        print(price[0].text)

    myurl = 'https://www.travelo.pk/packages.php'
    myurl1 = 'https://www.travelo.pk'
    uClients = uReq(myurl)
    pageHtml = uClients.read()
    uClients.close()
    pageSoup = soup(pageHtml, "html.parser")
    Containers = pageSoup.findAll("div", {"class": "col-sm-4"})

    for Container in Containers:
        abc=TripScrap.objects.create();
        abc.T_Name=Container.div.h5.text
        pic=myurl1 + '/' + Container.div.img["src"]
        abc.pic=pic
        aaa=Container.div.p.text
        aaa = " ".join(aaa)
        digits = [int(s) for s in aaa.split() if s.isdigit()]
        abc.noOfDays=digits[0]
        if len(digits) >=2:
            abc.noOfNights=digits[1]
        else:
            abc.noOfNights = 1
        price = Container.findAll("div", {"class": "price"})
        abc.price=price[0].text[1:7]
        abc.startLocation="Lahore"
        abc.startDate="24th July"
        abc.save()
    return render(request,"Frontend/tripscrap.html",{'trips':TripScrap.objects.all(),})
    #return redirect(reverse('index'))

def newsScrap(request):
    newsfeed.objects.all().delete()
    import requests
    urls = News_Sraping_Url.objects.all()
    for url in urls:
        main_url = url.url
        main_url = "https://newsapi.org/v2/everything?q=tourism-Pakistan&apiKey=5cc0c4c87f07471b8aa8acf009fbbd10"
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
            urll=ar["urlToImage"]
            if urll is not None:
                abc.url = urll
            else:
                abc.url = " "
            abc.save()
    context = {
        'news': newsfeed.objects.all(),
    }
    return render(request, 'Frontend/News.html', context)

def Add_Review(request):
    Trip_id = request.GET['Item_id']
    content = request.GET['content']
    rating = request.GET['ratings']
    abc=TripReview.objects.create(reviewFor=Trip_id)
    abc.rev_good=content
    abc.rating=rating
    abc.reviewBy=request.session.get("username", "Anonymouse")
    abc.save()
    tripp=Trip.objects.get(Trip_Id=Trip_id)
    tripp.Total_Reviews=int(tripp.Total_Reviews)+1;
    tripp.Total_Rating=int(tripp.Total_Rating)+int(rating);
    tripp.Average_Rating= float(tripp.Total_Rating)/float(tripp.Total_Reviews);
    tripp.save();
    data = {
        'message':"Comment Added Sucessfully",
        'totalreviews':tripp.Total_Reviews,
    }
    return HttpResponse(json.dumps(data))

def sorting(request):
    obj = Trip_History.objects.order_by('-count')
    print("----------------------------------------")
    print("Top trending Trips based on User data ")
    i = 1
    for x in obj:
        print(i, x.Trip_Name, x.count, )
        i = i + 1
    obj = Destination_History.objects.order_by('-count')
    print("----------------------------------------")
    print("Top trending Destinations based on User data  ")
    i = 1
    for x in obj:
        print(i, x.Destination_Name, x.count, )
        i = i + 1

    obj = Tour_Operator_History.objects.order_by('-count')
    print("----------------------------------------")
    print("Top trending Tour Operators based on User data ")
    i = 1
    for x in obj:
        print(i, x.Tour_Operator_Name, x.count, )
        i = i + 1
    return redirect(reverse('index'))

def sorting1(request):
    obj=Trip.objects.order_by('-Average_Rating')
    print("----------------------------------------")
    print("Top trending Trips based on User Rating  ")
    i = 1
    for x in obj:
        print(i, x.T_Name, x.Average_Rating, )
        i = i + 1
    obj = Destinations.objects.order_by('-Average_Rating')
    print("----------------------------------------")
    print("Top trending Destinations based on User Rating")
    i = 1
    for x in obj:
        print(i, x.Des_Name, x.Average_Rating, )
        i = i + 1

    obj = Tour_Operator.objects.order_by('-Average_Rating')
    print("----------------------------------------")
    print("Top trending Tour Operators based on User Rating")
    i = 1
    for x in obj:
        print(i, x.Operator_Name, x.Average_Rating, )
        i = i + 1
    return redirect(reverse('index'))

def get_places(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = Trip.objects.filter(T_Name__icontains=q)
    results = []
    for pl in places:
      place_json = {}
      place_json = pl.T_Name + "," + pl.price
      results.append(place_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

