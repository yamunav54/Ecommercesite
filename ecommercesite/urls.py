"""ecommercesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from cartpage.views import homeview,loginview,registerview,logoutuser,cartview,storeview,checkoutview


urlpatterns = [
    path('',homeview,name='home'),
    path('login/',loginview,name='login'),
    path('logout',logoutuser,name='logout'),
    path('register/',registerview,name='register'),
    path('store/', storeview,name='store'),
    path('checkout/',checkoutview,name='checkout'),
    path('cart/',cartview,name='cart'),


    path('admin/', admin.site.urls),

]