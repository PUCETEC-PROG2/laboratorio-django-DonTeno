# Generated by Django 4.2 on 2025-01-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('F', 'Fuego'), ('E', 'Electrico'), ('P', 'Planta'), ('A', 'Agua'), ('L', 'Lagarija')], max_length=30),
        ),
    ]
