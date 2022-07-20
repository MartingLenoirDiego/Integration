from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


def index(request):
    context = {}
    return render(request, 'index.html', context)


def games(request):
    all_games = Games.objects.filter(user = 2 )
    context = {
        'games': all_games,
    }
    return render(request, 'games.html', context)


def game(request, game_id):
    print(game_id)
    choose_game = get_object_or_404(Games, pk=game_id)
    return render(request, 'game.html', {'game': choose_game})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("")
    template_name = "registration/signup.html"


def login_view(request):
    user = authenticate(request, username="Dis", password="12DIE34go*/")
    if user is not None:
        login(request, user)
        return render(request, 'game.html')
    else:
        print('2')
