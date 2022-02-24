"""mart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index),
    path('index/',views.index),
    path('detail/<int:id>/',views.detail),
    path('shoppingcar/',views.shoppingcar),
    path('addtocar/<str:mode>/',views.addtocar),
    path('addtocar/<int:id>/<str:mode>/',views.addtocar),
    path('memberlogin/',views.memberlogin),
    path('memberlogout/',views.memberlogout),
    path('memberpro/',views.memberpro),
    path('memberinfo/',views.memberinfo),
    path('memberedit/',views.memberedit),
    path('order/',views.order),
    path('checkok/',views.checkok),
    path('ordercheck/',views.ordercheck),
    path('background/',views.background),
    path('background/<str:mode>/<int:id>/',views.background),
    path('membercheck/',views.membercheck),
    path('membercheck/<str:mode>/<int:id>/',views.membercheck),
    path('sellerlogin/',views.sellerlogin),
    path('sellerpro/',views.sellerpro),
    path('productindex/',views.productindex),
    path('productedit/<int:id>/',views.productedit),
    path('productedit/<int:id>/<str:mode>/',views.productedit),
    path('productupload/',views.productupload),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)