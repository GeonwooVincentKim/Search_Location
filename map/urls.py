from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='template'),
    url(r'^hi_hi/$', views.hi),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
