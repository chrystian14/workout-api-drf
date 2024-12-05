from rest_framework import serializers
from .models import PlanoDeTreino


class PlanoDeTreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoDeTreino
        fields = ("id", "nome", "usuario", "data_criacao")
