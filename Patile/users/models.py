# Create your models here.

from django.db import models

from patient.models import Patient


class UserProfile(models.Model):
    telegram_id = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)

    @property
    def get_notice_count(self):
        return Patient.objects.filter(pk=self.id).count()
