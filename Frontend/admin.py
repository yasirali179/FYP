from django.contrib import admin

# Register your models here.
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
