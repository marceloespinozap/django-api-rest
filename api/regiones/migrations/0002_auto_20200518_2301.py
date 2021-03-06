# Generated by Django 2.2.5 on 2020-05-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regiones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calles',
            name='nombre_calle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='comunas',
            name='comuna',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='provincias',
            name='provincia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='regiones',
            name='abreviatura',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='regiones',
            name='capital',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='regiones',
            name='region',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
