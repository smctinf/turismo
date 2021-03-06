# Generated by Django 3.2.9 on 2021-12-12 20:09

import contas.functions
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo_Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=60, unique=True, verbose_name='Descrição')),
                ('ativo', models.BooleanField(default=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
            ],
            options={
                'verbose_name': 'Motivo da Viagem',
                'verbose_name_plural': 'Motivos das Viagens',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Pontos_Turisticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, unique=True)),
                ('obs', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observação')),
                ('requer_agendamento', models.BooleanField(default=False)),
                ('ativo', models.BooleanField(default=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
            ],
            options={
                'verbose_name': 'Ponto Turístico',
                'verbose_name_plural': 'Pontos Turísticos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, unique=True)),
                ('ativo', models.BooleanField(default=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
            ],
            options={
                'verbose_name': 'Tipo de Veículo',
                'verbose_name_plural': 'Tipos de Veículos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_Chegada', models.DateField(verbose_name='Data Chegada')),
                ('dt_Saida', models.DateField(verbose_name='Data Saída')),
                ('ficarao_hospedados', models.BooleanField(default=False, verbose_name='Ficarão Hospedados?')),
                ('hotel', models.CharField(blank=True, max_length=120, null=True)),
                ('restaurante', models.CharField(blank=True, max_length=120, null=True)),
                ('quant_passageiros', models.PositiveSmallIntegerField()),
                ('empresa_transporte', models.CharField(max_length=120)),
                ('cnpj_empresa_transporte', models.CharField(max_length=14, validators=[contas.functions.validate_CNPJ])),
                ('cadastur_empresa_transporte', models.CharField(max_length=14, validators=[contas.functions.validate_CNPJ])),
                ('obs', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Observação')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
                ('tipo_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='senhas.tipo_veiculo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Viagem',
                'verbose_name_plural': 'Tipos de Viagens',
                'ordering': ['user', 'dt_Chegada', 'dt_Saida'],
            },
        ),
        migrations.CreateModel(
            name='Viagem_Turismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_guia', models.CharField(max_length=60)),
                ('cadastur_guia', models.CharField(max_length=14, validators=[contas.functions.validate_CNPJ])),
                ('celular', models.CharField(max_length=11)),
                ('telefone', models.CharField(blank=True, max_length=10, null=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Dt. Inclusão')),
                ('pontos_turisticos', models.ManyToManyField(blank=True, to='senhas.Pontos_Turisticos')),
                ('viagem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='senhas.viagem')),
            ],
            options={
                'verbose_name': 'Viagem com Turismo',
                'verbose_name_plural': 'Viagens com Turismo',
                'ordering': ['viagem'],
            },
        ),
    ]
