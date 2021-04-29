from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View
from . views import*

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')