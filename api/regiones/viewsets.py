from rest_framework import viewsets
from .models import Regiones
from .serializer import RegionSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Regiones.objects.all()
    serializer_class = RegionSerializer
