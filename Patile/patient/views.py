# Create your views here.
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from patient.models import Patient


def search_patient(request):
    if request.method == 'POST':
        patient_name = request.POST.get("patient_name")
        patients = Patient.objects.filter(name__icontains=patient_name)
        if patients:
            data = serializers.serialize("json", patients)
            return HttpResponse(data, content_type='application/json')
        else:
            return HttpResponse(False)


def pet_details(request, id):
    patient = Patient.objects.get(pk=id)
    return render(request, "singlePet.html", {"patient": patient})


def pets(request):
    patients = Patient.objects.all()
    return render(request, "pets.html", {"patients": patients})
