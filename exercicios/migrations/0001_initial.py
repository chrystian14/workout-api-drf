# Generated by Django 5.1.3 on 2024-12-02 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("grupos_musculares", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercicio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("descricao", models.TextField(blank=True, null=True)),
                (
                    "grupo_muscular",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exercicios",
                        to="grupos_musculares.grupomuscular",
                    ),
                ),
            ],
        ),
    ]