from django.db import models

# Create your models here.


class Khoa(models.Model):
    ten_khoa = models.CharField(max_length=255)


class Nganh(models.Model):
    ten_nganh = models.CharField(max_length=255)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)


class Lop(models.Model):
    tenlop = models.CharField(max_length=255)
    nganh = models.ForeignKey(Nganh, on_delete=255)
    khoa_dao_tao = models.IntegerField(default=0)

class SinhVien(models.Model):
    masv = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gioi_tinh = models.BooleanField(default=False)
    ngaysinh = models.DateField(auto_now=True)
    dia_chi = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE)

class HocPhan(models.Model):
    ten_hp = models.CharField(max_length=255)
    so_tc = models.IntegerField(default=0)
    so_tiet_lt = models.IntegerField(default=0)
    so_tiet_th = models.IntegerField(default=0)


class ChuongTrinhDaoTao(models.Model):
    mahp = models.ForeignKey(HocPhan, on_delete=models.CASCADE)