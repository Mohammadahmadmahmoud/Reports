from django.contrib import admin
from .models import Customer,Announcement,Tag,Order
# Register your models here.
admin.site.register(Customer)
admin.site.register(Announcement)
admin.site.register(Tag)
admin.site.register(Order)
