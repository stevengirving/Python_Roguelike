class Player:
    def __init__(self, name, health):
        self.name = name
        self.stats["health"] += health

    def attack(self):
        return self.stats["attack"]

    def damaged(self, damage):
        self.stats["health"] -= damage

    stats = {
        "health": 20,
        "attack": 5,
        "defense": 2,
        "room": 1,
            }

    inventory = [
                 "wooden sword",
                 "wooden shield",
                 "potion",
                 ]


class Load(Player):
    def __init__(self, name, current_room, stats, inventory):
        self.name = name
        self.stats["health"]: stats[0]
        self.stats["attack"]: stats[1]
        self.stats["defense"]: stats[2]
        self.stats["room"]: stats[3]
        self.inventory = inventory[:]
