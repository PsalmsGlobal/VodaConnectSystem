from django.urls import path, include
from . import views

app_name='auth'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login")



]
