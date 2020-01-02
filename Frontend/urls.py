from django.urls import path
from Frontend.views import *

urlpatterns = [
    path('', index, name="index"),
    path('Trips', trips, name="trips"),
    path('Trip', trip, name="trip"),
    path('Blogs', blogs, name="blogs"),
    path('Blog', blog, name="blog"),
    path('Place', place, name="place"),
    path('Places', Places, name="places"),
    path('TourOperator', touroperator, name="touroperator"),
    path('Login', login, name="login"),
    path('Register', register, name="register"),
    path('search_results', search_results, name="search_results"),
    path('logout', logout, name="logout"),

]