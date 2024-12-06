from rest_framework import serializers

from exercicios.exceptions import ExercicioNotFound
from exercicios.models import Exercicio
from planos_de_treino.exceptions import PlanoDeTreinoNotFound
from planos_de_treino.models import PlanoDeTreino
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

    def validate_exercicio_id(self, value):
        exercicio_exists = Exercicio.objects.filter(pk=value).exists()

        if not exercicio_exists:
            raise ExercicioNotFound()

        return value

    def validate_plano_de_treino_id(self, value):
        plano_de_treino_exists = PlanoDeTreino.objects.filter(pk=value).exists()

        if not plano_de_treino_exists:
            raise PlanoDeTreinoNotFound()

        return value
