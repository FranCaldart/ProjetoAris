# Generated by Django 4.1.2 on 2022-10-27 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ncs", "0002_alter_nc_descricao_alter_nc_municipio_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nc",
            name="Situacao",
            field=models.CharField(
                choices=[("Atendida", "Atendida"), ("Pendente", "Pendente")],
                max_length=20,
                null=True,
            ),
        ),
    ]
