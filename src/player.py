from enemy import Enemy
import time
from os import system
import random

def roll_crit(crit_chance: float) -> bool:
    roll = random.randint(0, 100)
    print(roll)
    if crit_chance >= roll:
        return True
    return False

class Player:
    def __init__(self, name : str):
        self.name = name
        self.position = [0, 0]
    
    def move(self, direction : list[int]):
        self.position[0] += direction[0]
        self.position[1] += direction[1]


class Warrior(Player):
    def __init__(self, name : str, strength : int, intellect : int, dexterity : int):
        super().__init__(name)
        self.class_name = "warrior"
        self.strength = strength
        self.intellect = intellect
        self.dexterity = dexterity
        self.health = (5 + strength) * 10
        self.mana = (10 + self.intellect) * 10
        self.critical_chance = float((1 + self.dexterity) * 1.2)
        self.defense = (3 + self.strength)
        self.special_attack_mana_cost = 20
        self.is_alive = True
    
    def __repr__(self) -> str:
        return f'Name: {self.name} | Class: {self.class_name}\nSTR: {self.strength} | INT: {self.intellect} | DEX: {self.dexterity}\nHP: {self.health} | MP: {self.mana} | CRIT: {self.critical_chance}'
    
    
    def take_damage(self, damage : int):
        self.health -= (damage - self.defense)
        if self.health <= 0:
            self.is_alive = False
    
    def basic_attack(self, target: Enemy):
        is_crit = roll_crit(self.critical_chance)
        if is_crit:
            print("Critical Strike!\nAttacking: " + str(target))
            target.take_damage(self.strength * 2)
        else:
            print("Attacking: " + str(target))
            target.take_damage(self.strength)
        for i in range(5):
                print('.')
                time.sleep(0.5)
        system('clear')

    def special_attack(self, target: Enemy):
        if self.mana >= self.special_attack_mana_cost:
            self.mana -= self.special_attack_mana_cost
            print("Attacking: " + str(target))
            target.take_damage(self.strength + self.intellect)
            for i in range(5):
                print('.')
                time.sleep(0.5)
            system('clear')
        else:
            print("Not enough mana...")
    
    def heal(self):
        self.health += 2 * self.intellect

class Sorcerer(Player):
    def __init__(self, name : str, strength : int, intellect : int, dexterity : int):
        super().__init__(name)
        self.class_name = "sorcerer"
        self.strength = strength
        self.intellect = intellect
        self.dexterity = dexterity
        self.health = (3 + strength) * 10
        self.mana = (18 + self.intellect) * 10
        self.critical_chance = float((1 + self.dexterity) * 1.2)
        self.defense = (1 + self.strength)
        self.special_attack_mana_cost = 20
        self.is_alive = True
    
    def __repr__(self) -> str:
        return f'Name: {self.name} | Class: {self.class_name}\nSTR: {self.strength} | INT: {self.intellect} | DEX: {self.dexterity}\nHP: {self.health} | MP: {self.mana} | CRIT: {self.critical_chance}'
    
    
    def take_damage(self, damage : int):
        self.health -= (damage - self.defense)
        if self.health <= 0:
            self.is_alive = False
    
    def basic_attack(self, target: Enemy):
        is_crit = roll_crit(self.critical_chance)
        if is_crit:
            print("Critical Strike!\nAttacking: " + str(target))
            target.take_damage(self.intellect * 2)
        else:
            print("Attacking: " + str(target))
            target.take_damage(self.intellect)
        for i in range(5):
                print('.')
                time.sleep(0.5)
        system('clear')

    def special_attack(self, target: Enemy):
        if self.mana >= self.special_attack_mana_cost:
            self.mana -= self.special_attack_mana_cost
            print("Attacking: " + str(target))
            target.take_damage(self.strength + self.intellect)
            for i in range(5):
                print('.')
                time.sleep(0.5)
            system('clear')
        else:
            print("Not enough mana...")
    
    def heal(self):
        self.health += 2 * self.intellect