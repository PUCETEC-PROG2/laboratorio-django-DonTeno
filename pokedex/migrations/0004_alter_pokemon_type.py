# Generated by Django 4.2 on 2025-01-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_trainer_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('L', 'Lagarija'), ('A', 'Agua'), ('E', 'Electrico'), ('P', 'Planta'), ('F', 'Fuego'), ('T', 'Tierra')], max_length=30),
        ),
    ]