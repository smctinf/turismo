# Generated by Django 3.2.10 on 2022-03-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0010_alter_viagem_cadastur_empresa_transporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem_turismo',
            name='outros',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]
