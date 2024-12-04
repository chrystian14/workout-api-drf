from rest_framework import generics
from .models import PlanoDeTreino
from .serializers import PlanoDeTreinoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from usuarios.permissions import IsAdmin


class PlanoDeTreinoView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = PlanoDeTreino.objects.all()
    serializer_class = PlanoDeTreinoSerializer
