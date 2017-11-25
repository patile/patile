from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PatientSerializer
from patient.models import Patient


class PatientView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Patient.objects.all()
        from api.serializers import PatientSerializer
        serializer = PatientSerializer(snippets, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
