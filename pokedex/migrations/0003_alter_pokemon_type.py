# Generated by Django 4.2 on 2025-01-16 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('F', 'Fuego'), ('E', 'Electrico'), ('A', 'Agua'), ('P', 'Planta'), ('L', 'Lagarija')], max_length=30),
        ),
    ]
