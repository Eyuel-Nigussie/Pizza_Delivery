from django.contrib import admin
from django.urls import path, include #include helps us to access urls in external apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('orders/', include('orders.urls')),
]
