import factory
from datetime import datetime as dt
from usuarios.factories import RegularUserFactory
from .models import PlanoDeTreino


class PlanoDeTreinoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanoDeTreino
        exclude = ("usuario",)

    nome = factory.Sequence(lambda num: f"Plano de Treino {num:05d}")
    data_criacao = factory.LazyFunction(lambda: dt.now().isoformat())

    usuario = factory.SubFactory(RegularUserFactory)
    usuario_id = factory.LazyAttribute(
        lambda plano_de_treino: plano_de_treino.usuario.pk
    )
