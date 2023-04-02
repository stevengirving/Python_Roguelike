from random import randint

class EnemyParty:
    def __init__(self, maximum_strength):
        self.maximum_strength = maximum_strength
        self.enemy_group = []
        self.create_party()

    def create_party(self):
        """Creates an enemy party based on point allocation"""
        group = []
        self.current_strength = 0
        while self.current_strength < self.maximum_strength:
            new_enemy = randint(1,3)
            if self.current_strength + new_enemy > self.maximum_strength:
                pass
            else:
                group.append(new_enemy)
                self.current_strength += new_enemy
        else:
            self.enemy_group = self.create_unit(group)
            return self.enemy_group


    def create_unit(self, group):
        """Creates individual enemies based from the enemy strength """
        enemy_sizes = {1: "small", 2: "medium", 3: "large"}
        for x in group:
            size = enemy_sizes[x]
            unit = enemy_list[size][randint(0,len(enemy_list[size]) - 1)]
            health = enemy_health[size] + randint(0,2) + self.current_strength
            attack = enemy_attack[size] + randint(-2,2) + self.current_strength
            new_unit = EnemyUnit(unit, health, attack)
            self.enemy_group.append(new_unit)
        return self.enemy_group

class EnemyUnit:
    """Template for indidivual enemy units"""
    def __init__(self, name, health, attack):
        self.name = name.title()
        self.health = health
        self.attack = attack

    def enemy_action(self):
        action = randint(0,3)
        if action == 0:
            print(f"The {self.name} does nothing")
            return 0
        elif action == 3:
            print(f"The {self.name} does a BIG ATTACK")
            damage = self.attack + randint(1,5)
            print(f"You take {damage} damage")
            return damage
        else:
            print(f"The {self.name} does some stuff")
            damage = self.attack + randint(-2,2)
            print(f"You take {damage} damage")
            return damage

    def enemy_damaged(self, damage):
        print(f"The {self.name} takes {damage} damage")
        self.health -= damage


# All enemies based on size
enemy_list = {
    "small": ["goblin", "kobold", "skeleton", "zombie", "rat", "spider", "bat"],
    "medium": ["hobgoblin", "bugbear", "doppleganger", "ettercap", "harpy", "manticore", "minotaur", "ogre", "werewolf"], 
    "large": ["a small rabbit", "giant", "chimera", "bear", "cyclops", "gorgon", "hydra", "troll"],
    "boss": [],
}

# Base Health
enemy_health = {
    "small": 3,
    "medium": 6, 
    "large": 9,
    "boss": 12, 
}

#Base Attack
enemy_attack = {
    "small": 2,
    "medium": 4,
    "large": 6,
    "boss": 8,
}
