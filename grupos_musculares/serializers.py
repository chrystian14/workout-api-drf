from rest_framework import serializers
from .models import GrupoMuscular


class GrupoMuscularSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoMuscular
        fields = "__all__"
