from Constants import *


class View:
    def __init__(self, current_map, target, x=0, y=0):
        self.x = x
        self.y = y

        self.min_x = 0  # change to make a blank offset, also need to change shit in player/map class
        self.min_y = 0

        self.max_x = -((current_map.get_width()*STEP)-WIDTH)
        self.max_y = -((current_map.get_height()*STEP)-HEIGHT)

        self.set_x()
        self.set_y()

        self.target = target

    # def update(self):
    #     self.x = int(-self.target.pos[0]) + int(WIDTH / 2)
    #     self.y = int(-self.target.pos[1]) + int(HEIGHT / 2)
    #
    #     self.set_x()
    #     self.set_y()

    def set_x(self):
        self.x = min(self.min_x, self.x)
        self.x = max(self.max_x, self.x)

    def set_y(self):
        self.y = min(self.min_y, self.y)
        self.y = max(self.max_y, self.y)

    def get_offset(self):
        return self.x, self.y

    def check_if_offset_changed(self, previous_offset):
        # return True
        return True if (self.x, self.y) != previous_offset else False

    def shift(self, x, y):
        self.x += x
        self.y += y
        self.set_x()
        self.set_y()

