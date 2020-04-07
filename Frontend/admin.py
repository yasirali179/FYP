from django import forms
from django.contrib import admin
from django.contrib.admin import AdminSite

admin.site.site_header="Trip Advisor Admin panel"

from Frontend.models import*


admin.site.register(User)
admin.site.register(Images)
admin.site.register(Required_Gear)
admin.site.register(Services)
admin.site.register(Activities)
admin.site.register(Tour_Operator)
admin.site.register(Review)
admin.site.register(Trip)
admin.site.register(Destinations)
admin.site.register(Deal)
admin.site.register(Destination_History)
admin.site.register(Trip_History)
admin.site.register(Tour_Operator_History)
admin.site.register(newsfeed)
admin.site.register(NewsLetterEmails)


class EventAdminSite(AdminSite):
    site_header = "Tour Operator Admin Panel"
    site_title = "Tour Operator Admin Panel"
    index_title = "Welcome to Tour Operator Admin Panel"

event_admin_site = EventAdminSite(name='Tour Operator')


event_admin_site.register(NewsLetterEmails)
