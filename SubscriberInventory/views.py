from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View
from . views import*


class HomeView(View):
    def get(self, request):
        return render(request, 'VOIPLine/home.html')

class VoipInventoryView(View):
    def get(self, request):
        return render(request, 'VOIPLine/voip_inventory.html')

class ActivationDetailsView(View):
    def get(self, request):
        return render(request, 'VOIPLine/activation_details.html')

class ThemeView(View):
    def get(self, request):
        return render(request, 'VOIPLine/theme.html')
