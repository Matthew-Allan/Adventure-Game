

class Menu:

    def __init__(self, player, board):
        self.player = player
        self.map_size = "small area"
        self.log = ["Log not available yet"]
        self.menu = "Main"
        self.board = board

    def show(self):

        screen = []

        screen.append("+ - - - - - - - - - - - - - - - - - - - +")

        if self.menu == "Main":
            screen.append("   Menu:")
            screen.append("    1) Backpack")
            screen.append("    2) Stats")
            screen.append("    3) Log")
            screen.append("    4) Map Size")

        elif self.menu == "Backpack":
            screen.append("   Backpack:")
            screen.append("    1) Weapons")
            screen.append("    2) Potions")
            screen.append("    3) Curiosities ")

        elif self.menu == "Stats":
            screen.append("   Stats:")
            screen.append("    -Health:    {0}".format(self.player.health))
            screen.append("    -Gold:      {0}".format(self.player.points))
            screen.append("    -X/Y:       {0}/{1}".format(self.player.y, self.player.x))

        elif self.menu == "Log":
            screen.append("   Log:")

            for each in self.log:
                screen.append("     > " + each)

        elif self.menu == "Map Size":
            screen.append("   Map Size:")
            if self.map_size == "small area":
                screen.append("     > 1) Small Area")
                screen.append("       2) Wide Area")
            else:
                screen.append("       1) Small Area")
                screen.append("     > 2) Wide Area")

        elif self.menu == "Weapons":
            screen.append("   Weapons:")
            screen.append("       -Primary:")
            screen.append("           -{0}".format(self.player.hand["Primary"]))
            screen.append("       -Secondary:")
            screen.append("           -{0}".format(self.player.hand["Secondary"]))
            screen.append("       -Bag:")
            for weapon in self.player.weapons:
                screen.append("           -" + weapon)

        elif self.menu == "Potions":
            screen.append("   Potions:")
            number = 1
            for potion in self.player.potions:
                screen.append("    " + str(number) + ") " + potion)
                number += 1

        elif self.menu == "Curiosities":
            screen.append("   Curiosities:")
            for curiosity in self.player.curiosities:
                screen.append("    -" + curiosity)

        for each in range(-1, len(self.board) - len(screen)):
            screen.append("|                                       |")

        screen.append("+ - | Press E to exit | - - - - - - - - +")

        Screen = []

        for each in screen:
            if each[0] == "+" or each[0] == "|":
                Screen.append(each)
                continue
            else:
                each = "|" + each + " " * (39 - len(each)) + "|"
                Screen.append(each)

        return Screen

    def navigate(self, instruction):

        if self.menu == "Main":
            if instruction == "1":
                self.menu = "Backpack"
            elif instruction == "2":
                self.menu = "Stats"
            elif instruction == "3":
                self.menu = "Log"
            elif instruction == "4":
                self.menu = "Map Size"
            elif instruction.lower() == "e":
                print("REEEEE")

        elif self.menu == "Backpack":
            if instruction == "1":
                self.menu = "Weapons"
            elif instruction == "2":
                self.menu = "Potions"
            elif instruction == "3":
                self.menu = "Curiosities"
            elif instruction.lower() == "e":
                self.menu = "Main"

        elif self.menu == "Stats":
            if instruction.lower() == "e":
                self.menu = "Main"

        elif self.menu == "Log":
            if instruction.lower() == "e":
                self.menu = "Main"

        elif self.menu == "Map Size":
            if instruction == "1":
                self.map_size = "small area"
            elif instruction == "2":
                self.map_size = "wide area"
            elif instruction.lower() == "e":
                self.menu = "Main"

        elif self.menu == "Weapons":
            if instruction.lower() == "e":
                self.menu = "Backpack"

        elif self.menu == "Potions":
            if instruction.lower() == "e":
                self.menu = "Backpack"

        elif self.menu == "Curiosities":
            if instruction.lower() == "e":
                self.menu = "Backpack"
