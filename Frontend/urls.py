from django.urls import path
from Frontend.views import *

urlpatterns = [
    path('', index, name="index"),
    path('a', trips, name="trips"),
    path('b', trip, name="trip"),
    path('c', blogs, name="blogs"),
    path('d', blog, name="blog"),
    path('e', location, name="location"),
    path('f', login, name="login"),
    path('g', register, name="register"),
    path('h', search_results, name="search_results"),


]