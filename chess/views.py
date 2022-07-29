from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
import os


def games(request):
    print(request.user)
    all_games = Games.objects.filter(user = request.user )
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
    success_url = reverse_lazy("success")
    template_name = "registration/signup.html"


def success(request):
    context = {}
    return render(request, 'success.html', context)


def play(request):
    context = {}
    return render(request, 'play.html', context)


def upload_page(request):
    context = {}
    return render(request, 'upload.html', context)


def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")

    return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

