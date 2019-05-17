from colorama import *
from GameClasses import *

print(">--<({0}o{1})>----------<({0}o{1})>--<".format(Fore.LIGHTCYAN_EX, Fore.RESET))
print("|    <{0}ADVENTURE GAME{1}>    |".format(Fore.MAGENTA, Fore.RESET))
print(">--<(by {0}Matthew Allan{1})>--<".format(Fore.LIGHTCYAN_EX, Fore.RESET))

weaponP = Weapon()
weaponP.default("Right")

weaponS = Weapon()
weaponS.default("Left")

monster = Monster()
monster.make_stats()
print("\nYou encounter a " + str(monster.name) + "!")

player = Player()
player.weapons["Primary"] = weaponP
player.weapons["Secondary"] = weaponS

while monster.health > 0 and player.health > 0:
    while True:
        input("\nPress {0}ENTER{1} to continue.".format(Fore.LIGHTMAGENTA_EX, Fore.RESET))

        print("\nYou:")
        print("{0}Health{1}:           ".format(Fore.RED, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.health) + "{0} HP".format(Fore.RESET))
        print("{0}Armor{1}:            ".format(Fore.WHITE, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.armor) + "{0} HP".format(Fore.RESET))
        print("{0}Weapon{1} ({2}P{1}):       ".format(Fore.MAGENTA, Fore.RESET, Fore.LIGHTCYAN_EX) + player.weapons["Primary"].name + "{0}".format(Fore.RESET))
        print("{0}Weapon{1} ({2}S{1}):       ".format(Fore.MAGENTA, Fore.RESET, Fore.CYAN) + player.weapons["Secondary"].name + "{0}".format(Fore.RESET))
        print("  -{0}Damage{1}:        ".format(Fore.RED, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Primary"].damage) + "{0}".format(Fore.RESET))
        print("  -{0}Weight{1}:        ".format(Fore.LIGHTBLACK_EX, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Primary"].weight) + "{0}".format(Fore.RESET))
        print("  -{0}Crit Chance{1}:   ".format(Fore.LIGHTMAGENTA_EX, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Primary"].crit_chance) + "{0}%".format(Fore.RESET))
        print("{0}a{1}: Check monster     {0}b{1}: Hit monster ({2}ends your go{1})".format(Fore.LIGHTGREEN_EX, Fore.RESET, Fore.LIGHTRED_EX))
        choice = input("{0}>>>{1}".format(Fore.YELLOW, Fore.RESET)).lower()
        if choice == "a":
            print()
            monster.stats()
            continue
        elif choice == "b":
            print()
            if random.randint(1, 10) < 9:
                monster.hit_with(player.weapons["Primary"])
            else:
                print("You swung at the " + monster.name + " with your " + player.weapons["Primary"].name + " but {0}missed{1}!".format(Fore.RED, Fore.RESET))
            if random.randint(1, 10) < 9:
                if monster.health > 0:
                    monster.hit_with(player.weapons["Secondary"])
            else:
                print("You swung at the " + monster.name + " with your " + player.weapons["Secondary"].name + " but {0}missed{1}!".format(Fore.RED, Fore.RESET))
            break
        else:
            print()
            print(choice + " is not an option.")
            continue
    if random.randint(1, 10) < 8:
        if monster.health > 0:
            player.hit(monster)
    else:
        print("The " + monster.name + " swung and {0}missed{1}!".format(Fore.RED, Fore.RESET))


