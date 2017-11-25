from django.conf.urls import url

from veterinary import views

app_name = 'veterinary'

urlpatterns = [
    url(r'^accept', views.accept_patient, name='accept'),
]
