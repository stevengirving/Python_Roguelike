from random import randint

class EnemyParty(object):
    
    def create(self, current_group, maximum_group):
        group = []
        while current_group < maximum_group:
            new_enemy = randint(1,3)
            if current_group + new_enemy > maximum_group:
                pass
            else:
                group.append(new_enemy)
                current_group += new_enemy
        else:
            return group

# Enemy Types

## Small
### 1 enemy strength
### 3-5 HP
### 2-3 ATK

## Medium
### 2 enemy strength
### 5-8 HP
### 4-5 ATK

## Large
### 3 enemy strength
### 8-13 HP
### 6-9 ATK

## Boss
### 15-20 HP
### 10-12 ATK

# Actions
## 50% Normal Attack
## 25% Heavy Attack
## 25% Nothing
