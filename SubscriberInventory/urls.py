from django.urls import path
from . import views

app_name='subsInv'
urlpatterns = [

    path('', views.HomeView.as_view(), name='home' ),
    path('voip/inventory/', views.VoipInventoryView.as_view(), name='voip_inventory'),
    path('activation/details/', views.ActivationDetailsView.as_view(), name='activation_details'),



]