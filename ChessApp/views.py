from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .Game import Game
from .Games import gameDict, gameHistoryDict
from .models import Game as Gamedb, Move
import json


@login_required
def index_page(request):
    if request.method == 'POST':
        game_id = request.POST['game_id']
        game = gameDict.games[str(game_id)]
        # print(hash(game))
        if request.POST['type'] == "make_move":
            # print("running")
            # game.make_move(request)
            response = game.run(request, True)
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


# недоделана
def game_view(request):
    username = request.user.username
    if request.method == 'GET':
        game_id = request.GET.get("game_id", 1000)
        game_db = Gamedb.objects.get(id=game_id)
        moves_from_db = Move.objects.filter(game_id=game_id)
        # for move in moves_from_db:
            # print(move.move)
        last_move = moves_from_db[0]
        # print(last_move)
        for move in moves_from_db:
            if move.move_counter >= last_move.move_counter:
                last_move = move
        game = Game(new_game=False)
        response = game.get_position_from_db(request=last_move, last_move=True)
        print(response)
        # response = json.dumps(response)
        # return HttpResponse(json.dumps(response))
        # response = game.get_position_from_db()
        # all_moves = []
        # moves_from_db = Move.objects.filter(game_id=game_id)
        # for move in moves_from_db:
            # all_moves.append(move.move)
        # game_db = Gamedb.objects.get(game_id=game_id)
        # game = Game(player_white=game_db.player_white_username, player_black=game_db.player_black_username,
                    # new_game=False)
        # gameHistoryDict.add_game(hash(game), game)
        return render(request, 'ChessApp/game.html', {'response': response})


def profile(request):
    username = request.user.username
    game_ids = []
    games = Gamedb.objects.filter(player_white_username=username) | Gamedb.objects.filter(player_black_username=username)
    for game in games:
        game_ids.append(game.id)
    # print(game_ids)
    data = {
        'username': username,
        'game_ids': game_ids
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
    # print(request.META)
    if request.method == 'POST':
        # print(request.POST)
        return redirect('/')
    else:
        return render(request, 'ChessApp/main.html')
