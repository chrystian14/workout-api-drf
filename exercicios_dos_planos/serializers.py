from rest_framework import serializers
from .models import ExercicioDoPlano


class ExercicioDoPlanoSerializer(serializers.ModelSerializer):
    plano_de_treino_id = serializers.IntegerField()
    exercicio_id = serializers.IntegerField()

    class Meta:
        model = ExercicioDoPlano
        fields = (
            "id",
            "repeticoes",
            "series",
            "carga",
            "numero_equipamento",
            "plano_de_treino_id",
            "exercicio_id",
        )
