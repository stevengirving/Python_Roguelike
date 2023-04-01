from random import randint
import enemy
import dungeon
import player
import system
import inputs

"""
current_room = 1
test = enemy.EnemyParty(10, current_room)
player_unit = player.Player("steven", 10)

for i in range(len(test.enemy_group)):
    x = test.enemy_group[i]
    y = player_unit
    combat_round = 1
    print(f"Current room: {current_room}")
    while x.health > 0:
        print(f"\nRound {combat_round}!\n")
        print(f"You: {y.stats['health']} HP")
        print(f"{x.name}: {x.health} HP {x.attack} ATK\n")
        y.damaged(x.enemy_action())
        if y.stats["health"] <= 0:
            print(f"You died {y.name.title()}!")
            exit(0)
        print(f"\nYou take a swing back at the {x.name}")
        x.enemy_damaged(y.stats["attack"] + randint(-1,+2))
        if x.health <= 0:
            print(f"{x.name} dies\n")
            break
        combat_round += 1
    current_room += 1
    print("~~~")
"""

system.Menu()
