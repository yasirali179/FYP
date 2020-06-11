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
    abc = return_or_create_cart(request)
    if request.method == 'POST':
        if abc.items_in_cart is not None:
            return redirect(reverse('orderConfirm'))
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
    print("idr")
    abc=return_or_create_cart(request)
    message=" "
    total=0
    if abc is None:
        message="Login First"
    else:
        item_id = request.GET['Item_id']
        quantity = request.GET['quantity']
        print(item_id)
        print(quantity)
       # if int(quantity) is 0:
           # abc.items_in_cart=""
           # abc.quantity=0
           # abc.Total=0
          #  abc.save()
         #   message = "removed"
        #else:
        iteme = Trip.objects.get(Trip_Id=item_id)
        abc.items_in_cart = iteme;
        abc.quantity = quantity;
        if iteme.Item_Is_Discount:
            abc.Total = iteme.Discount_Price * int(quantity)
        else:
            abc.Total = iteme.price * int(quantity)
        abc.save();
        message = "Added"
        total=abc.Total
    data ={
        'message': message,
        'PriceTotal': total,
    }
    return HttpResponse(json.dumps(data))


def compare(request,articalvalue1,articalvalue2):
    onetrip=False;
    if articalvalue2 is 'Z':
        onetrip=True
    if request.method == 'POST':
        radio = request.POST.get("trip2")
        print(radio)
    context={
        't':Trip.objects.get(Trip_Id=articalvalue1),
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
            return redirect(reverse('shop'))

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