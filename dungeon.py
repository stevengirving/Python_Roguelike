from random import randint
import enemy
from math import remainder
import system
import dungeon


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
            player_character.stats["health"] += 5
            CreateRoom(player_character)

class FightRoom:

    def start(self, player_character):
        print("\nFight room!\n")
        self.fight_round = 1
        current_room = player_character.stats["room"]
        fight = enemy.EnemyParty(current_room)
        self.total_health = []
        print("In the room, ready for you, you find:")
        for x in range(0,len(fight.enemy_group)):
            print(fight.enemy_group[x].name)
            self.total_health.append(fight.enemy_group[x].health)
        self.fight_health = sum(self.total_health)
        while self.fight_health > 0:
            # Call to input.py to select enemy
            # FightRoom.player_turn(player_character, enemy_unit)
            print(f"\nRound {self.fight_round}\n")
            self.fight_round += 1
            target = randint(0,len(fight.enemy_group) - 1)
            damage = FightRoom().player_turn(player_character, fight.enemy_group[target])
            self.fight_health -= damage
            if fight.enemy_group[target].health <= 0:
                print(f"You murdered the poor {fight.enemy_group[y].name}")
            for y in range(0, len(fight.enemy_group)):
                FightRoom().enemy_turn(player_character, fight.enemy_group[y])
                if player_character.stats["health"] <= 0:
                    system.SaveGame(player_character)
                    system.GameOver("you should have dodged.")
                print(f"\n{fight.enemy_group[y].name} HP:", fight.enemy_group[y].health)
                print("Player HP:", player_character.stats["health"], "\n")
        else:
            pass
    
    def player_turn(self, player_character, enemy_unit):
        if enemy_unit.health <= 0:
            return 0
        else:
            damage = player_character.attack(enemy_unit.name)
            enemy_unit.enemy_damaged(damage)
            return damage

    def enemy_turn(self, player_character, enemy_unit):
        if enemy_unit.health <= 0:
            pass
        else:
            player_character.damaged(enemy_unit.enemy_action())


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
