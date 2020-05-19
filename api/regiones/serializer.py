from rest_framework import serializers
from .models import Regiones


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiones
        fields = '__all__'