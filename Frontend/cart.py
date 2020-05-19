import json
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

def ItemCount(request):
    C = return_or_create_cart(request)
    items_in_cartt = 0
    if C is not None:
        items_in_cartt = C.items_in_cart.count()
    return items_in_cartt



def cart(request):
    abc = return_or_create_cart(request)
    if request.method == 'POST':
        if abc.items_in_cart.count() is not 0:
            return redirect(reverse('OrderConfirm'))
    if abc is not None:
        context = {'users': Quantity.objects.filter(cart=abc),
                   'Total': abc.Total,
                   'username': request.session.get("username", None),
                   'Count': abc.items_in_cart.count(),
                   }
    else:
        context = {'users': None, 'Total': 0, 'username': request.session.get("username", None), 'Count': 0,}

    return render(request,'Frontend/cart.html',context)



def Add_in_Cart(request):
    abc=return_or_create_cart(request)
    message=" "
    asd=0
    mytotal = 0
    wetotal=0
    if abc is None:
        message="Login First"
    else:
        item_id = request.GET['Item_id']
        quantity = request.GET['quantity']
        iteme = Trip.objects.get(Trip_Id=item_id)
        Quantity.objects.get_or_create(items=iteme,cart=abc)
        all=Quantity.objects.get(items=iteme,cart=abc)
        all.quantity=int(quantity)
        all.save()
        abc.Total=0
        for a in Quantity.objects.filter(cart=abc):
            if a.items.Item_Is_Discount:
                a.total = a.items.Discount_Price * a.quantity
            else:
                a.total=a.items.price*a.quantity
            abc.Total+=a.total
            a.save()
            abc.save()
        abc.save()
        message = "Added"
        asd = abc.items_in_cart.count()
        if iteme.Item_Is_Discount:
            mytotal = iteme.Discount_Price * int(quantity)
        else:
            mytotal = iteme.price * int(quantity)
        wetotal=abc.Total
    data ={
        'message': message,
        'Count': asd,
        'mytotal': mytotal,
        'PriceTotal': wetotal
    }
    return HttpResponse(json.dumps(data))

def Remove_from_Cart(request):
    abc=return_or_create_cart(request)
    message = " "
    asd = 0
    PriceTotal=0
    if abc is None:
        message = "Login First"
    else:
        item_id = request.GET['Item_id']
        iteme = Trip.objects.get(Trip_Id=item_id)
        Quantity.objects.filter(items=iteme,cart=abc).delete()
        abc.Total=0
        for a in Quantity.objects.filter(cart=abc):
            if a.items.Item_Is_Discount:
                a.total = a.items.Item_Discount * a.quantity
            else:
                a.total = a.items.Item_Price * a.quantity
            abc.Total+=a.total
            a.save()
            abc.save()
        abc.save()
    data = {
        'Count': abc.items_in_cart.count(),
        'PriceTotal': abc.Total,
    }
    return HttpResponse(json.dumps(data))