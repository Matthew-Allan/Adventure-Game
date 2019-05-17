from PlayerClasses import Player

map_size = "small"

log = ["You encountered a Large Ghoul", "You defeated the Large Ghoul", "You found a magical dagger"]

player = Player(4, 5, ["0", "1", "0"], 0, 3, 6, "P", 10)

while True:

    print("""menu:
    1) Backpack
    2) Stats
    3) Log
    4) Map Size""")

    instruction = input(":")

    print("")

    if instruction == "1":
        while True:

            print("""Backpack:
    1) Weapons
    2) Potions
    3) Curiosities """)

            secondary_instruction = input(":")

            print("")

            if secondary_instruction == "e":
                break
            else:
                print("That is not an option\n")
                continue

    elif instruction == "2":
        while True:

            print("""Stats:
    -Health: {0}
    -Gold:   {1}
    -X/Y:     {2}/{3}
            """.format(player.health, player.points, player.y, player.x))

            secondary_instruction = input(":")

            print("")

            if secondary_instruction == "e":
                break
            else:
                print("That is not an option\n")
                continue

    elif instruction == "3":
        print("Log:")

        for each in log:
            print(" > " + each)

        print("")

    elif instruction == "4":
        while True:

            print("Map size:")

            if map_size == "small":
                print(" > small\n   large")
            else:
                print("   (S)mall\n > (L)arge")

            secondary_instruction = input(":").lower()

            print("")

            if secondary_instruction == "s":
                map_size = "small"
                log.append("Map size changed to small")
            elif secondary_instruction == "l":
                map_size = "large"
                log.append("Map size changed to large")
            elif secondary_instruction == "e":
                break
            else:
                print("That is not an option\n")
                continue

    else:
        print("That is not an option\n")
