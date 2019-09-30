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

    def __str__(self):
        return self.ten_khoa

    class Meta:
        verbose_name_plural = "Khoa"


class Nganh(models.Model):
    ten_nganh = models.CharField(max_length=255)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten_nganh
    class Meta:
        verbose_name_plural = "Ngành"

class Lop(models.Model):
    tenlop = models.CharField(max_length=255)
    nganh = models.ForeignKey(Nganh, on_delete=255)
    khoa_dao_tao = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Lớp"

    def __str__(self):
        return self.tenlop


class SinhVien(AbstractUser):
    masv = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gioi_tinh = models.BooleanField(default=False)
    ngaysinh = models.DateField(auto_now=True)
    dia_chi = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sinh viên"

class HocPhan(models.Model):
    ten_hp = models.CharField(max_length=255)
    so_tc = models.IntegerField(default=0)
    so_tiet_lt = models.IntegerField(default=0)
    so_tiet_th = models.IntegerField(default=0)

    def __str__(self):
        return self.ten_hp

    class Meta:
        verbose_name_plural = "Học phần"


class ChuongTrinhDaoTao(models.Model):
    mahp = models.ForeignKey(HocPhan, on_delete=models.CASCADE)
    manganh = models.ForeignKey(Nganh, on_delete=models.CASCADE)
    makhoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)
    tuchon = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.mahp.ten_hp + '-' + self.manganh.ten_nganh

    class Meta:
        verbose_name_plural = "Chương trình đào tạo"


class Diem(models.Model):
    hocky = models.IntegerField(default=0)
    ctdt = models.ForeignKey(ChuongTrinhDaoTao, on_delete=models.CASCADE, default=None, blank=True)
    hocphan = models.ForeignKey(HocPhan, on_delete=models.CASCADE, default=None, blank=True)
    sinhvien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    diem = models.FloatField(default=0)

    @property
    def get_diem_chu(self):
        return convert_diem_so_thanh_diem_chu(self.diem)

    def __str__(self):
        return str(self.hocky) + '-' + str(self.diem)

    class Meta:
        verbose_name_plural = "Điểm"


class KeHoachHocTapPerson(models.Model):
    sinhvien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    hocphan = models.ForeignKey(HocPhan, on_delete=models.CASCADE)
    hocky = models.IntegerField(default=0)

    def __str__(self):
        return self.sinhvien

    class Meta:
        verbose_name_plural = "Kế hoạch học tập"
