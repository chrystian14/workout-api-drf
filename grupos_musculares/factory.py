import factory
import random

grupos_musculares = [
    {"nome": "Cardio", "descricao": "Exercícios de cardiovascular"},
    {"nome": "Força", "descricao": "Exercícios de força"},
    {"nome": "Flexibilidade", "descricao": "Exercícios de flexibilidade"},
    {"nome": "Peito", "descricao": "Exercícios para peito"},
    {"nome": "Costas", "descricao": "Exercícios para costas"},
    {"nome": "Pernas", "descricao": "Exercícios para pernas"},
]


class GrupoMuscularFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "grupos_musculares.GrupoMuscular"
        django_get_or_create = ("nome",)

    nome = random.choice(
        [grupo_muscular["nome"] for grupo_muscular in grupos_musculares]
    )
    descricao = factory.Faker("sentence")
