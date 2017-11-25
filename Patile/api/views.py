import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PatientSerializer,VeterinarySerializer
from patient.models import Patient
from veterinary.models import Veterinary
from users.models import UserProfile

class PatientView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request):
        patient_id = request.GET.get("patient_id", "")
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
            serializer = PatientSerializer(patient)
        else:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients,many=True)
        return Response(serializer.data)

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        print(data)
        user, created = UserProfile.objects.get_or_create(**data.get("user"))
        data["user"] = user
        Patient.objects.create(**data)
        return Response(status=status.HTTP_200_OK)


class VeterinaryView(APIView):
    def get(self,request):
        city_id = request.GET.get("city_id"," ")
        if city_id == " ":
            veterinaries = Veterinary.objects.all()
            serializer = VeterinarySerializer(veterinaries, many=True)
        else:
            veterinaries = Veterinary.objects.filter(city=city_id)
            serializer = VeterinarySerializer(veterinaries, many=True)

        return Response(serializer.data)

