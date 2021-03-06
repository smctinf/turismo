# Generated by Django 3.2.10 on 2022-03-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guias', '0004_alter_guias_turismo_cadastur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guias_turismo',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='guias_turismo',
            name='facebook',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='guias_turismo',
            name='instagram',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='guias_turismo',
            name='nome',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='guias_turismo',
            name='segmento_de_atuacao',
            field=models.ManyToManyField(to='guias.Segmento_Atuacao', verbose_name='Segmento de Atuação'),
        ),
        migrations.AlterField(
            model_name='guias_turismo',
            name='site',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
