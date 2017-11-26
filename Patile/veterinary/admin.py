# Register your models here.
from django.contrib import admin

from veterinary.models import Veterinary,City,Veterinary_Patient

admin.site.register(Veterinary)
admin.site.register(City)
admin.site.register(Veterinary_Patient)