import random
import factory

from grupos_musculares.factories import GrupoMuscularFactory

exercicios = [
    {"nome": "Corrida", "descricao": "Corrida ao ar livre", "grupo_muscular": "Cardio"},
    {
        "nome": "Levantamento de Peso",
        "descricao": "Levantamento de pesos pesados",
        "grupo_muscular": "Força",
    },
    {
        "nome": "Alongamento",
        "descricao": "Exercícios de alongamento",
        "grupo_muscular": "Flexibilidade",
    },
    {"nome": "Supino", "descricao": "Exercício de supino", "grupo_muscular": "Peito"},
    {
        "nome": "Barra Fixa",
        "descricao": "Exercício de barra fixa",
        "grupo_muscular": "Costas",
    },
    {
        "nome": "Agachamento",
        "descricao": "Exercício de agachamento",
        "grupo_muscular": "Pernas",
    },
]


def get_random_exercicio():
    return random.choice([exercicio["nome"] for exercicio in exercicios])


def get_exercicio_description_by_nome(nome: str):
    for exercicio in exercicios:
        if exercicio["nome"] == nome:
            return exercicio["descricao"]

    return "Descricao Generica"


class ExercicioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "exercicios.Exercicio"
        exclude = ("grupo_muscular",)
        django_get_or_create = ("nome",)

    nome = factory.LazyFunction(get_random_exercicio)
    descricao = factory.LazyAttribute(
        lambda obj: get_exercicio_description_by_nome(obj.nome)
    )

    grupo_muscular = factory.SubFactory(GrupoMuscularFactory)
    grupo_muscular_id = factory.LazyAttribute(
        lambda exercicio: exercicio.grupo_muscular.pk
    )
