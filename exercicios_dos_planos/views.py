from rest_framework import generics

from grupos_musculares.models import GrupoMuscular
from .models import ExercicioDoPlano
from .serializers import ExercicioDoPlanoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsAdmin


class ExercicioDoPlanoView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = ExercicioDoPlano.objects.all()
    serializer_class = ExercicioDoPlanoSerializer
