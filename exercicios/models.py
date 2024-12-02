from django.db import models


# Todo: Pesquisar fichas de treino de academias
class Exercicio(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    grupo_muscular = models.ForeignKey(
        "grupos_musculares.GrupoMuscular",
        related_name="exercicios",
        on_delete=models.CASCADE,
    )
