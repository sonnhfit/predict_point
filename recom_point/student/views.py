from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChuongTrinhDaoTao, Diem, KeHoachHocTapPerson, HocPhan
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
        context = {
            'data': ''
        }
        return render(request, 'xemdiemdudoan.html', context)


class XemChuongTrinhDaoTao(View):

    def get(self, request):
        ma_nganh = request.user.lop.nganh
        ctdt = ChuongTrinhDaoTao.objects.filter(manganh=ma_nganh)

        context = {
            'data': ctdt,
            'nganh': ma_nganh
        }
        return render(request, 'xemchuongtrinhdaotao.html', context)


class XemDiemView(View):

    def get(self, request):
        data = Diem.objects.filter(sinhvien=request.user)
        context = {
            'data': data
        }
        return render(request, 'xemdiem.html', context)


class ThemKeHoachHocTapCaNhan(View):

    def get(self, request):
        user = request.user
        get_private_plan = KeHoachHocTapPerson.objects.filter(sinhvien=user)
        nganhh = request.user.lop.nganh
        list_hocphan = ChuongTrinhDaoTao.objects.filter(manganh=nganhh)
        context = {
            'data': get_private_plan,
            'list_hocphan': list_hocphan
        }
        return render(request, 'kehoachhoctapcanhan.html', context)

    def post(self, request):
        hocky = request.POST['hocky']
        hocphan = request.POST['hocphan']
        hocph = HocPhan.objects.get(id=hocphan)
        KeHoachHocTapPerson.objects.create(
            sinhvien=request.user, hocky=hocky, hocphan=hocph)
        return redirect('kehoachhoctapcanhan')

