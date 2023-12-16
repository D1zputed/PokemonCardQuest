from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from pokemon_quest_app.models import PokemonCard
from pokemon_quest_app.models import Trainer

# Create your views here.
class HomePageView(ListView):
    model = PokemonCard
    context_object_name = "home"
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainers'
    template_name = 'trainers.html'
    paginate_by = 15