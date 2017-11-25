# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from patient.models import Patient


def search_patient(request, id):
    patient = Patient.objects.get(pk=id)
    if patient:
        return JsonResponse(patient)
    else:
        return HttpResponse(False)


def pet_details(request, id):
    patient = Patient.objects.get(pk=id)
    return render(request, "singlePet.html", {"patient": patient})
