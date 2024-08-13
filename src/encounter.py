import enemy
from os import system

class Encounter:
    def __init__(self, code, player):
        self.code = code
        self.player = player
    
    def play_encounter():
        pass

class EmptyRoomEncounter(Encounter):
    def __init__(self, code, player):
        super().__init__(code, player)
    
    def play_encounter(self):
        print("\n\nThis is an empty room...\n\n")

class ExitEncounter(Encounter):
    def __init__(self, code, player):
        super().__init__(code, player)
    
    def play_encounter(self):
        print(f'You\'ve made it to the exit! Congratulations!\n{self.player}\n')
        input("Press enter to exit the game...")

class EnemyEncounter(Encounter):
    def __init__(self, code, player):
        super().__init__(code, player)

        if code == 'S':
            self.enemy = enemy.Slime("Tom", 12, 3)
        
    def play_encounter(self):

        while self.player.health > 0 and self.enemy.health > 0:
            print(f'\n{self.enemy}\n')
            print(f'\n{self.player}\n')
            player_choice = input('What will you do...\n1. Basic Attack\n2. Special Attack\n3. Heal\n')

            match player_choice:
                case '1':
                    self.player.basic_attack(self.enemy)
                case '2':
                    self.player.special_attack(self.enemy)
                case '3':
                    self.player.heal()
            system('clear')
            if self.enemy.health > 0:
                print(f'\n{self.enemy}\n')
                print(f'\n{self.player}\n')

                self.enemy.basic_attack(self.player)
