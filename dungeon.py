from random import randint
import enemy
from math import remainder
import system
import dungeon

# Heal 5 HP after every room

class CreateRoom:
    def __init__(self, player_character):
        self.current_room = player_character.stats["room"] 
        print(f"\nNow entering room {self.current_room}")
        while True:
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
            player_character.stats["room"] += 1
            CreateRoom(player_character)

class FightRoom:

    def start(self, player_character):
        print("\nFight room!\n")
        fight_round = 1
        current_room = player_character.stats["room"]
        fight = enemy.EnemyParty(current_room)
        for x in range(0,len(fight.enemy_group)):
            while fight.enemy_group[x].health > 0:
                print(f"\nRound {fight_round}\n")
                fight_round += 1
                fight.enemy_group[x].health -= player_character.attack(fight.enemy_group[x].name)
                if fight.enemy_group[x].health <= 0:
                    print(f"You murdered the poor {fight.enemy_group[x].name}")
                    break
                player_character.stats["health"] -= fight.enemy_group[0].enemy_action()
                if player_character.stats["health"] <= 0:
                    system.GameOver("you got stabbed")
                print("Enemy HP:", fight.enemy_group[x].health)
                print("Player HP:", player_character.stats["health"])
            else:
                pass
    
class HealRoom:
    
    def start(self, player_character):
        print("Healing room!")
        player_character.stats["health"] += 25
        print(f"Player HP: {player_character.stats['health']}")

class EmptyRoom:
    
    def start(self, player_character):
        print("\nEmpty room!\n")

class BossRoom:
    
    def start(self, player_character):
        print("Boss room!")
