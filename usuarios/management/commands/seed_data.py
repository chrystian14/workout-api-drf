from django.core.management.base import BaseCommand
from exercicios.factories import ExercicioFactory
from exercicios_dos_planos.factories import ExercicioDoPlanoFactory
from planos_de_treino.factories import PlanoDeTreinoFactory
from usuarios.factories import RegularUserFactory
import random


class Command(BaseCommand):
    help = "Popula o banco de dados com dados iniciais usando factories"

    def handle(self, *args, **kwargs):
        qtd_usuarios = 20
        treino_por_usuario_range = (1, 5)
        exercicios_por_plano_range = (1, 40)

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
                        f"[e-{index:04d}] Exercícios criados para {plano.nome}: {qtd_exercicios}"
                    )
                )

            print("\n")

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
