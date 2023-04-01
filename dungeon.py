from random import randint
from math import remainder
import system

# Heal 5 HP after every room

class CreateRoom:
    def __init__(self, player_character, current_room=1):
        self.current_room = current_room
        if remainder(self.current_room,10) == 0:
            BossRoom().start(player_character)
        else:
            x = randint(1,20)
            if x == 20:
                HealRoom().start(player_character)
            elif x <= 4:
                EmptyRoom().start(player_character)
            else:
                FightRoom().start(player_character)


class FightRoom:

    def start(self, player_character):
        print("Fight room!")
        

class HealRoom:
    
    def start(self, player_character):
        print("Healing room!")

class EmptyRoom:
    
    def start(self, player_character):
        print("Empty room!")

class BossRoom:
    
    def start(self, player_character):
        print("Boss room!")
