from django.conf.urls import url

from .views import PatientView

urlpatterns = [
    url(r'^patients', PatientView.as_view(), name='patients'),
]
