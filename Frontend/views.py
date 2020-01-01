from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Frontend/index.html')

def trips(request):
    return render(request,'Frontend/trips.html')
def trip(request):
    return render(request,'Frontend/trip.html')

