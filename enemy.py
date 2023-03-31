from random import randint

class EnemyParty:
    def __init__(self, maximum_strength, current_room):
        self.maximum_strength = maximum_strength
        self.current_room = current_room
        self.current_strength = 0
        self.enemy_group = []
        self.create_party()

    def create_party(self):
        """Creates an enemy party based on point allocation"""
        group = []
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
            health = enemy_health[size] + randint(-2,2) + self.current_room
            attack = enemy_attack[size] + randint(-2,2) + self.current_room
            new_unit = EnemyUnit(unit, health, attack)
            self.enemy_group.append(new_unit)
        return self.enemy_group

class EnemyUnit:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def enemy_action(self):
        action = randint(0,3)
        if action == 0:
            print("They do nothing")
            return 0
        elif action == 3:
            print("They do a big move")
            return self.attack + randint(1,5)
        else:
            print("They do a normal move")
            return self.attack + randint(-2,2)

    def enemy_damaged(self, damage):
        self.health = self.health - damage


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

test = EnemyParty(10, 23)

for i in range(len(test.enemy_group)):
    x = test.enemy_group[i]
    print(x.name, x.health, x.attack)
