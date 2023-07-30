from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Game(models.Model):
    player_white_username = models.CharField(max_length=100)
    player_black_username = models.CharField(max_length=100)
    result = models.CharField(max_length=100, default="Unknown")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)


class Move(models.Model):
    move_counter = models.IntegerField()
    who_to_move = models.CharField(max_length=8, default="white")
    piece = models.CharField(max_length=20)
    old_position = models.CharField(max_length=8)
    new_position = models.CharField(max_length=8)
    move = models.CharField(max_length=8)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

