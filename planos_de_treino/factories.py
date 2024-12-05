import factory
from datetime import datetime as dt
from usuarios.factories import RegularUserFactory
from .models import PlanoDeTreino


class PlanoDeTreinoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanoDeTreino
        exclude = ("usuario",)

    nome = factory.Faker("word")
    data_criacao = factory.LazyFunction(lambda: dt.now().isoformat())

    usuario = factory.SubFactory(RegularUserFactory)
    usuario_id = factory.LazyAttribute(
        lambda plano_de_treino: plano_de_treino.usuario.pk
    )
