# Generated by Django 3.2.10 on 2022-02-22 15:37

import contas.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0007_alter_viagem_cnpj_empresa_transporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='cnpj_empresa_transporte',
            field=models.CharField(max_length=14, validators=[contas.functions.validate_CNPJ]),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='cadastur_guia',
            field=models.CharField(max_length=14, validators=[contas.functions.validate_CADASTUR]),
        ),
    ]
