from django.conf.urls import url

from home import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^vets/$', views.vets, name='vets'),
    url(r'^singleVet/$', views.singleVet, name='singleVet'),
    url(r'^about/$', views.about, name='about'),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^bestVets/$', views.bestVets, name='bestVets'),
    url(r'^bestUsers/$', views.bestUsers, name='bestUsers'),
    url(r'^payComp/$', views.payComp, name='payComp'),

]