from django.db import models


class ExercicioDoPlano(models.Model):
    repeticoes = models.PositiveIntegerField()
    series = models.PositiveSmallIntegerField()
    carga = models.PositiveSmallIntegerField(null=True, blank=True)
    numero_equipamento = models.PositiveIntegerField(null=True, blank=True)

    plano_de_treino = models.ForeignKey(
        "planos_de_treino.PlanoDeTreino",
        related_name="exercicios_do_plano",
        on_delete=models.CASCADE,
    )

    exercicio = models.ForeignKey(
        "exercicios.Exercicio",
        related_name="planos_inclusivos",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.pk} - {self.plano_de_treino.nome} - {self.exercicio.nome}"
