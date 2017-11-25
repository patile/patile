from django.conf.urls import url
from django.contrib import admin

from home import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
]