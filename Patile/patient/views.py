# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from patient.models import Patient


def search_patient(request):
    if request.method == 'POST':
        patient_name = request.POST.get("patient_name")
        patients = Patient.objects.filter(name__icontains=patient_name)
        if patients:
            return JsonResponse(patients)
        else:
            return HttpResponse(False)


def pet_details(request, id):
    patient = Patient.objects.get(pk=id)
    return render(request, "singlePet.html", {"patient": patient})


def pets(request):
    patients = Patient.objects.all()
    return render(request, "pets.html", {"patients": patients})
