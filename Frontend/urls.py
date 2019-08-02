from django.urls import path
from Frontend.views import *

urlpatterns = [
    path('', index, name="index"),
]