from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import *


def index(request):
    context = {}
    return render(request, 'index.html', context)


def games(request):
    all_games = Games.objects.order_by('user_id')
    context = {
        'games': all_games,
    }
    return render(request, 'games.html', context)


def game(request, game_id):
    print(game_id)
    choose_game = get_object_or_404(Games, pk=game_id)
    return render(request, 'game.html', {'game': choose_game})

