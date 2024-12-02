# Generated by Django 5.1.3 on 2024-12-02 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0002_alter_user_email_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "A user with that email already exists."},
                max_length=127,
                unique=True,
            ),
        ),
    ]
