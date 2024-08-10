import encounter

class Room:
    def __init__(self, code, player):
        

        match code:
            case '#':
                self.encounter = encounter.EmptyRoomEncounter(code, player)
            
            case 'S':
                self.encounter = encounter.EnemyEncounter('S', player)