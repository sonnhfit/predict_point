from django.contrib import admin
from .models import (SinhVien, ChuongTrinhDaoTao
,HocPhan, Nganh, Khoa, Diem, Lop)
# Register your models here.
admin.site.register(SinhVien)
admin.site.register(ChuongTrinhDaoTao)
admin.site.register(HocPhan)
admin.site.register(Nganh)
admin.site.register(Khoa)
admin.site.register(Diem)
admin.site.register(Lop)

