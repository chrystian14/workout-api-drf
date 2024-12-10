from django.core.management.base import BaseCommand
from exercicios.factories import ExercicioFactory
from exercicios_dos_planos.factories import ExercicioDoPlanoFactory
from planos_de_treino.factories import PlanoDeTreinoFactory
from usuarios.factories import RegularUserFactory
import random

from django.apps import apps


def clear_database():
    # Define a ordem de exclusão para manter a integridade referencial
    models_to_clear = [
        {"app_label": "exercicios_dos_planos", "model_name": "ExercicioDoPlano"},
        {"app_label": "planos_de_treino", "model_name": "PlanoDeTreino"},
        {"app_label": "exercicios", "model_name": "Exercicio"},
        {"app_label": "grupos_musculares", "model_name": "GrupoMuscular"},
        {"app_label": "usuarios", "model_name": "User"},
    ]

    for model_info in models_to_clear:
        model = apps.get_model(
            app_label=model_info["app_label"], model_name=model_info["model_name"]
        )
        model.objects.all().delete()
        print(
            f"Todos os registros do modelo {model_info['model_name']} foram excluídos."
        )
    print()


class Command(BaseCommand):
    help = "Popula o banco de dados com dados iniciais usando factories"

    def handle(self, *args, **kwargs):
        qtd_usuarios = 20
        treino_por_usuario_range = (1, 5)
        exercicios_por_plano_range = (1, 40)

        self.stdout.write(self.style.SUCCESS("Limpando o banco de dados..."))
        clear_database()

        self.stdout.write(
            self.style.SUCCESS("Populando banco de dados com dados iniciais...")
        )

        usuarios = RegularUserFactory.create_batch(qtd_usuarios)
        self.stdout.write(self.style.SUCCESS(f"Usuários criados: {len(usuarios)}"))

        for index, user in enumerate(usuarios, 1):
            qtd_planos = random.randint(*treino_por_usuario_range)
            planos_de_treino = PlanoDeTreinoFactory.create_batch(
                qtd_planos, usuario=user
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"[pdt-{index:03d}] Planos de Treino criados para {user.username}: {qtd_planos}"
                )
            )

            for index, plano in enumerate(planos_de_treino, 1):
                qtd_exercicios = random.randint(*exercicios_por_plano_range)
                ExercicioDoPlanoFactory.create_batch(
                    qtd_exercicios, plano_de_treino=plano
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"[e-{index:05d}] Exercícios criados para {plano.nome}: {qtd_exercicios}"
                    )
                )

            print("\n")

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
