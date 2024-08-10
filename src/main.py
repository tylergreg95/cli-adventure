from player import Player, Warrior
from map import Map
import room
from os import system

map = Map()

def initialize_game():
    player_name = input('Enter your character\'s name... ')
    system('clear')
    player = Warrior(player_name, 10, 5, 6)

    

    # Place player at beginning
    player.position = map.entrance
    map.cells[player.position[0]][player.position[1]] = 'P'

    #print(f'EXIT: {map.exit[0]} : {map.exit[1]}')

    game_loop(player)

def choose_direction() -> list[int]:
    valid_direction_choices = ['1', '2', '3', '4']

    dir = []

    direction_choice = input("Select a direciton...\n1. Up\n2. Down\n3. Left\n4. Right\n")

    while direction_choice not in valid_direction_choices:
        print('Invalid choice')
        direction_choice = input('Select a direciton...\n1. Up\n2. Down\n3. Left\n4. Right\n')

    match direction_choice:
        case '1':
            dir.append(-1)
            dir.append(0)
        case '2':
            dir.append(1)
            dir.append(0)
        case '3':
            dir.append(0)
            dir.append(-1)
        case '4':
            dir.append(0)
            dir.append(1)
    return dir

def game_loop(player: Player):
    map.show_map()
    #print(f'PLAYER: {player.position[0]} : {player.position[1]}')
    # if the player is not at the exit, continuously call game_loop()
    while player.position[0] != map.exit[0] or player.position[1] != map.exit[1]:
        dir = choose_direction()

        system('clear')

        next_room_code = map.cells[player.position[0] + dir[0]][player.position[1] + dir[1]]
        next_room = room.Room(next_room_code, player)

        map.cells[player.position[0]][player.position[1]] = '#'
        player.move(dir)
        map.cells[player.position[0]][player.position[1]] = 'P'

        next_room.encounter.play_encounter()
        system('clear')

        game_loop(player)

initialize_game()