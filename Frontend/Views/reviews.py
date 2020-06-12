import json
from django.http import HttpResponse
from Frontend.models import *


def Add_Trip_Review(request):
    Trip_id = request.GET['Item_id']
    content = request.GET['content']
    rating = request.GET['ratings']
    print(rating)
    abc=TripReview.objects.create(reviewFor=Trip_id) # to add review in review database .an object is created
    abc.rev_good=content
    abc.rating=rating
    abc.reviewBy=request.session.get("username", "Anonymouse")
    abc.save()
    tripp=Trip.objects.get(Trip_Id=Trip_id) # get object from database by trip id to change its rating
    tripp.Total_Reviews=int(tripp.Total_Reviews)+1;
    tripp.Total_Rating=int(tripp.Total_Rating)+int(rating);
    rating = float(tripp.Total_Rating) / float(tripp.Total_Reviews);
    tripp.Average_Rating = "%.2f" % round(rating, 2)
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
    operator=Tour_Operator.objects.get(Op_Id=Trip_id)
    operator.Total_Reviews=int(operator.Total_Reviews)+1;
    operator.Total_Rating=int(operator.Total_Rating)+int(rating);
    rating = float(operator.Total_Rating) / float(operator.Total_Reviews);
    operator.Average_Rating = "%.2f" % round(rating, 2)
    operator.save();
    data = {
        'message':"Comment Added Sucessfully",
        'totalreviews':operator.Total_Reviews,
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
    destination=Destinations.objects.get(Des_Id=Trip_id)
    destination.Total_Reviews=int(destination.Total_Reviews)+1;
    destination.Total_Rating=int(destination.Total_Rating)+int(rating);
    rating=float(destination.Total_Rating) / float(destination.Total_Reviews);
    destination.Average_Rating="%.2f" % round(rating, 2)
    destination.save();
    data = {
        'message':"Comment Added Sucessfully",
        'totalreviews':destination.Total_Reviews,
    }
    return HttpResponse(json.dumps(data))
