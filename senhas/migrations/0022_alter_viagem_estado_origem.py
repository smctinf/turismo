# Generated by Django 4.0.6 on 2022-07-26 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0006_auto_20220310_1556'),
        ('senhas', '0021_alter_viagem_cnpj_empresa_transporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='estado_origem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contas.estado'),
        ),
    ]