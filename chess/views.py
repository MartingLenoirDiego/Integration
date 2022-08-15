from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
import os
from django.views.decorators.csrf import csrf_protect
import base64
import io
from PIL import Image


def games(request):
    print(request.user)
    all_games = Games.objects.filter(user = request.user )
    context = {
        'games': all_games,
    }
    return render(request, 'games.html', context)


def game(request, game_id):
    choose_game = get_object_or_404(Games, pk=game_id)
    return render(request, 'game.html', {'game': choose_game})


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("success")
    template_name = "registration/signup.html"


def success(request):
    context = {}
    return render(request, 'success.html', context)


def play(request):
    context = {}
    return render(request, 'play.html', context)


def test(request):
    data = request.POST['image']
    data = data.split("base64")
    print(data[1])
    data = bytes(data[1],'UTF-8')
    with open("chess/imageToChess.png", "wb") as fh:
       fh.write(base64.decodebytes(data))
    os.system('python chess/tensorflow_chessbot.py --filepath chess/imageToChess.png ')

    return HttpResponse('c')