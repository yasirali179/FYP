from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'Frontend/index.html')

def trips(request):
    return render(request,'Frontend/trips.html')
def trip(request):
    return render(request,'Frontend/trip.html')
def blog(request):
    return render(request,'Frontend/blog_single.html')
def blogs(request):
    return render(request,'Frontend/blog.html')

def Dest(request):
    return render(request, 'Frontend/Dest.html')
def Destinatins(request):
    return render(request, 'Frontend/Destinatins.html')
def login(request):
    return render(request,'Frontend/login.html')
def register(request):
    return render(request,'Frontend/register.html')

def search_results(request):
    return render(request,'Frontend/search_results.html')


