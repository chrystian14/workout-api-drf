from rest_framework import generics
from .models import Exercicio
from .serializers import ExercicioSerializer


class ExercicioView(generics.ListCreateAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
