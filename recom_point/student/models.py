from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


def convert_diem_so_thanh_diem_chu(diem):
    if diem >= 8.5:
        return 'A'
    if diem >= 8.0:
        return 'B+'
    if diem >= 7.0:
        return 'B'
    if diem >= 6.5:
        return 'C+'
    if diem >= 5.5:
        return 'C'
    if diem >= 5.0:
        return 'D'
    if diem < 5:
        return 'F'


class Khoa(models.Model):
    ten_khoa = models.CharField(max_length=255)


class Nganh(models.Model):
    ten_nganh = models.CharField(max_length=255)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)


class Lop(models.Model):
    tenlop = models.CharField(max_length=255)
    nganh = models.ForeignKey(Nganh, on_delete=255)
    khoa_dao_tao = models.IntegerField(default=0)


class SinhVien(AbstractUser):
    masv = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gioi_tinh = models.BooleanField(default=False)
    ngaysinh = models.DateField(auto_now=True)
    dia_chi = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE, null=True, blank=True)


class HocPhan(models.Model):
    ten_hp = models.CharField(max_length=255)
    so_tc = models.IntegerField(default=0)
    so_tiet_lt = models.IntegerField(default=0)
    so_tiet_th = models.IntegerField(default=0)


class ChuongTrinhDaoTao(models.Model):
    mahp = models.ForeignKey(HocPhan, on_delete=models.CASCADE)
    manganh = models.ForeignKey(Nganh, on_delete=models.CASCADE)
    makhoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    tuchon = models.BooleanField(default=False, blank=True, null=True)


class Diem(models.Model):
    hocky = models.IntegerField(default=0)
    ctdt = models.ForeignKey(ChuongTrinhDaoTao, on_delete=models.CASCADE, default=None, blank=True)
    hocphan = models.ForeignKey(HocPhan, on_delete=models.CASCADE, default=None, blank=True)
    sinhvien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    diem = models.FloatField(default=0)

    @property
    def get_diem_chu(self):
        return convert_diem_so_thanh_diem_chu(self.diem)


class KeHoachHocTapPerson(models.Model):
    sinhvien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    hocphan = models.ForeignKey(HocPhan, on_delete=models.CASCADE)
    hocky = models.IntegerField(default=0)
