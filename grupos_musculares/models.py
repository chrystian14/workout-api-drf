from django.db import models


class GrupoMuscular(models.Model):
    nome = models.CharField(max_length=127, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
