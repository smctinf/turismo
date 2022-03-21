# Generated by Django 3.2.10 on 2022-03-21 16:57

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
            name='ProblemasRelatados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=350)),
                ('ativo', models.BooleanField(default=True)),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Inclusão')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Problema',
                'verbose_name_plural': 'Problemas Relatados',
                'ordering': ['id'],
            },
        ),
    ]