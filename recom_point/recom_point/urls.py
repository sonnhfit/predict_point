"""recom_point URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from student.views import (
    IndexView, LoginView, XemDiemDuDoanView,
    XemChuongTrinhDaoTao, XemDiemView, ThemKeHoachHocTapCaNhan
)


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('chuongtrinhdaotao/', XemChuongTrinhDaoTao.as_view(), name='ctdaotao'),
    path('kehoachhoctapcanhan/', ThemKeHoachHocTapCaNhan.as_view(), name='kehoachhoctapcanhan'),
    path('xemdiemthi/', XemDiemView.as_view(), name='xemdiemthi'),
    path('xemdiem/', XemDiemDuDoanView.as_view(), name='xemdiem'),
    prefix_default_language=False
)

