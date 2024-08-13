from player import Player, Warrior, Sorcerer
from map import Map
import room
from os import system

map = Map()

def initialize_game():
    player_name = input('Enter your character\'s name... ')
    valid_class_selectors = ['1', '2', '3']
    player_class = input('Select your class\n1. Warrior\n2. Sorcerer\n3. Rogue\n')
    while player_class not in valid_class_selectors:
        player_class = input('Select your class\n1. Warrior\n2. Sorcerer\n3. Rogue\n')
    system('clear')

    match player_class:
        case '1':
            player = Warrior(player_name, 10, 5, 6)
        case '2':
            player = Sorcerer(player_name, 7, 12, 7)
        case '3':
            print("Not implemented")
            exit()


    

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
        try:
            next_room_code = map.cells[player.position[0] + dir[0]][player.position[1] + dir[1]]
        except IndexError:
            next_room_code = 'W'

        chose_wall = False

        if next_room_code == 'W':
            chose_wall = True
            print('You cannot walk through walls...')

        if not chose_wall:
            next_room = room.Room(next_room_code, player)

            map.cells[player.position[0]][player.position[1]] = '#'
            player.move(dir)
            map.cells[player.position[0]][player.position[1]] = 'P'

            next_room.encounter.play_encounter()
            system('clear')

        game_loop(player)

initialize_game()