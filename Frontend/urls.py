from django.conf.urls import url
from django.urls import path

from Frontend import admin
from Frontend.admin import event_admin_site

from Frontend.views import *

urlpatterns = [
    path('', index, name="index"),
    path('OneDay', trips1, name="trips1"),
    path('MultipleDays', trips2, name="trips2"),
    path('Trip/<slug:articalvalue>', trip, name="trip"),
    path('Destinations/Trip/<slug:articalvalue>', trip, name="trip"),
    path('Blogs', blogs, name="blogs"),
    path('Blog', blog, name="blog"),
    path('NewsFeed', News, name="News"),
    path('NewsFeed/<slug:articalvalue>', News_single, name="News_single"),
    path('Destinations/<slug:articalvalue>', place, name="place"),
    path('Places', Places, name="places"),
    path('Operator/<slug:articalvalue>', operator, name="operator"),
    path('Operator/Trip/<slug:articalvalue>', trip, name="trip"),
    path('Operator', touroperator, name="touroperator"),
    path('Login', login, name="login"),
    path('Register', register, name="register"),
    path('search_results', search_results, name="search_results"),
    path('logout', logout, name="logout"),
    url(r'^ajax/Subscribe_NewsLetter/$', Subscribe_NewsLetter, name='Subscribe_NewsLetter'),
    path('myoperator/', event_admin_site.urls),
    path('scrap', Scrap, name="Scrap"),

]