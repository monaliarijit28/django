"""web_project URL Configuration

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
from django.conf.urls import include, url
from Doctor_Checkup import views
from django.urls import path
import sys

urlpatterns = [

    #url(r'^$', views.index_redirect, name='index_redirect'),
    #url(r'^index_redirect/(.+)/(.+)/$', views.index_redirect, name='index_redirect'),
    #url(r'^web/', include('web.urls')),
    #path('',include("web_project.urls")),
    path('Doctor_Checkup/',include('django.contrib.auth.urls')),

    path(r'', views.index, name="home"),
    path(r'home/', views.index, name="home"),
    
    path('sign_up/',views.sign_up,name="sign-up"),
    path(r'admin/', admin.site.urls),
]
  