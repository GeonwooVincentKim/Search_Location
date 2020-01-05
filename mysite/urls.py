"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello
from map import views

# app_name = 'main_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('map/', views.index, name='index'),
    # path('map/', include('map.urls', namespace='map')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/', include('map.urls', namespace='map')),
    # path('hi/', hello),
    url(r'^hi/$', hello),
    # url(r'^break/$', hi),
    # url(r'^Hi$/', hello),
]

