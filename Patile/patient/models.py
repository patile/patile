from django.db import models


class Patient(models.Model):
    STATUS_TYPE = ('AVAILABLE', 'Available'), ('TREATMENT', 'In Treatment'), ("DONE", "Treatment Done")
    name = models.CharField(max_length=100, default="Jane Doe")
    status = models.CharField(max_length=30, choices=STATUS_TYPE, default="AVAILABLE")
    user = models.ForeignKey("users.UserProfile", related_name="patient")
    description = models.TextField(max_length=140, blank=True, null=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=9)
    latitude = models.DecimalField(decimal_places=6, max_digits=9)
    before = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True, blank=True)  # auto now add nasil calisiyor
    type = models.CharField(max_length=40, null=True, blank=True)
    sickness = models.CharField(max_length=100, default="Unknown")
    after = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def accept_patient(self):

        try:
            self.status == "TREATMENT"
        except:
            raise BaseException("Does not exist")
        self.save()

    def close_patient(self):

        try:
            self.status == "DONE"
        except:
            raise BaseException("Does not exist")
        self.save()
