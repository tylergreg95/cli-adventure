from time import sleep
from os import system

class Enemy:
    def __init__(self, name : str, health : int, defense : int):
        self.name = name
        self.health = health
        self.defense = defense
    
    def take_damage(self, damage : int):
        self.health -= (damage - self.defense)
        if self.health <= 0:
            #trigger death
            pass

class Slime(Enemy):
    def __init__(self, name: str, health: int, defense: int):
        super().__init__(name, health, defense)
        self.enemy_type = "Slime"
        self.attack_power = 20

    def __repr__(self):
        return f'{self.name} the {self.enemy_type} | HP: {self.health} | DEF: {self.defense}'
    
    def basic_attack(self, target):
        print("Attacking: " + str(target))
        target.take_damage(self.attack_power)
        for i in range(5):
                print('.')
                sleep(0.5)
        system('clear')