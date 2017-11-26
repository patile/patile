from django.conf.urls import url

from .views import PatientView, VeterinaryView

urlpatterns = [
    url(r'^patients', PatientView.as_view(), name='patients'),
    url(r'^veterinaries', VeterinaryView.as_view(), name='veterinaries'),

]

