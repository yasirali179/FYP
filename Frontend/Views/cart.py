import json
import datetime
import random

from django.shortcuts import render, redirect
from django.urls import reverse
from Frontend.models import *
from django.http import HttpResponse


def return_or_create_cart(request):
    PH=request.session.get("username", None)
    if PH is None:
        return None
    else:
        Custm = User.objects.get(U_Name=PH)
        Cart.objects.get_or_create(Cust=Custm)
        return Cart.objects.get(Cust=Custm)


def cart(request ):
    abc = return_or_create_cart(request)    # create cart of register user or get cart object is already created
    if request.method == 'POST':           # confirm order
        if abc.items_in_cart is not None:
            return redirect(reverse('orderConfirm')) #redirect to order
    if abc is not None:
        context = {
                    'items': abc.items_in_cart,
                    'quantity':abc.quantity,
                   'total': abc.Total,
                   'username': request.session.get("username", None),
                   }
    else:
        context = {'users': None, 'Total': 0, 'username': request.session.get("username", None)}

    return render(request, 'Frontend/BookingOrders/cart.html', context)

def Add_in_Cart(request):
    abc=return_or_create_cart(request)  # create cart of register user or get cart object is already created
    message=" "
    total=0
    if abc is None:
        message="Login First"
    else:
        trip = request.GET['Item_id']
        quantity = request.GET['quantity']  #get item_id and quantity from frontend through Ajax query
        tripp = Trip.objects.get(Trip_Id=trip) #get trip object for database
        abc.items_in_cart = tripp;
        abc.quantity = quantity;
        if tripp.Item_Is_Discount:
            abc.Total = tripp.Discount_Price * int(quantity)
        else:
            abc.Total = tripp.price * int(quantity)
        abc.save();
        message = "Added"
        total=abc.Total
    data ={
        'message': message,
        'PriceTotal': total,
    }
    return HttpResponse(json.dumps(data)) #dumps data in jason format to frontend


def compare(request,articalvalue1,articalvalue2):
    context={
        't':Trip.objects.get(Trip_Id=articalvalue1),
        'u': Trip.objects.get(Trip_Id=articalvalue2)
    }
    return render(request, 'Frontend/comparison.html', context)


def orderConfirm(request):
    PH = request.session.get("username", None)

    if PH is None:
        return redirect(reverse('login'))
    abc = return_or_create_cart(request)
    if request.method == 'POST':
        if abc.items_in_cart is not None:
            edf = Order.objects.create(Cust=abc.Cust)
            edf.O_Total = abc.Total
            edf.quantity=abc.quantity
            edf.items_in_order=abc.items_in_cart
            abc.items_in_cart.No_of_Seats=abc.items_in_cart.No_of_Seats-abc.quantity
            abc.items_in_cart.save();
            now = datetime.datetime.now()
            any = abc.Total * random.randint(121, 800)
            edf.O_id = str(abc.items_in_cart.No_of_Seats) + str(now.minute) + str(now.microsecond) + str(
                random.randint(1000, 8000)) + str(now.day) + str(now.second) + str(any) + str(
                random.randint(1000, 8000))
            edf.save()
            abc.items_in_cart=None;
            abc.quantity=0;
            abc.Total=0;
            abc.save()
            return redirect('OrderStatus', edf.O_id)
        else:
            return redirect(reverse('cart'))
    else:
        cust = User.objects.get(U_Name=PH)
        if abc.items_in_cart is None:
            return redirect(reverse('index'))

    context = {
        'data': abc,
        'username': request.session.get("username", None),
    }
    return render(request, 'Frontend/BookingOrders/orderconfirm.html', context)

def OrderStatus(request,OrderID):
    if Order.objects.filter(O_id=OrderID).count() is not 0:
        a=Order.objects.get(O_id=OrderID)
        return render(request, 'frontend/BookingOrders/orderdetails.html',{'order': a,'username': request.session.get("username", None)});
    else:
        return redirect(reverse('OrderMain'))

def OrderMain(request):
    PH = request.session.get("username", None)
    abc = None
    message=""
    if PH is None:
        message="login"
    else:
        custm = User.objects.get(U_Name=PH)
        abc=Order.objects.filter(Cust=custm,Finish=False)
        print(abc)
    return render(request, 'frontend/BookingOrders/Orderlist.html',{'orders':abc,'username': request.session.get("username", None),'message':message});

def apis(request,a):
    data={
       'abc':a,
    }
    return HttpResponse(json.dumps(data))