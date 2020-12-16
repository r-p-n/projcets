from DItems import *
from Image import Image
from Item import Item
from Weapon import Weapon


class LootContainer:
    def __init__(self, inv, size):
        self.img_loader = Image()
        self.seen_images = {}
        self.m_x, self.m_y = size
        self.inv = inv
        self.f_inv = {}
        self.filled_cells = set()
        self.find_filled_cells()
        self.fill_inv()

    def find_filled_cells(self):
        for y in range(self.m_y):
            for x in range(self.m_x):
                if self.inv.get((x, y), 0):
                    self.filled_cells.add((x, y))

    def add_item(self, obj_type, item_id, index, modifier_id=None):
        # TODO refactor obj_type checks, code duplication
        self.filled_cells.add(index)
        if obj_type == "w":
            stats = WEAPONS[item_id]
            path, name, description, damage, speed, attack_range, weight, value, rarity = stats
            if path not in self.seen_images:
                image = self.img_loader.load_image(path)
            else:
                image = self.seen_images[path]
            self.f_inv[index] = Weapon(image, name, description, damage, speed,
                                       attack_range, weight, value, rarity, modifier_id)

        elif obj_type == "i":
            stats = ITEMS[item_id]

            path, name, description, duration, health, max_health, damage, speed, weight, value, rarity = stats
            if path not in self.seen_images:
                image = self.img_loader.load_image(path)
            else:
                image = self.seen_images[path]  # TODO
            self.f_inv[index] = Item(image, name, description, duration, health, max_health, damage, speed, weight,
                                     value,
                                     rarity)

    def fill_inv(self):
        for index in self.filled_cells:
            obj_id = self.inv[index][0]
            obj_type = obj_id[0]
            item_id = obj_id[1:5]
            modifier_id = obj_id[5:]

            self.add_item(obj_type, item_id, index, modifier_id)

    def get_item(self, index):
        return self.f_inv[index] if index in self.filled_cells else None
