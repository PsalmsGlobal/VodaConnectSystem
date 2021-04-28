from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Authentication.urls')),
    path('', include('SubscriberInventory.urls')),
]

admin.site.site_title = "GPG site admin"
admin.site.site_header = "GPG Administration"