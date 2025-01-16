from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer
from django.shortcuts import redirect, render
from pokedex.forms import PokemonForm

def index(request):
    pokemons = Pokemon.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'pokemons': pokemons
        },
        request))
    
    
def trainers(request):
    trainers = Trainer.objects.order_by('first_name')
    template = loader.get_template('trainers.html')
    return HttpResponse(template.render({
        'trainers': trainers
    },
    request))

def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()

    return render(request, 'pokemon_form.html', {'form': form})


def trainer_details(request, trainer_id):
    trainer = Trainer.objects.get(pk = trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))