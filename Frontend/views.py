from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST.get("datepicker11")
        print(username)
    return render(request,'Frontend/index.html')


def login(request):
    if request.method == 'POST':

        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email+password)
    return render(request,'Frontend/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get("ns_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(username+email+password)
    return render(request,'Frontend/register.html')




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


def search_results(request):
    return render(request,'Frontend/search_results.html')


