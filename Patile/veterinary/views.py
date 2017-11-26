import json

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from patient.models import Patient
from veterinary.forms import SignUpForm, LoginForm
from veterinary.models import Veterinary_Patient, Veterinary


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
        vet_pet = Veterinary_Patient.objects.filter(veterinary=Veterinary.objects.get())
        response_json = {}
        for pet in vet_pet:
            response_json["name"] = pet.patient.name
            results.append(response_json)
        data = json.dumps(results)
        return HttpResponse(data)


def vet_count(request):
    if request.method == "POST":
        vet = Veterinary.objects.get(id=1)
        active_pet = Veterinary_Patient.objects.filter(veterinary=vet, patient__status="AVAILABLE").count()
        close_pet = Veterinary_Patient.objects.filter(patient__status="DONE", veterinary=vet).count()
        response_json = {}
        response_json["active_count"] = str(active_pet)
        response_json["close_count"] = str(close_pet)
        data = json.dumps(response_json)
        return HttpResponse(data)


def vet_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home:index")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def LoginView(request):
    if request.user.is_authenticated:
        return redirect("home:index")

    if request.method == "POST":

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home:index")
        else:
            return redirect("user:login")

    form = LoginForm()
    return render(request, "registration/login.html", {"form": form})
