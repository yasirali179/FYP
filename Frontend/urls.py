from django.urls import path
from Frontend.views import *

urlpatterns = [
    path('', index, name="index"),
    path('trips', trips, name="trips"),
    path('trip', trip, name="trip"),


]