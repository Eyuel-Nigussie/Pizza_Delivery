from django.contrib import admin
from .models import Order

# Register your models here.

#registering model to admin page with customized
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['size','order_status', 'quantity', 'created_at']
    list_filter=['created_at','order_status','size',]