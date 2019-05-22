
import random
try:
    from colorama import *
except ModuleNotFoundError:
    from BlackAndWhite import *

class Weapon:

    def __init__(self):
        weapon_types = ["Sword", "Dagger", "Blade", "Mace", "Nunchucks", "Bat", "Club", "Bow"]
        weapon_adjectives = ["Wooden", "Metal", "Diamond", "Sharp", "Blunt", "Broken", "Chipped", "Dented", "Godly", "Magic"]
        self.adjective = random.choice(weapon_adjectives)
        self.type = random.choice(weapon_types)

    def make_stats(self):
        if self.type == "Sword":
            self.damage = 45
            self.crit_chance = 10
            self.weight = 25

        elif self.type == "Fist":
            pass

        elif self.type == "Dagger":
            self.damage = 35
            self.crit_chance = 15
            self.weight = 5

        elif self.type == "Blade":
            self.damage = 35
            self.crit_chance = 15
            self.weight = 5

        elif self.type == "Mace":
            self.damage = 55
            self.crit_chance = 50
            self.weight = 50

        elif self.type == "Nunchucks":
            self.damage = 20
            self.crit_chance = 10
            self.weight = 10

        elif self.type == "Bat":
            self.damage = 45
            self.crit_chance = 40
            self.weight = 40

        elif self.type == "Club":
            self.damage = 45
            self.crit_chance = 40
            self.weight = 40

        elif self.type == "Bow":
            self.damage = 35
            self.crit_chance = 20
            self.weight = 5

        else:
            print("missed one")

        if self.adjective == "Wooden":
            self.adjective = "{0}{1}{2}".format(Fore.LIGHTRED_EX, self.adjective, Fore.RESET)
            self.damage += 5
            self.crit_chance += 1
            self.weight += 10

        elif self.adjective == "Metal":
            self.adjective = "{0}{1}{2}".format(Fore.WHITE, self.adjective, Fore.RESET)
            self.damage += 10
            self.crit_chance += 3
            self.weight += 20

        elif self.adjective == "Diamond":
            self.adjective = "{0}{1}{2}".format(Fore.LIGHTCYAN_EX, self.adjective, Fore.RESET)
            self.damage += 20
            self.crit_chance += 5
            self.weight += 10

        elif self.adjective == "Sharp":
            self.adjective = "{0}{1}{2}".format(Fore.WHITE, self.adjective, Fore.RESET)
            self.damage += 15
            self.crit_chance += 4
            self.weight += 5

        elif self.adjective == "Blunt":
            self.adjective = "{0}{1}{2}".format(Fore.WHITE, self.adjective, Fore.RESET)
            self.damage -= 3
            self.crit_chance -= 1
            self.weight += 0

        elif self.adjective == "Broken":
            self.adjective = "{0}{1}{2}".format(Fore.WHITE, self.adjective, Fore.RESET)
            self.damage -= 5
            self.crit_chance -= 5
            self.weight -= 2

        elif self.adjective == "Chipped":
            self.adjective = "{0}{1}{2}".format(Fore.LIGHTRED_EX, self.adjective, Fore.RESET)
            self.damage -= 2
            self.crit_chance -= 1
            self.weight -= 1

        elif self.adjective == "Dented":
            self.adjective = "{0}{1}{2}".format(Fore.WHITE, self.adjective, Fore.RESET)
            self.damage -= 1
            self.crit_chance -= 1
            self.weight += 0

        elif self.adjective == "Godly":
            self.adjective = "{0}{1}{2}".format(Fore.LIGHTYELLOW_EX, self.adjective, Fore.RESET)
            self.damage += 50
            self.crit_chance += 20
            self.weight += 0

        elif self.adjective == "Magic":
            self.adjective = "{0}{1}{2}".format(Fore.MAGENTA, self.adjective, Fore.RESET)
            self.damage += 40
            self.crit_chance += 10
            self.weight += 0

        else:
            print("missed one")

        if self.damage < 1:
            self.damage = 1

        if self.weight < 1:
            self.weight = 1

        if self.crit_chance < 0:
            self.crit_chance = 0

        elif self.crit_chance > 100:
            self.crit_chance = 100

        self.name = self.adjective + " " + self.type

    def stats(self):
        print("Stats:")
        print("Name:        " + self.name)
        print("Damage:      " + str(self.damage))
        print("Crit chance: " + str(self.crit_chance) + "%")
        print("Weight:      " + str(self.weight))

    def default(self, hand):
        self.adjective = "{0}{1}{2}".format(Fore.RED, hand, Fore.RESET)
        self.type = "Fist"
        self.name = self.adjective + " " + self.type
        self.weight = 5
        self.crit_chance = 1
        self.damage = 5

    def revamp(self):
        weapon_adjectives = ["Wooden", "Metal", "Diamond", "Sharp", "Blunt", "Broken", "Chipped", "Dented", "Godly", "Magic"]
        self.adjective = random.choice(weapon_adjectives)
        self.make_stats()
        

class Monster:

    def __init__(self):
        monster_types = ["Zombie", "Skeleton", "Witch", "Ghoul", "Hunk", "Snake"]
        monster_adjectives = ["Large", "Strong", "Weak", "Fast", "Deadly", "Heavy", "Tiny", "Powerful", "Evil"]
        self.adjective = random.choice(monster_adjectives)
        self.type = random.choice(monster_types)
        self.worth = 0

    def make_stats(self):
        if self.type == "Zombie":
            self.damage = 30
            self.crit_chance = 5
            self.weight = 20
            self.health = 100
            self.armor = 20
            self.worth += 50

        elif self.type == "Skeleton":
            self.damage = 35
            self.crit_chance = 10
            self.weight = 5
            self.health = 150
            self.armor = 50
            self.worth += 70

        elif self.type == "Witch":
            self.damage = 50
            self.crit_chance = 20
            self.weight = 20
            self.health = 1050
            self.armor = 50
            self.worth += 250

        elif self.type == "Ghoul":
            self.damage = 30
            self.crit_chance = 20
            self.weight = 0
            self.health = 1500
            self.armor = 150
            self.worth += 500

        elif self.type == "Hunk":
            self.damage = 100
            self.crit_chance = 40
            self.weight = 100
            self.health = 5000
            self.armor = 350
            self.worth += 2000

        elif self.type == "Snake":
            self.damage = 20
            self.crit_chance = 10
            self.weight = 10
            self.health = 75
            self.armor = 25
            self.worth += 20

        if self.adjective == "Large":
            self.adjective = "{0}{1}{2}".format(Fore.LIGHTBLACK_EX, self.adjective, Fore.RESET)
            self.damage += 15
            self.crit_chance += 5
            self.weight += 15
            self.health += 50
            self.armor += 25
            self.worth += 50

        elif self.adjective == "Strong":
            self.adjective = "{0}{1}{2}".format(Fore.LIGHTBLACK_EX, self.adjective, Fore.RESET)
            self.damage += 10
            self.crit_chance += 5
            self.weight += 15
            self.health += 10
            self.armor += 30
            self.worth += 50

        elif self.adjective == "Weak":
            self.adjective = "{0}{1}{2}".format(Fore.WHITE, self.adjective, Fore.RESET)
            self.damage -= 5
            self.crit_chance -= 3
            self.weight -= 5
            self.health -= 20
            self.armor -= 20
            self.worth -= 10

        elif self.adjective == "Fast":
            self.adjective = "{0}{1}{2}".format(Fore.LIGHTCYAN_EX, self.adjective, Fore.RESET)
            self.damage += 10
            self.crit_chance += 10
            self.weight -= 5
            self.health -= 50
            self.armor = 0
            self.worth += 60

        elif self.adjective == "Deadly":
            self.adjective = "{0}{1}{2}".format(Fore.MAGENTA, self.adjective, Fore.RESET)
            self.damage += 20
            self.crit_chance += 15
            self.weight += 10
            self.health += 5
            self.armor += 15
            self.worth += 100

        elif self.adjective == "Heavy":
            self.adjective = "{0}{1}{2}".format(Fore.LIGHTBLACK_EX, self.adjective, Fore.RESET)
            self.damage += 5
            self.crit_chance -= 5
            self.weight += 20
            self.health += 100
            self.armor += 50
            self.worth += 100

        elif self.adjective == "Tiny":
            self.adjective = "{0}{1}{2}".format(Fore.WHITE, self.adjective, Fore.RESET)
            self.damage += 10
            self.crit_chance += 15
            self.weight -= 5
            self.health -= 20
            self.armor -= 50
            self.worth -= 10

        elif self.adjective == "Powerful":
            self.adjective = "{0}{1}{2}".format(Fore.YELLOW, self.adjective, Fore.RESET)
            self.damage += 20
            self.crit_chance += 20
            self.weight += 15
            self.health += 30
            self.armor += 20
            self.worth += 100

        elif self.adjective == "Evil":
            self.adjective = "{0}{1}{2}".format(Fore.RED, self.adjective, Fore.RESET)
            self.damage += 30
            self.crit_chance += 10
            self.weight += 5
            self.health += 20
            self.armor += 20
            self.worth += 100

        if self.damage < 1:
            self.damage = 1

        if self.weight < 1:
            self.weight = 1

        if self.health < 10:
            self.health = 10

        if self.armor < 0:
            self.armor = 0

        if self.crit_chance < 0:
            self.crit_chance = 0

        elif self.crit_chance > 100:
            self.crit_chance = 100

        self.name = self.adjective + " " + self.type

    def hit_with(self, weapon):
        player_weight, player_damage, player_crit_chance = weapon.weight, weapon.damage, weapon.crit_chance
        if self.armor == 0:
            damage_health = True
        else:
            damage_health = False
        if random.randint(1, 100) <= player_crit_chance:
            player_damage = player_damage * 3
            player_weight = player_weight * 2

        if damage_health == False:
            self.armor = max(0, self.armor - player_weight)
            print("You hit the " + self.name + "'s armor with your " + weapon.name + " for {0}".format(Fore.YELLOW) + str(player_weight) + "{0}!".format(Fore.RESET))
            if self.armor == 0:
                print("You destroyed the " + self.name + "'s armor with your " + weapon.name + "!")
        else:
            player_damage += player_weight
            self.health -= player_damage
            print("You hit the " + self.name + " with your " + weapon.name + " for {0}".format(Fore.YELLOW) + str(player_damage) + "{0}!".format(Fore.RESET))
            if self.health < 0:
                self.health = 0
            if self.health == 0:
                print("You {}killed{} the ".format(Fore.RED, Fore.RESET) + self.name + " with your " + weapon.name + "!")
                

    def stats(self):
        print("Monster:")
        print("{0}Name{1}:             ".format(Fore.YELLOW, Fore.RESET) + self.name)
        print("{0}Health{1}:           ".format(Fore.RED, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(self.health) + "{0} HP".format(Fore.RESET))
        print("{0}Armor{1}:            ".format(Fore.WHITE, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(self.armor) + "{0} HP".format(Fore.RESET))
        print("{0}Damage{1}:           ".format(Fore.RED, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(self.damage) + "{0}".format(Fore.RESET))
        print("{0}Weight{1}:           ".format(Fore.LIGHTBLACK_EX, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(self.weight) + "{0}".format(Fore.RESET))
        print("{0}Crit chance{1}:      ".format(Fore.LIGHTMAGENTA_EX, Fore.RESET) + "{0}".format(Fore.YELLOW) + str(self.crit_chance) + "{0}%".format(Fore.RESET))

class Player:

    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.armor = 1000
        self.weapons = {"Primary": None, "Secondary": None}
        self.potions = ["Lesser Health Potion", "Lesser Health Potion"]
        self.money = 0

    def hit(self, monster):
        monster_damage, monster_crit_chance, monster_weight = monster.damage, monster.crit_chance, monster.weight
        if self.armor == 0:
            damage_health = True
        else:
            damage_health = False
        if random.randint(1, 100) <= monster_crit_chance:
            monster_damage = monster_damage * 3
            monster_weight = monster_weight * 2

        if damage_health == False:
            self.armor = max(0, self.armor - monster_weight)
            print("The " + monster.name + " {0} {1}armor{2}!".format(random.choice(["ripped out a chunk of your", "dented your", "put a chink in your"]), Fore.WHITE, Fore.RESET))
            if self.armor == 0:
                print("The " + monster.name + " has destroyed your armor!")
        else:
            monster_damage += monster_weight
            self.health -= monster_damage
            print("The " + monster.name + " has hit you for {0}".format(Fore.YELLOW) + str(monster_damage) + "{0}!".format(Fore.RESET))
            if self.health < 0:
                self.health = 0
            if self.health == 0:
                print("The " + monster.name + " has killed you!!")

    def stats(self):
        print("Stats:")
        print("Name:        You")
        print("Health:      " + str(self.health) + "HP")
        print("Armor:       " + str(self.armor) + "HP")

    def heal(self, potion_indx):
        if self.potions[potion_indx] == "Lesser Health Potion":
            self.health += 100
        elif self.potions[potion_indx] == "Greater Health Potion":
            self.health += 1000
        elif self.potions[potion_indx] == "Lesser Armor Potion":
            self.armor += 100
        elif self.potions[potion_indx] == "Greater Armor Potion":
            self.armor += 1000
        self.potions.pop(potion_indx)

    def give_potion(self):
        potion_lvls = ["Lesser ", "Geater "]
        potion_types = ["Armor ", "Health "]
        potion_lvl = random.choice(potion_lvls)
        potion_type = random.choice(potion_types)
        potion_name = potion_lvl + potion_type + "Potion"
        self.potions.append(potion_name)
        return potion_name

        self.potions.pop(potion_indx)
        


