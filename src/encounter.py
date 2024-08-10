import enemy

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

class EnemyEncounter(Encounter):
    def __init__(self, code, player):
        super().__init__(code, player)

        if code == 'S':
            self.enemy = enemy.Slime("Tom", 12, 3)
        
    def play_encounter(self):
        print(f'\n\n{self.enemy}\n\n')

        while self.player.health > 0 and self.enemy.health > 0:
            player_choice = input('What will you do...\n1. Basic Attack\n2. Special Attack\n3. Heal\n')

            match player_choice:
                case '1':
                    self.player.basic_attack(self.enemy)
                case '2':
                    self.player.special_attack(self.enemy)
                case '3':
                    self.player.heal()
