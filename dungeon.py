from random import randint
import enemy
from math import remainder
import system
import dungeon
from os import system as clear


class CreateRoom:
    def __init__(self, player_character):
        self.current_room = player_character.stats["room"] 
        clear("clear")
        print(f"\nNow entering room {self.current_room}")
        while True:
            x = randint(1,20)
            if x == 20:
                HealRoom().start(player_character)
            elif x <= 4:
                EmptyRoom().start(player_character)
            else:
                FightRoom().start(player_character)
            player_character.stats["room"] += 1
            player_character.stats["health"] += 5
            input("\n> NEXT")
            clear("clear")
            CreateRoom(player_character)

class FightRoom:

    def start(self, player_character):
        print("\nFight room!\n")
        current_room = player_character.stats["room"]
        fight = enemy.EnemyParty(current_room)
        print("In the room, ready for you, you find:")
        for x in range(0,len(fight.enemy_group)):
            print(fight.enemy_group[x].name)
        input("\n> NEXT")
        FightRoom().round(player_character, fight.enemy_group)

    def round(self, player_character, enemy):
        self.fight_round = 1
        while enemy != []:
            # Call to input.py to select enemy
            # FightRoom.player_turn(player_character, enemy_unit)
            clear("clear")
            print(f"\nRound {self.fight_round}\n")
            self.fight_round += 1
            target = randint(0,len(enemy) - 1)
            damage = FightRoom().player_turn(player_character, enemy[target])
            if enemy[target].health <= 0:
                del enemy[target]
            for x in range(0, len(enemy)):
                FightRoom().enemy_turn(player_character, enemy[x])
                if player_character.stats["health"] <= 0:
                    system.SaveGame(player_character)
                    system.GameOver(f"you were killed by {enemy[x].name}.")
                print(f"\n{enemy[x].name} HP:", enemy[x].health)
                print("Player HP:", player_character.stats["health"], "\n")
                input("\n> NEXT")
    
    def player_turn(self, player_character, enemy_unit):
        if enemy_unit.health <= 0:
            return 0
        else:
            damage = player_character.attack(enemy_unit.name)
            enemy_unit.enemy_damaged(damage)
            return damage

    def enemy_turn(self, player_character, enemy_unit):
        if enemy_unit.health <= 0:
            enemy_unit.health = 0
            pass
        else:
            player_character.damaged(enemy_unit.enemy_action())


class HealRoom:
    
    def start(self, player_character):
        print("Healing room!")
        player_character.stats["health"] += 25
        print(f"\nPlayer HP: {player_character.stats['health']}")

class EmptyRoom:
    
    def start(self, player_character):
        print("\nEmpty room!\n")
