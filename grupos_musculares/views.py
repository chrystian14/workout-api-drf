from rest_framework import generics
from .models import GrupoMuscular
from .serializers import GrupoMuscularSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsAdmin


class GrupoMuscularView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = GrupoMuscular.objects.all()
    serializer_class = GrupoMuscularSerializer
