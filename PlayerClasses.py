import random

class Player:

    def __init__(self, x, y, x_parameters, y_parameters, points, character, health, curiosities, potions, weapons):
        self.x = x
        self.y = y
        self.x_parameters = x_parameters
        self.y_parameters = y_parameters
        self.points = points
        self.character = character
        self.health = health
        self.menu = "Main"
        self.hand = {"Primary": "Right Fist", "Secondary": "Left Fist"}
        self.weapons = weapons
        self.potions = potions
        self.curiosities = curiosities

    def walk(self, instruction, hit_boxes):
        if instruction == "w":
            test_x = self.x - 1
            if test_x < 0:
                test_x = 0
            if hit_boxes[test_x][self.y] is not "1":
                self.x = test_x

        if instruction == "s":
            test_x = self.x + 1
            if test_x > self.x_parameters:
                test_x = self.x_parameters
            if hit_boxes[test_x][self.y] is not "1":
                self.x = test_x

        if instruction == "a":
            test_y = self.y - 1
            if test_y < 0:
                test_y = 0
            if hit_boxes[self.x][test_y] is not "1":
                self.y = test_y

        if instruction == "d":
            test_y = self.y + 1
            if test_y > self.y_parameters:
                test_y = self.y_parameters
            if hit_boxes[self.x][test_y] is not "1":
                self.y = test_y

        if instruction == "W":
            test_x = self.x - 1
            if test_x < 0:
                test_x = 0
            if hit_boxes[test_x][self.y] is not "1":
                test_x = self.x - 2
                if test_x < 0:
                    test_x = 0
                if hit_boxes[test_x][self.y] is not "1":
                    self.x = test_x
                else:
                    self.x = test_x + 1

        if instruction == "S":
            test_x = self.x + 1
            if test_x > self.x_parameters:
                test_x = self.x_parameters
            if hit_boxes[test_x][self.y] is not "1":
                test_x = self.x + 2
                if test_x > self.x_parameters:
                    test_x = self.x_parameters
                if hit_boxes[test_x][self.y] is not "1":
                    self.x = test_x
                else:
                    self.x = test_x - 1

        if instruction == "A":
            test_y = self.y - 1
            if test_y < 0:
                test_y = 0
            if hit_boxes[self.x][test_y] is not "1":
                test_y = self.y - 2
                if test_y < 0:
                    test_y = 0
                if hit_boxes[self.x][test_y] is not "1":
                    self.y = test_y
                else:
                    self.y = test_y + 1

        if instruction == "D":
            test_y = self.y + 1
            if test_y > self.y_parameters:
                test_y = self.y_parameters
            if hit_boxes[self.x][test_y] is not "1":
                test_y = self.y + 2
                if test_y > self.y_parameters:
                    test_y = self.y_parameters
                if hit_boxes[self.x][test_y] is not "1":
                    self.y = test_y
                else:
                    self.y = test_y - 1

    def random_collect(self):
        chance = random.randint(1, 100)
        if chance < 50:
            items = ["Bracelet", "Mug", "Bone", "Glove", "Cloth", "Weave", "Ring", "Watch", "Stone", "Skull", "Doorknob", "Stick"]
            type = ["Colourful", "Beaded", "Christal Encrusted", "Jade", "Sapphire", "Golden", "Carved", "Chiseled", "Dull"]
            item = random.choice(type) + " " + random.choice(items)
            self.curiosities.append(item)
        elif chance < 75:
            items = ["Armor Potion", "Health Potion"]
            type = ["Lesser", "Greater"]
            potion = random.choice(type) + " " + random.choice(items)
            self.potions.append(potion)
        else:
            items = ["Sword", "Dagger", "Blade", "Mace", "Nunchucks", "Bat", "Club", "Bow"]
            type = ["Wooden", "Metal", "Diamond", "Sharp", "Blunt", "Broken", "Chipped", "Dented", "Godly", "Magic"]
            weapon = random.choice(type) + " " + random.choice(items)
            self.weapons.append(weapon)


