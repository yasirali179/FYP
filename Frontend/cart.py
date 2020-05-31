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


def cart(request ):
    abc = return_or_create_cart(request)
    if request.method == 'POST':
        if abc.items_in_cart.count() is not 0:
            return redirect(reverse('OrderConfirm'))
    if abc is not None:
        context = {
                    'items': abc.items_in_cart,
                    'quantity':abc.quantity,
                   'total': abc.Total,
                   'username': request.session.get("username", None),
                   }
    else:
        context = {'users': None, 'Total': 0, 'username': request.session.get("username", None)}

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
       # if int(quantity) is 0:
           # abc.items_in_cart=""
           # abc.quantity=0
           # abc.Total=0
          #  abc.save()
         #   message = "removed"
        #else:
        iteme = Trip.objects.get(Trip_Id=item_id)
        abc.items_in_cart=iteme;
        abc.quantity=quantity;
        if iteme.Item_Is_Discount:
            abc.Total = iteme.Discount_Price * int(quantity)
        else:
            abc.Total = iteme.price * int(quantity)
        abc.save();
        message = "Added"
    data ={
        'message': message,
        'PriceTotal': abc.Total,
        'myname':abc,
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
    return render(request, 'Frontend/comparison.html',context)