from django.db import models


class PlanoDeTreino(models.Model):
    nome = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        "usuarios.User", related_name="plano_de_treino", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.pk} - {self.nome}"
