import random
import factory

from grupos_musculares.factory import GrupoMuscularFactory

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


class ExercicioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "exercicios.Exercicio"
        django_get_or_create = ("nome",)

    nome = random.choice([exercicio["nome"] for exercicio in exercicios])
    grupo_muscular = factory.SubFactory(GrupoMuscularFactory)
