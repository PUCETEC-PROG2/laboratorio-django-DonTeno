from django.urls import path

from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("trainers/", views.trainers, name="trainers"),
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainers/<int:trainer_id>/", views.trainer_details, name="trainer_details"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon")
]