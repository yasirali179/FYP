import json
from django.http import HttpResponse
from Frontend.models import *


def Add_Trip_Review(request):
    Trip_id = request.GET['Item_id']
    content = request.GET['content']
    rating = request.GET['ratings']
    print(rating)
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


def Add_TourOp_Review(request):
    Trip_id = request.GET['Item_id']
    content = request.GET['content']
    rating = request.GET['ratings']
    print(rating)
    abc=TourCompanyReview.objects.create(reviewFor=Trip_id)
    abc.rev_good=content
    abc.rating=rating
    abc.reviewBy=request.session.get("username", "Anonymouse")
    abc.save()
    tripp=Tour_Operator.objects.get(Op_Id=Trip_id)
    tripp.Total_Reviews=int(tripp.Total_Reviews)+1;
    tripp.Total_Rating=int(tripp.Total_Rating)+int(rating);
    tripp.Average_Rating= float(tripp.Total_Rating)/float(tripp.Total_Reviews);
    tripp.save();
    data = {
        'message':"Comment Added Sucessfully",
        'totalreviews':tripp.Total_Reviews,
    }
    return HttpResponse(json.dumps(data))


def Add_Dest_Review(request):
    Trip_id = request.GET['Item_id']
    content = request.GET['content']
    rating = request.GET['ratings']
    print(rating)
    abc=DestincationReview.objects.create(reviewFor=Trip_id)
    abc.rev_good=content
    abc.rating=rating
    abc.reviewBy=request.session.get("username", "Anonymouse")
    abc.save()
    tripp=Destinations.objects.get(Des_Id=Trip_id)
    tripp.Total_Reviews=int(tripp.Total_Reviews)+1;
    tripp.Total_Rating=int(tripp.Total_Rating)+int(rating);
    tripp.Average_Rating= float(tripp.Total_Rating)/float(tripp.Total_Reviews);
    tripp.save();
    data = {
        'message':"Comment Added Sucessfully",
        'totalreviews':tripp.Total_Reviews,
    }
    return HttpResponse(json.dumps(data))
