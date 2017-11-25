# Create your views here.
from django.shortcuts import render

def login(request):
    return render(request, 'vet-home.html')
def ill(request):
    return render(request, 'ill_animal-detail.html')
def under_treatment(request):
    return render(request, 'under_treatment-detail.html')
def success(request):
    return render(request, 'success-detail.html')

def accept_patient(request):
    return render(request, "")
