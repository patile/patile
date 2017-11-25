# Create your views here.
from django.shortcuts import render

def login(request):
    return render(request, 'vet-home.html')

def accept_patient(request):
    return render(request, "")
