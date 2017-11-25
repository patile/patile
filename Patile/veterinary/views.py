import json

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from patient.models import Patient
from veterinary.models import Veterinary_Patient


def login(request):
    return render(request, 'vet-home.html')
def ill(request):
    return render(request, 'ill_animal-detail.html')
def under_treatment(request):
    return render(request, 'under_treatment-detail.html')
def success(request):
    return render(request, 'success-detail.html')

def accept_patient(request):
    if request.method == "POST":
        id = request.POST.get("patient_id")
        get_object_or_404(Patient, id=id).accept_patient()
        response_json = {}
        response_json["help_text"] = "Hasta Hayvanı Aldığın İçin Teşekkürler"
        data = json.dumps(response_json)
        return HttpResponse(data)


def close_patient(request):
    if request.method == "POST":
        id = request.POST.get("patient_id")
        get_object_or_404(Patient, id=id).close_patient()
        response_json = {}
        response_json["help_text"] = "Hasta Hayvan Kapandı"
        data = json.dumps(response_json)
        return HttpResponse(data)


@user_passes_test(lambda u: not u.is_staff)
def vet_patient(request):
    results = []
    if request.method == "POST":
        vet = request.user
        vet_pet = Veterinary_Patient.objects.filter(veterinary=vet)
        response_json = {}
        for pet in vet_pet:
            response_json["name"] = pet.patient.name
            results.append(response_json)
        data = json.dumps(results)
        return HttpResponse(data)
