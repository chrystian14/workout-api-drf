import factory

from exercicios.factories import ExercicioFactory
from planos_de_treino.factories import PlanoDeTreinoFactory
from .models import ExercicioDoPlano


class ExercicioDoPlanoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExercicioDoPlano

    repeticoes = factory.Faker("random_int", min=1, max=25)
    series = factory.Faker("random_int", min=1, max=10)
    carga = factory.Faker("random_number")
    numero_equipamento = factory.Faker("random_int", min=1, max=200)

    exercicio = factory.SubFactory(ExercicioFactory)
    exercicio_id = factory.LazyAttribute(
        lambda exercicio_do_plano: exercicio_do_plano.exercicio.pk
    )

    plano_de_treino = factory.SubFactory(PlanoDeTreinoFactory)
    plano_de_treino_id = factory.LazyAttribute(
        lambda exercicio_do_plano: exercicio_do_plano.plano_de_treino.pk
    )
