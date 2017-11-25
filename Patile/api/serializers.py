from rest_framework import serializers

from patient.models import Patient
from users.models import UserProfile
from veterinary.models import Veterinary

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('telegram_id', 'phone', 'full_name')


class PatientSerializer(serializers.ModelSerializer):
    """Serializer to map the Patient instance into JSON format."""

    user = UserSerializer(read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Patient
        fields = ('longitude', 'latitude', 'description', 'before', 'user')




class VeterinarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinary
        fields = ('veterinary_name','latitute','longtitute','address')



