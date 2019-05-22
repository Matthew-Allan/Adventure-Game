from GameClasses import *
try:
    from colorama import *
except ModuleNotFoundError:
    from BlackAndWhite import *

def scoreboard(amount_monsters_killed):
    write = open("Scoreboard.txt", "a")
    write.write("Name:{0}, Monsters Killed:{1}, Money Made:{2}, Primary Weapon:{3}, Secondary Weapon:{4}\n".format(player.name, amount_monsters_killed, player.money, player.weapons["Primary"].name, player.weapons["Secondary"].name))
    write.close()

def show_scoreboard():
    read = open("Scoreboard.txt", "r")
    lines = read.readlines()
    print("Scoreboard:\n")
    for line in lines:
        print(line)

amount_monsters_killed = 0
        
print(">--<({0}o{1})>----------<({0}o{1})>--<".format(Fore.LIGHTCYAN_EX, Fore.RESET))
print("|    <{0}ADVENTURE GAME{1}>    |".format(Fore.MAGENTA, Fore.RESET))
print(">--<(by {0}Matthew Allan{1})>--<".format(Fore.LIGHTCYAN_EX, Fore.RESET))

name = input("\nPlease add a name:\n>>>")

player = Player(name)

weapon = Weapon()
weapon.default("Right")

player.weapons["Primary"] = weapon

weapon = Weapon()
weapon.default("Left")

player.weapons["Secondary"] = weapon

player.potions = ["Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion", "Lesser Health Potion"]

while True:
    monster = Monster()
    monster.make_stats()
    print("\nYou encounter a " + str(monster.name) + "!")
    while monster.health > 0 and player.health > 0:
        while True:
            input("\nPress {0}ENTER{1} to continue.".format(Fore.LIGHTMAGENTA_EX, Fore.RESET))

            print("\nYou:")
            print("{0}Health{1}:           ".format(Fore.RED, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.health) + "{0} HP".format(Fore.RESET))
            print("{0}Armor{1}:            ".format(Fore.WHITE, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.armor) + "{0} HP".format(Fore.RESET))
            print("{0}Money{1}:            ".format(Fore.YELLOW, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.money) + "{0}G".format(Fore.RESET))
            print("{0}Weapon{1} ({2}P{1}):       ".format(Fore.MAGENTA, Fore.RESET, Fore.LIGHTCYAN_EX) + player.weapons["Primary"].name + "{0}".format(Fore.RESET))
            print("  -{0}Damage{1}:        ".format(Fore.RED, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Primary"].damage) + "{0}".format(Fore.RESET))
            print("  -{0}Weight{1}:        ".format(Fore.LIGHTBLACK_EX, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Primary"].weight) + "{0}".format(Fore.RESET))
            print("  -{0}Crit Chance{1}:   ".format(Fore.LIGHTMAGENTA_EX, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Primary"].crit_chance) + "{0}%".format(Fore.RESET))
            print("{0}Weapon{1} ({2}S{1}):       ".format(Fore.MAGENTA, Fore.RESET, Fore.CYAN) + player.weapons["Secondary"].name + "{0}".format(Fore.RESET))
            print("  -{0}Damage{1}:        ".format(Fore.RED, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Secondary"].damage) + "{0}".format(Fore.RESET))
            print("  -{0}Weight{1}:        ".format(Fore.LIGHTBLACK_EX, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Secondary"].weight) + "{0}".format(Fore.RESET))
            print("  -{0}Crit Chance{1}:   ".format(Fore.LIGHTMAGENTA_EX, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(player.weapons["Secondary"].crit_chance) + "{0}%".format(Fore.RESET))
            print("{0}a{1}: Check monster     {0}b{1}: Revamp a weapon (cost = 100G) ({2}ends your go{1})     {0}c{1}: Drink Potion ({2}ends your go{1})     {0}d{1}: Hit monster ({2}ends your go{1})".format(Fore.LIGHTGREEN_EX, Fore.RESET, Fore.LIGHTRED_EX))
            choice = input("{0}>>>{1}".format(Fore.YELLOW, Fore.RESET)).lower()
            if choice == "a":
                print()
                monster.stats()
                continue
            elif choice == "b":
                if player.money < 100:
                    print("Sorry no can do")
                    continue
                print()
                while True:
                    print("a: Revamp primary     b: Revamp secondary     c: Cancel")
                    choice = input(">>>").lower()
                    if choice == "a":
                        if player.weapons["Primary"].name == "Right Fist":
                            print("Sorry no can do")
                            continue
                    if choice == "b":
                        if player.weapons["Secondary"].name == "Left Fist":
                            print("Sorry no can do")
                            continue
                    if choice == "a" or choice == "b":
                        print()
                        print("Are you sure? Doing this will replace your current weapons powers (y/n)")
                        boolian_choice = input(">>>").lower()
                        if boolian_choice == "n":
                            break
                        elif boolian_choice == "y":
                            if choice == "a":
                                original_name = player.weapons["Primary"].name
                                player.weapons["Primary"].revamp()
                                print("\nYour " + original_name + " has become a " + player.weapons["Primary"].name)
                                player.money -= 100
                                break
                            else:
                                original_name = player.weapons["Secondary"].name
                                player.weapons["Secondary"].revamp()
                                print("\nYour " + original_name + " has become a " + player.weapons["Secondary"].name)
                                player.money -= 100
                                break
                    elif choice == "c":
                        break
                
                if choice == "c":
                    continue
                print()
                break

            elif choice == "c":
                if len(player.potions) == 0:
                    print("Sorry no can do")
                    continue
                print()
                while True:
                    x = 1
                    for each in player.potions:
                        print(str(x) + ") " + each)
                        x += 1
                    print("c) Cancel")
                    choice = input("{0}>>>{1}".format(Fore.YELLOW, Fore.RESET)).lower()
                    if choice == "c":
                        break
                    try:
                        choice = int(choice)
                    except ValueError:
                        print("That is not an option!")
                        continue
                    if choice > len(player.potions) or choice < 1:
                        print("That is not an option!")
                        continue
                    player.heal(choice - 1)
                    break
                if choice == "c":
                    continue
                print()
                break
            
            elif choice == "d":
                print()
                if random.randint(1, 10) < 9:
                    monster.hit_with(player.weapons["Primary"])
                else:
                    print("You swung at the " + monster.name + " with your " + player.weapons["Primary"].name + " but {0}missed{1}!".format(Fore.RED, Fore.RESET))
                if monster.health > 0:
                    if random.randint(1, 10) < 9:
                        monster.hit_with(player.weapons["Secondary"])
                    else:
                        print("You swung at the " + monster.name + " with your " + player.weapons["Secondary"].name + " but {0}missed{1}!".format(Fore.RED, Fore.RESET))
                break
            else:
                print()
                print(choice + " is not an option.")
                continue
        if monster.health > 0:
            if random.randint(1, 10) < 8:
                player.hit(monster)
            else:
                print("what")
                print("The " + monster.name + " swung and {0}missed{1}!".format(Fore.RED, Fore.RESET))
    
    if monster.health == 0:
        amount_monsters_killed += 1
    
    if player.health == 0:
        print("\nGAME OVER\n\nHope you had fun!\n\nYou killed {} monsters!".format(amount_monsters_killed))
        scoreboard(amount_monsters_killed)
        show_scoreboard()
        break
    
    weapon = Weapon()
    weapon.make_stats()
    player.money += monster.worth
    print("\n+" + str(monster.worth) + "g!")
    potion_name = player.give_potion()
    print("\nYou got a " + potion_name + "!")
    
    while True:    
        print("\nYou got a " + weapon.name + "!\n\na:Check new weapon     b:Put new weapon in primary     c:Put new weapon in secondary     d:Drop new weapon")
        choice = input(">>>").lower()
        if choice == "a":
            print()
            weapon.stats()
            continue
        elif choice == "b" or choice == "c":
            print()
            print("Are you sure? Doing this will drop your current weapon (y/n)")
            boolian_choice = input(">>>").lower()
            if boolian_choice == "n":
                continue
            elif boolian_choice == "y":
                if choice == "b":
                    player.weapons["Primary"] = weapon
                    break
                else:
                    player.weapons["Secondary"] = weapon
                    break
        elif choice == "d":
            print("You dropped the " + weapon.name)
            break
        
input()
