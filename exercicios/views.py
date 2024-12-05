from rest_framework import generics

from grupos_musculares.models import GrupoMuscular
from .models import Exercicio
from .serializers import ExercicioSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsAdmin


class ExercicioView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
