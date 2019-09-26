from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChuongTrinhDaoTao
# Create your views here.


class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            return redirect('login')


class XemDiemDuDoanView(View):

    def get(self, request):
        return render(request, 'xemdiemdudoan.html')


class XemChuongTrinhDaoTao(View):

    def get(self, request):
        ma_nganh = request.user.lop.nganh
        ctdt = ChuongTrinhDaoTao.objects.filter(manganh=ma_nganh)

        context = {
            'data': ctdt,
            'nganh': ma_nganh
        }
        return render(request, 'xemchuongtrinhdaotao.html', context)
