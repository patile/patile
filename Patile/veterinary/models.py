from django.db import models


class Veterinary(models.Model):
    veterinary_name = models.CharField(max_length=200)
    latitute = models.DecimalField(max_digits=9, decimal_places=6)
    longtitute = models.DecimalField(max_digits=9, decimal_places=6)
    notice_count = models.IntegerField()
    address = models.TextField()
    created_date = models.DateField()


class Veterinary_Patient(models.Model):
    veterinary = models.ForeignKey("Veterinary", related_name="patient")
    patient = models.ForeignKey("Patient", related_name="veterinary")
