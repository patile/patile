from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def pets(request):
    return render(request, 'pets.html')


def contact(request):
    return render(request, 'contact.html')

def vets(request):
    return render(request, 'vets.html')

def singlePet(request):
    return render(request, 'singlePet.html')

def singleVet(request):
    return render(request, 'singleVet.html')

def about(request):
    return render(request, 'about.html')
def payment(request):
    return render(request, 'payment.html')
def bestVets(request):
    return render(request, 'bestVets.html')
def bestUsers(request):
    return render(request, 'bestUsers.html')

