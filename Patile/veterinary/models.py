from django.db import models


class Veterinary(models.Model):
    photo = models.ImageField()
    veterinary_name = models.CharField(max_length=200)
    latitute = models.DecimalField(max_digits=9, decimal_places=6)
    longtitute = models.DecimalField(max_digits=9, decimal_places=6)
    notice_count = models.IntegerField()
    address = models.TextField()
    created_date = models.DateField()

    def __str__(self):
        return self.veterinary_name


class Veterinary_Patient(models.Model):
    veterinary = models.ForeignKey("Veterinary", related_name="patient")
    patient = models.ForeignKey("patient.Patient", related_name="veterinary")

    def __str__(self):
        return self.veterinary.veterinary_name + " - " + self.patient.name


class Status(models.Model):
    patient = models.ForeignKey("Veterinary_Patient", related_name="status")
    status = models.TextField(max_length=500)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.patient.patient.name + " - " + self.status
