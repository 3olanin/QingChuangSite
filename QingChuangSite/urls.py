"""QingChuangSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from showData import views as showData_views  

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', showData_views.index),
    path('', showData_views.showdataIndex),
    path('add/',showData_views.add),
    path('add/<int:a>/<int:b>/',showData_views.add2, name='add2'),
    path('home/',showData_views.home),
    path('downloadData/',showData_views.downloadData),
]
