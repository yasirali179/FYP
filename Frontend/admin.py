from django import forms
from django.contrib import admin
from django.contrib.admin import AdminSite

admin.site.site_header="Trip Advisor Admin panel"
admin.site.site_title = "Trip Advisor Admin panel"
admin.site.index_title = "Welcome to Trip Advisor Admin panel"

from Frontend.models import*


class my(admin.ModelAdmin):
    list_display = ('T_Name','Dest','event_host', 'active')
    list_filter = ('Dest','event_host', 'active')

admin.site.register(User)
admin.site.register(Images)
admin.site.register(Required_Gear)
admin.site.register(Services)
admin.site.register(Activities)
admin.site.register(Tour_Operator)
admin.site.register(Review)
admin.site.register(Trip,my)
admin.site.register(Destinations)
admin.site.register(Deal)
admin.site.register(Destination_History)
admin.site.register(Trip_History)
admin.site.register(Tour_Operator_History)
admin.site.register(newsfeed)
admin.site.register(NewsLetterEmails)
admin.site.register(News_Sraping_Url)







class EventAdminSite(AdminSite):
    site_header = "Tour Operator Admin"
    site_title = "Tour Operator Admin Portal"
    index_title = "Welcome to Tour Operator Portal"

event_admin_site = EventAdminSite(name='event_admin')

class abc(admin.ModelAdmin):
    exclude = ('active', )



event_admin_site.register(Trip,abc)


