from random import randint
import enemy
from math import remainder
import system
import dungeon

# Heal 5 HP after every room

class CreateRoom:
    def __init__(self, player_character):
        self.current_room = player_character.stats["room"] 
        if remainder(self.current_room,10) == 0:
            BossRoom().start(player_character)
        else:
            x = 5 #randint(1,20)
            if x == 20:
                HealRoom().start(player_character)
            elif x <= 4:
                EmptyRoom().start(player_character)
            else:
                FightRoom().start(player_character)


class FightRoom:

    def start(self, player_character):
        print("Fight room!")
        current_room = player_character.stats["room"]
        fight = enemy.EnemyParty(20, current_room)
        for x in range(0,len(fight.enemy_group)):
            while fight.enemy_group[x].health > 0:
                if player_character.stats["health"] < 0:
                    system.GameOver("you got stabbed")
                fight.enemy_group[x].health -= player_character.attack()
                player_character.stats["health"] -= fight.enemy_group[0].enemy_action()
                print("Enemy HP:", fight.enemy_group[x].health)
                print("Player HP:", player_character.stats["health"])
            else:
                print("enemy dead, hopefully")
        #CreateRoom(player_character)
    
class HealRoom:
    
    def start(self, player_character):
        print("Healing room!")
        player_character["health"] += 100

class EmptyRoom:
    
    def start(self, player_character):
        print("Empty room!")
        dungeon.CreateRoom(player_character) 

class BossRoom:
    
    def start(self, player_character):
        print("Boss room!")
