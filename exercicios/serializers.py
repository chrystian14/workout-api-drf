from rest_framework import serializers

from grupos_musculares.exceptions import GrupoMuscularNotFound
from grupos_musculares.models import GrupoMuscular
from .models import Exercicio


class ExercicioSerializer(serializers.ModelSerializer):
    grupo_muscular_id = serializers.IntegerField()

    class Meta:
        model = Exercicio
        fields = ("id", "nome", "descricao", "grupo_muscular_id")

    def validate_grupo_muscular_id(self, value):
        grupo_muscular_exists = GrupoMuscular.objects.filter(pk=value).exists()

        if not grupo_muscular_exists:
            raise GrupoMuscularNotFound()

        return value
