# Generated by Django 3.1.4 on 2022-10-18 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import senhas.validations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0009_auto_20221018_1831'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('senhas', '0021_merge_20220525_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=120)),
                ('url', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='viagem_turismo',
            name='ativo',
        ),
        migrations.AlterField(
            model_name='pontos_turisticos',
            name='nome',
            field=models.CharField(max_length=60, unique=True, validators=[senhas.validations.validate_nome]),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='cadastur_empresa_transporte',
            field=models.CharField(max_length=18, validators=[senhas.validations.validate_Cadastur]),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='cnpj_empresa_transporte',
            field=models.CharField(max_length=18, validators=[senhas.validations.validate_CNPJ]),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='contato_responsavel',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='dt_Chegada',
            field=models.DateField(validators=[senhas.validations.validate_data], verbose_name='Data Chegada'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='dt_Saida',
            field=models.DateField(blank=True, null=True, validators=[senhas.validations.validate_data], verbose_name='Data Saída'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='estado_origem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contas.estado'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='quant_passageiros',
            field=models.PositiveSmallIntegerField(validators=[senhas.validations.validate_passageiros]),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='responsavel_viagem',
            field=models.CharField(default=None, max_length=120, validators=[senhas.validations.validate_nome]),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='senha',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='cadastur_guia',
            field=models.CharField(max_length=18, validators=[senhas.validations.validate_Cadastur]),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='celular',
            field=models.CharField(max_length=15, validators=[senhas.validations.validate_celular]),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='nome_guia',
            field=models.CharField(max_length=60, validators=[senhas.validations.validate_nome]),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='telefone',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[senhas.validations.validate_telefone]),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='viagem',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='senhas.viagem'),
        ),
    ]
