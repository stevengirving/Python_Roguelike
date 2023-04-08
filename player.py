from random import randint

class Player:
    def __init__(self, name, health):
        self.name = name
        if name == "Test":
            self.stats["health"] = 1000
            self.stats["attack"] = 100
        else:
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
        "room": 1,
            }


class Load(Player):
    def __init__(self, name, stats):
        self.name = name
        self.stats["health"] = int(stats[0]) + 25
        self.stats["attack"] = int(stats[1])
        self.stats["room"] = int(stats[-1])

