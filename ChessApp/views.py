from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .Game import Game
from .Games import gameDict
from .models import Game as Gamedb, Move
import json


@login_required
def index_page(request):
    if request.method == 'POST':
        game_id = request.POST['game_id']
        game = gameDict.games[str(game_id)]
        if request.POST['type'] == "make_move":
            # print("running")
            # game.make_move(request)
            response = game.run(request)
            return HttpResponse(json.dumps(response))
        if request.POST['type'] == "get_position":
            # print(game.queen_black.position)
            # game2 = Game()
            response = game.get_position_from_db(request)
            return HttpResponse(json.dumps(response))

    game_id = request.GET.get("game_id", 1000)
    game = gameDict.games[str(game_id)]
    data = {
        'game_id': game_id,
        'player_white': game.player_white,
        'player_black': game.player_black
    }
    return render(request, 'ChessApp/play.html', data)


def profile(request):
    username = request.user.username
    games = Gamedb.objects.filter(player_white_username=username) | Gamedb.objects.filter(player_black_username=username)
    data = {
        'username': username
    }
    return render(request, 'ChessApp/profile.html', data)


def register(request):
    if request.method == 'POST':
        # print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                print('hehe')
            login(request, user)
            players = Group.objects.get(name='Players')
            players.user_set.add(user)
            return redirect('/')

    else:
        form = UserCreationForm()
    return render(request, 'ChessApp/register.html', {'form': form})


def auth(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("auth")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                print("user")
            login(request, user)
            return redirect('/')

    else:
        form = AuthenticationForm()
    return render(request, 'ChessApp/auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def main(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('/')
    else:
        return render(request, 'ChessApp/main.html')
