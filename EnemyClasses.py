class Enemy:

    def __init__(self, x, y, x_parameters, y_parameters, target):
        self.x = x
        self.y = y
        self.x_parameters = x_parameters
        self.y_parameters = y_parameters
        self.target = target

    def walk(self, hit_boxes):
        if self.x > self.target.x:
            x_distance = self.x - self.target.x
            x_direction = -1
        elif self.x < self.target.x:
            x_distance = self.target.x - self.x
            x_direction = 1
        else:
            x_distance = 0
            x_direction = 0

        if self.y > self.target.y:
            y_distance = self.y - self.target.y
            y_direction = -1
        elif self.y < self.target.y:
            y_distance = self.target.y - self.y
            y_direction = 1
        else:
            y_distance = 0
            y_direction = 0

        if x_distance < y_distance:
            if y_direction == 1:
                test_y = self.y + 1
                if test_y > self.y_parameters:
                    test_y = self.y_parameters
                if hit_boxes[self.x][test_y] is not "1" and hit_boxes[self.x][test_y] is not "0":
                    print(hit_boxes[self.x][test_y])
                    self.y = test_y
            elif y_direction == -1:
                test_y = self.y - 1
                if test_y < 0:
                    test_y = 0
                if hit_boxes[self.x][test_y] is not "1" and hit_boxes[self.x][test_y] is not "0":
                    print(hit_boxes[self.x][test_y])
                    self.y = test_y
        elif y_distance < x_distance:
            if x_direction == 1:
                test_x = self.x + 1
                if test_x > self.x_parameters:
                    test_x = self.x_parameters
                if hit_boxes[test_x][self.y] is not "1" and hit_boxes[test_x][self.y] is not "0":
                    print(hit_boxes[test_x][self.y])
                    self.x = test_x
            elif x_direction == -1:
                test_x = self.x - 1
                if test_x < 0:
                    test_x = 0
                if hit_boxes[test_x][self.y] is not "1" and hit_boxes[test_x][self.y] is not "0":
                    print(hit_boxes[test_x][self.y])
                    self.x = test_x
        else:
            if x_direction == 1:
                test_x = self.x + 1
                if test_x > self.x_parameters:
                    test_x = self.x_parameters
                if hit_boxes[test_x][self.y] is not "1" and hit_boxes[test_x][self.y] is not "0":
                    print(hit_boxes[test_x][self.y])
                    self.x = test_x
            elif x_direction == -1:
                test_x = self.x - 1
                if test_x < 0:
                    test_x = 0
                if hit_boxes[test_x][self.y] is not "1" and hit_boxes[test_x][self.y] is not "0":
                    print(hit_boxes[test_x][self.y])
                    self.x = test_x
