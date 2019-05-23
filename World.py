from PlayerClasses import Player
from EnemyClasses import Enemy
from MenuClasses import *


def iterate(hit_boxes):
    for entity in entities:
        hit_boxes[entity.x][entity.y] = "0"

    for entity in entities:
        hit_boxes[entity.x][entity.y] = " "
        entity.walk(hit_boxes)
        hit_boxes[entity.x][entity.y] = "0"


def load_map(name):

    board_underneath = []

    read = open(name + ".txt", "r")
    world_lines = read.readlines()
    read.close()

    for line in world_lines:
        board_underneath.append([x for x in line.strip('\n')])

    hit_boxes_underneath = []

    for row in board_underneath:
        line = []
        for pixel in row:
            if pixel == "+" or pixel == "-" or pixel == "|" or pixel == "O":
                line.append("1")
            elif pixel == "D":
                line.append("0")
            else:
                line.append(" ")
        hit_boxes_underneath.append(line)

    #read = open(name + " Hit Boxes.txt", "r")
    #world_lines = read.readlines()
    #read.close()

    #for line in world_lines:
    #    hit_boxes_underneath.append([x for x in line.strip('\n')])

    return board_underneath, hit_boxes_underneath


board_underneath, hit_boxes_underneath = load_map("Houses2")

read = open("save_game.txt", "r")
raw_info = read.readlines()
read.close()

info = []

for each in raw_info:
    info.append(each.strip('\n'))

x = int(info[0])
y = int(info[1])
points = int(info[2])
health = int(info[3])
character = info[4]

print(info)

curiosities = info[5].split("/")
curiosities.pop(0)

potions = info[6].split("/")
potions.pop(0)

weapons = info[7].split("/")
weapons.pop(0)

x_parameters = len(board_underneath) - 1
y_parameters = len(board_underneath[1]) - 1

player = Player(x, y, x_parameters, y_parameters, points, character, health, curiosities, potions, weapons)
enemy1 = Enemy(19, 19, x_parameters, y_parameters, player)
enemy2 = Enemy(0, 19, x_parameters, y_parameters, player)
enemy3 = Enemy(19, 0, x_parameters, y_parameters, player)

entities = [enemy1, enemy2, enemy3]

menu = Menu(player, board_underneath)

while True:

    Screen = []

    top_string = "+ - | Map |" + " -" * (y_parameters - 4) + " +"
    bottom_string = "+" + " -" * (y_parameters + 1) + " +"

    hit_boxes = []

    for each_line in hit_boxes_underneath:
        line = []
        for each_point in each_line:
            line.append(each_point)
        hit_boxes.append(line)

    board = []

    for each_line in board_underneath:
        line = []
        for each_point in each_line:
            line.append(each_point)
        board.append(line)

    strings = []
    if board[player.x][player.y] == "C":
        board_underneath[player.x][player.y] = " "
        player.random_collect()
        player.points += 1

    if board[player.x][player.y] == "#":
        board[player.x][player.y] = "*"
    else:
        board[player.x][player.y] = player.character
    for enemy in entities:
        if board[enemy.x][enemy.y] == "#":
            board[enemy.x][enemy.y] = "*"
        else:
            board[enemy.x][enemy.y] = "E"

    for x_axis in board:
        string = ""
        for y_axis in x_axis:
            string = string + " " + y_axis
        strings.append(string)
    Screen.append("\n" * 20)
    Screen.append("""
 _______ ______  _    _ _______ __   _ _______ _     _  ______ _______
 |_____| |     \  \  /  |______ | \  |    |    |     | |_____/ |______
 |     | |_____/   \/   |______ |  \_|    |    |_____| |    \_ |______
  ______ _______ _______ _______
 |  ____ |_____| |  |  | |______
 |_____| |     | |  |  | |______              
""")
    Screen.append("Points: " + str(player.points) + "     Health: " + str(player.health))
    Screen.append(top_string)
    for each in strings:
        Screen.append("|" + each + " |")
    Screen.append(bottom_string)

    for enemy in entities:
        if enemy.x == player.x and enemy.y == player.y:
            player.health -= 1

    if player.health < 0:
        Screen.append("GAME OVER")

        Screen_string = ""

        for line in Screen:
            Screen_string = Screen_string + "\n" + line

        print(Screen_string)
        input("")
        wright = open("save_game.txt", "w")
        wright.write(str(2) + "\n" + str(3) + "\n" + str(0) + "\n" + str(10) + "\n" + str(player.character) + "\n" + "\n" + "\n" + "\n-")
        wright.close()
        break

    index = 0

    Side_menu = menu.show()

    for each in Side_menu:
        Screen[index + 3] = Screen[index + 3] + "   " + each
        index += 1

    Screen_string = ""

    for line in Screen:
        Screen_string = Screen_string + "\n" + line

    print(Screen_string)

    instruction = input(":")

    if instruction == "w" or instruction == "a" or instruction == "s" or instruction == "d" or instruction == "W" or instruction == "A" or instruction == "S" or instruction == "D":
        player.walk(instruction, hit_boxes)
        iterate(hit_boxes)

    elif instruction.lower() == "q":
        curios = ""
        for curiosity in player.curiosities:
            curios = curios + "/" + curiosity
        potions_string = ""
        for potion in player.potions:
            potions_string = potions_string + "/" + potion
        weapons_string = ""
        for weapon in player.weapons:
            weapons_string = weapons_string + "/" + weapon
        wright = open("save_game.txt", "w")
        wright.write(str(player.x) + "\n" + str(player.y) + "\n" + str(player.points) + "\n" + str(player.health) + "\n"
                     + str(player.character) + "\n" + str(curios) + "\n" + str(potions_string) + "\n" + str(weapons_string) + "\n-")
        wright.close()
        break

    elif instruction.lower() == "c":
        while True:
            new_character = input(":")
            if len(new_character) == 1:
                player.character = new_character
                break

    elif instruction == "":
        iterate(hit_boxes)

    else:
        menu.navigate(instruction)



