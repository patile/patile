from django.conf.urls import url

from patient import views

app_name = 'patient'

urlpatterns = [
    url(r'^search-patient/(?P<id>\d+)$', views.search_patient, name='search_patient'),
    url(r'^pet-details/(?P<id>\d+)$', views.pet_details, name="pet_details")
]
