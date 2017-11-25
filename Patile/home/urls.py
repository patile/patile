from django.conf.urls import url
from django.contrib import admin

from home import views
app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pets/$', views.pets, name='pets'),
    url(r'^singlePet/$', views.singlePet, name='singlePet'),
    url(r'^vets/$', views.vets, name='vets'),
    url(r'^singleVet/$', views.singleVet, name='singleVet'),
    url(r'^about/$', views.about, name='about'),
    url(r'^payment/$', views.payment, name='payment'),

]