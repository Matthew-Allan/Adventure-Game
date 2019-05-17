from PlayerClasses import Player

map_size = "small area"

log = ["You encountered a Large Ghoul", "You defeated the Large Ghoul", "You found a magical dagger"]

player = Player(4, 5, ["0", "1", "0"], 0, 3, 6, "P", 10, ['Carved Watch', 'Christal Encrusted Stick', 'Jade Wring', 'Carved Wring', 'Christal Encrusted Bone', 'Golden Bone', 'Dull Watch', 'Beaded Glove', 'Beaded Watch'], ["Greater Armor Potion", "Lesser Health Potion"])

menu = "Main"

while True:

    screen = []

    print("")

    if menu == "Main":
        screen.append("menu:")
        screen.append("    1) Backpack")
        screen.append("    2) Stats")
        screen.append("    3) Log")
        screen.append("    4) Map Size")

    elif menu == "Backpack":
        screen.append("Backpack:")
        screen.append("    1) Weapons")
        screen.append("    2) Potions")
        screen.append("    3) Curiosities ")

    elif menu == "Stats":
        screen.append("Stats:")
        screen.append("    -Health:    {0}".format(player.health))
        screen.append("    -Gold:      {0}".format(player.points))
        screen.append("    -X/Y:       {0}/{1}".format(player.y, player.x))

    elif menu == "Log":
        screen.append("Log:")

        for each in log:
            screen.append("    > " + each)

    elif menu == "Map Size":
        screen.append("Map Size:")
        if map_size == "small area":
            screen.append(" > (S)mall Area")
            screen.append("   (W)ide Area")
        else:
            screen.append("   (S)mall Area")
            screen.append(" > (W)ide Area")

    elif menu == "Weapons":
        screen.append("Weapons:")
        screen.append("    -Primary:")
        screen.append("        -{0}".format(player.hand["Primary"]))
        screen.append("    -Secondary:")
        screen.append("        -{0}".format(player.hand["Secondary"]))
        screen.append("    -Bag:")
        for weapon in player.weapons:
            screen.append("        -" + weapon)

    elif menu == "Potions":
        screen.append("Potions:")
        number = 1
        for potion in player.potions:
            screen.append("    " + str(number) + ") " + potion)
            number += 1

    elif menu == "Curiosities":
        screen.append("Curiosities:")
        for curiosity in player.curiosities:
            screen.append("    -" + curiosity)

    for each in screen:
        print(each)

    instruction = input(":")

    if menu == "Main":
        if instruction == "1":
            menu = "Backpack"
        elif instruction == "2":
            menu = "Stats"
        elif instruction == "3":
            menu = "Log"
        elif instruction == "4":
            menu = "Map Size"
        elif instruction == "e":
            break

    elif menu == "Backpack":
        if instruction == "1":
            menu = "Weapons"
        elif instruction == "2":
            menu = "Potions"
        elif instruction == "3":
            menu = "Curiosities"
        elif instruction == "e":
            menu = "Main"

    elif menu == "Stats":
        if instruction == "e":
            menu = "Main"

    elif menu == "Log":
        if instruction == "e":
            menu = "Main"

    elif menu == "Map Size":
        if instruction == "s":
            map_size = "small area"
        elif instruction == "w":
            map_size = "wide area"
        elif instruction == "e":
            menu = "Main"

    elif menu == "Weapons":
        if instruction == "e":
            menu = "Backpack"

    elif menu == "Potions":
        if instruction == "e":
            menu = "Backpack"

    elif menu == "Curiosities":
        if instruction == "e":
            menu = "Backpack"
