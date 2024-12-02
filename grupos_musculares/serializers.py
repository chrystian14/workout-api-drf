from rest_framework import serializers

from grupos_musculares.models import GrupoMuscular


class GrupoMuscularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoMuscular
        fields = "__all__"
