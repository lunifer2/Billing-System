from django.contrib import admin
from .models import Bill, Order, Item, CustomUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Bill)
admin.site.register(Order)
admin.site.register(Item)