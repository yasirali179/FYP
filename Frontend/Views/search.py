import json
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from Frontend.models import *
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def search_results(request):
    radio = request.session.get("radio", None)
    input = request.session.get("input", None)
    print(radio)
    print(input)
    tripp = None
    destt = None
    oprr = None
    if radio is "1":
        tripp = Trip.objects.filter(T_Name__contains=input)
        if Trip.objects.filter(T_Name__exact=input).count() is not 0:
            obj = Trip.objects.get(T_Name=input)
            abc = Trip_History.objects.get(Trip_Name=obj)
            abc.count = abc.count + 1
            abc.save()
    if radio == "2":
        if input == "1":
            tripp = Trip.objects.filter(price__gte=0 , price__lte=5000)
            print(tripp)
        if input == "2":
            tripp = Trip.objects.filter(price__gte=5001,price__lte=10000)
            print(tripp)
        if input == "3":
            tripp = Trip.objects.filter(price__gte=10001,price__lte=15000)
        if input == "4":
            tripp = Trip.objects.filter(price__gte=15001,price__lte=20000)
    if radio == "3":
        destt = Destinations.objects.filter(Des_Name__contains=input)
    if radio == "4":
        print("abc")
    if radio == "5":
        oprr = Tour_Operator.objects.filter(Operator_Name__contains=input)

    if radio == "6":
        tripp = Trip.objects.filter(Departure_Date__gte=input)
    context = {
        'username': request.session.get("username", None),
        'trips': tripp,
        'destinations': destt,
        'operators': oprr,
    }
    return render(request, 'Frontend/search_results.html', context)



def search(request):
    request.session["radio"]  =request.GET['radio']
    request.session["input"]  =request.GET['input']

    data = {
        'message': "Sucessfully",
    }
    return HttpResponse(json.dumps(data))

def rangess(request):
    request.session["sort"]  = request.GET['content']
    data = {
        'message': "Comment Added Sucessfully",
    }
    return HttpResponse(json.dumps(data))

