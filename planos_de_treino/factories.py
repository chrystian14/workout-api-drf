import factory
from datetime import datetime as dt
from usuarios.factories import RegularUserFactory
from .models import PlanoDeTreino


class PlanoDeTreinoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlanoDeTreino

    nome = factory.Faker("word")
    usuario = factory.SubFactory(RegularUserFactory)
    data_criacao = factory.LazyFunction(lambda: dt.now().isoformat())

    @classmethod
    def _adjust_kwargs(cls, **kwargs):
        kwargs["usuario"] = kwargs["usuario"].pk
        return kwargs
