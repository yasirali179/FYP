from django.conf.urls import url
from django.urls import path
from Frontend.admin import event_admin_site
from Frontend.Views.cart import *
from Frontend.views import *
from Frontend.Views.loginSignup import *
from Frontend.Views.search import *
urlpatterns = [
    path('', index, name="index"),
    path('OneDay', trips1, name="trips1"),
    path('MultipleDays', trips2, name="trips2"),
    path('Trip/<slug:articalvalue>', trip, name="trip"),
    path('Destinations/Trip/<slug:articalvalue>', trip, name="trip"),
    path('cart/Trip/<slug:articalvalue>', trip, name="trip"),
    path('Blogs', blogs, name="blogs"),
    path('Blog', blog, name="blog"),
    path('NewsFeed', News, name="News"),
    path('NewsFeed/<slug:articalvalue>', News_single, name="News_single"),
    path('Destinations/<slug:articalvalue>', place, name="place"),
    path('Places', Places, name="places"),
    path('Operator/<slug:articalvalue>', operator, name="operator"),
    path('Operator/Trip/<slug:articalvalue>', trip, name="trip"),
    path('Operator', touroperator, name="touroperator"),
    #path('Login', login, name="login"),
    #path('Register', register, name="register"),
    path('search_results', search_results, name="search_results"),
    url(r'^ajax/search/$', search, name='search'),
    path('logout', logout, name="logout"),
    url(r'^ajax/Subscribe_NewsLetter/$', Subscribe_NewsLetter, name='Subscribe_NewsLetter'),
    url(r'^ajax/Add_Review/$', Add_Review, name='Add_Review'),
    path('myoperator/', event_admin_site.urls),
    path('tripscrap/', tripScrap, name="Scrap"),
    path('newsscrap/', newsScrap, name="newsScrap"),
    path('sort/', sorting, name="sort"),
    path('cart/', cart, name="cart"),
    path('compare/<slug:articalvalue1>-vs-<slug:articalvalue2>', compare, name="compare"),
    url(r'^ajax/Add_in_Cart/$', Add_in_Cart, name='Add_in_Cart'),
    url(r'^ajax/range/$', rangess, name='range'),
    url(r'^api/get_places/', get_places, name='get_places'),
    url(r'^ajax/Login/$', login, name='search'),
    url(r'^ajax/signup/$', register, name='search'),
    path('orders/', orderConfirm, name='orderConfirm'),
    path('OrderDetails/<slug:OrderID>', OrderStatus,name="OrderStatus"),
    path('OrderMain/', OrderMain, name="OrderMain"),
    path('api/',UserList.as_view()),
    path('apis/', apis, name="apis"),
]