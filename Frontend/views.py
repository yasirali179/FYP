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
from Frontend.serializers import UserSerializer
from rest_framework import status
















def index(request):

    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(display=True),
        'destinations': Destinations.objects.filter(display=True),
        'deals': Deal.objects.all(),
        'operators': Tour_Operator.objects.all(),
    }
    return render(request, 'Frontend/index.html', context)


def OneDay(request):
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(noOfDays=1,active=True,Departure_Date__gte=datetime.datetime.now().date())
    }
    return render(request, 'Frontend/trips.html', context)


def MultipleDays(request):
    context = {
        'username': request.session.get("username", None),
        'trips': Trip.objects.filter(noOfDays__gt=1,active=True,Departure_Date__gte=datetime.datetime.now().date()),
    }
    return render(request, 'Frontend/trips.html', context)


def trip(request, articalvalue):
    obj = Trip.objects.get(Trip_Id=articalvalue)
    print(obj.Departure_Date)
    reviews=Review.objects.filter(reviewFor=obj.Trip_Id)
    Trip_History.objects.get_or_create(Trip_Name=obj)
    abc = Trip_History.objects.get(Trip_Name=obj)
    abc.count = abc.count + 1
    abc.save()
    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'revs':reviews,
        'totalreviews': reviews.count(),
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
        'trips': obj1
    }
    return render(request, 'Frontend/operator.html', context)


def blog(request):
    return render(request, 'Frontend/blog_single.html')


def blogs(request):
    return render(request, 'Frontend/blog.html')


def Places(request):

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
    context = {
        'username': request.session.get("username", None),
        'p': obj,
        'trips': obj1
    }
    return render(request, 'Frontend/place.html', context)


def touroperator(request):

    context = {
        'username': request.session.get("username", None),
        'operators': Tour_Operator.objects.all(),
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
    my_url = 'https://pakistantourntravel.com/tours/hunza-valley-tour-package/'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "wpb_column vc_column_container vc_col-sm-4"})
    # print(len(containers))

    for container in containers:
        print(container.div.h2.a.text)
        price = container.findAll("div", {"class": "ts-teaser-text ts-teaser-auto"})
        print(price[0].text)

    myurl = 'https://www.travelo.pk/packages.php'
    uClients = uReq(myurl)
    pageHtml = uClients.read()
    uClients.close()
    pageSoup = soup(pageHtml, "html.parser")
    Containers = pageSoup.findAll("div", {"class": "col-sm-4"})
    # print(len(Containers))

    for Container in Containers:
        print(Container.div.img["alt"])
        price = Container.findAll("div", {"class": "price"})
        print(price[0].text)

    return redirect(reverse('index'))

def newsScrap(request):
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
            abc.url = ar["urlToImage"]
            abc.save()
    return redirect(reverse('index'))

def Add_Review(request):
    Trip_name = request.GET['Item_id']
    content = request.GET['content']
    abc=Review.objects.create(reviewFor=Trip_name)
    abc.rev_good=content
    abc.reviewBy=request.session.get("username", "Anonymouse")
    abc.save()

    data = {
        'message':"Comment Added Sucessfully",
        'totalreviews':Review.objects.filter(reviewFor=Trip_name).count(),
    }
    return HttpResponse(json.dumps(data))

def sorting(request):
    obj = Trip_History.objects.order_by('-count')
    print("----------------------------------------")
    print("Top trending Trips  ")
    i = 1
    for x in obj:
        print(i, x.Trip_Name, x.count, )
        i = i + 1
    obj = Destination_History.objects.order_by('-count')
    print("----------------------------------------")
    print("Top trending Destinations  ")
    i = 1
    for x in obj:
        print(i, x.Destination_Name, x.count, )
        i = i + 1

    obj = Tour_Operator_History.objects.order_by('-count')
    print("----------------------------------------")
    print("Top trending Tour Operators ")
    i = 1
    for x in obj:
        print(i, x.Tour_Operator_Name, x.count, )
        i = i + 1
    return redirect(reverse('index'))

def get_places(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    print(q)
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

