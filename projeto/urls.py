"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from cliente import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('novocliente/',views.novo_cliente, name='novo'),
    path('atualizacao/',views.atualizacao, name='atual'),
    path('update/<int:id>',views.update, name='update'),
    path('exclusao/<int:id>',views.excluir, name='excluir'),
    path('login/', LoginView.as_view(), name="login"),
    path('login/', LogoutView.as_view(), name="logout"),
    



]
