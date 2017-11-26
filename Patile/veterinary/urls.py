from django.conf.urls import url

from veterinary import views

app_name = 'veterinary'

urlpatterns = [
    url(r'^accept/$', views.accept_patient, name='accept'),
    url(r'^$', views.login,name='login'),
    url(r'^illl/get_warning', views.get_warning, name='ill'),
    url(r'^illl/$', views.ill, name='ill'),
    url(r'^under_treatment/$', views.under_treatment, name='under_treatment'),
    url(r'^success/$', views.success, name='success'),
    url(r'^vetpet/$', views.vet_patient, name='all'),
    url(r'^vetcount/$', views.vet_count, name='count'),
    url(r'^login/$', views.LoginView, name='login'),
url(r'^login/$', views.LoginView, name='login'),

]
