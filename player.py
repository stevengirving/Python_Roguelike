from random import randint

class Player:
    def __init__(self, name, health):
        self.name = name
        self.stats["health"] += health

    def attack(self, enemy):
        print(f"You take a swing at {enemy}")
        damage = self.stats["attack"] + randint(-1,2)
        return damage

    def damaged(self, damage):
        self.stats["health"] -= damage

    stats = {
        "health": 20,
        "attack": 3,
        "defense": 1,
        "room": 1,
            }

    inventory = [
                 "wooden sword",
                 "wooden shield",
                 "potion",
                 ]


class Load(Player):
    def __init__(self, name, stats, inventory):
        self.name = name
        self.stats["health"] = int(stats[0])
        self.stats["attack"] = int(stats[1])
        self.stats["defense"] = int(stats[2])
        self.stats["room"] = int(stats[3])
        self.inventory = inventory[:]

