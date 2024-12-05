from rest_framework import serializers
from .models import PlanoDeTreino


class PlanoDeTreinoSerializer(serializers.ModelSerializer):
    usuario_id = serializers.IntegerField()

    class Meta:
        model = PlanoDeTreino
        fields = ("id", "nome", "usuario_id", "data_criacao")
