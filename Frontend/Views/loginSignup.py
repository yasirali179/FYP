import json
from django.shortcuts import render, redirect
from django.urls import reverse
from Frontend.models import *
from django.http import HttpResponse


def login(request):
    label = " "
    message=""
    if request.session.get("username", None) is not None:
        return redirect(reverse('index'))
    nsname = request.GET['username']
    password = request.GET['password']
    abc = User.objects.filter(U_Name__iexact=nsname).count()
    if abc is not 0:
        d = User.objects.get(U_Name__iexact=nsname)
        if d.U_pswd == password:
            request.session["username"] = d.U_Name
            message="sucessfully";
        else:
            message= "password Error"
    else:
        message= "Account Not Exist"
    data={
        'message':message,
    }
    return HttpResponse(json.dumps(data))


def register(request):
    message=""
    username = request.GET['username']
    email = request.GET['password']
    password = request.GET['password']
    abc = User.objects.filter(U_Name__exact=username).count()
    if abc is not 0:
         message= "Already Exist"
    else:
        c = User.objects.create(U_Name=username, U_pswd=password, U_email=email)
        request.session["username"] = c.U_Name
        message="sucessfully"
    data = {
        'message': message,
    }
    return HttpResponse(json.dumps(data))


def logout(request):
    request.session.clear()
    return redirect(reverse('index'))
