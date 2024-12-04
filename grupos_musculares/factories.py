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


def get_random_grupo_muscular():
    return random.choice(
        [grupo_muscular["nome"] for grupo_muscular in grupos_musculares]
    )


def get_grupo_muscular_description_by_nome(nome: str):
    for grupo_muscular in grupos_musculares:
        if grupo_muscular["nome"] == nome:
            return grupo_muscular["descricao"]

    return "Descricao Generica"


class GrupoMuscularFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "grupos_musculares.GrupoMuscular"
        django_get_or_create = ("nome",)

    nome = factory.LazyFunction(get_random_grupo_muscular)
    descricao = factory.LazyAttribute(
        lambda obj: get_grupo_muscular_description_by_nome(obj.nome)
    )
