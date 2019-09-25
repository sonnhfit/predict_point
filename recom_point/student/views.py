from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class DemoView(View):
    def get(self, request):
        return HttpResponse('xin chao')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')