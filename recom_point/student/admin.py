from django.contrib import admin
from .models import (SinhVien, ChuongTrinhDaoTao
,HocPhan, Nganh, Khoa, Diem, Lop, KeHoachHocTapPerson)

class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('masv', 'name', 'gioi_tinh', 'ngaysinh', 'lop')

# Register your models here.
admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(ChuongTrinhDaoTao)
admin.site.register(HocPhan)
admin.site.register(Nganh)
admin.site.register(Khoa)
admin.site.register(Diem)
admin.site.register(Lop)
admin.site.register(KeHoachHocTapPerson)
