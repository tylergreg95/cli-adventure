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
    
    def __repr__(self):
        return f'{self.name} the {self.enemy_type} | HP: {self.health} | DEF: {self.defense}'