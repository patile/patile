from django.conf.urls import url

from veterinary import views

app_name = 'veterinary'

urlpatterns = [
    url(r'^accept', views.accept_patient, name='accept'),
    url(r'^$', views.login,name='login'),
    url(r'^illl/', views.ill, name='ill'),
    url(r'^under_treatment/', views.under_treatment, name='under_treatment'),
    url(r'^success/', views.success, name='success'),
    url(r'^vetpet/', views.vet_patient, name='all'),
    url(r'^vetcount/', views.vet_count, name='count'),

]
