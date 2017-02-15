from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomeView(View):

    def get(self, request):
        context = {
            'number': 10,
        }
        return render(request, 'home.html', context)

class AboutView(View):

    def get(self, request):
        context = {
            'number': 10,
        }
        return render(request, 'about.html', context)
