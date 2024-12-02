from rest_framework import generics
from .models import GrupoMuscular
from .serializers import GrupoMuscularSerializer


class GrupoMuscularView(generics.ListCreateAPIView):
    queryset = GrupoMuscular.objects.all()
    serializer_class = GrupoMuscularSerializer
