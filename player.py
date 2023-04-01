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
        "inventory": ["wooden sword", "wooden shield", "potion"],
    }


