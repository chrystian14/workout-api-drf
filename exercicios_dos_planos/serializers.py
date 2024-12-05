from rest_framework import serializers

from grupos_musculares.exceptions import GrupoMuscularNotFound
from grupos_musculares.models import GrupoMuscular
from .models import ExercicioDoPlano


class ExercicioDoPlanoSerializer(serializers.ModelSerializer):
    plano_de_treino_id = serializers.IntegerField()
    exercicio_id = serializers.IntegerField()

    class Meta:
        model = ExercicioDoPlano
        fields = (
            "repeticoes",
            "series",
            "carga",
            "numero_equipamento",
            "plano_de_treino_id",
            "exercicio_id",
        )
