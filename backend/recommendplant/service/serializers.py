from rest_framework import serializers
from .models import PlantModel

# serializer.py
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlantModel
        fields='__all__'