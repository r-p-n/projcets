import pygame

from LootContainer import LootContainer


class PlayerInventory:
    def __init__(self):
        #  TODO change to file
        self.inventory = {
            (0, 0): ["wsw01m00", 1],
            (1, 0): ["wsw02m00", 1],
            (2, 2): ["wsw01m00", 1],
            (3, 1): ["wsw02m01", 1],
            (3, 3): ["ip01", 2]
        }
        self.inventory_size = [10, 4]
        self.inventory = LootContainer(self.inventory, self.inventory_size)
        self.x = 32
        self.y = 64
        self.screen = pygame.display.get_surface()  # TODO maybe make const or something. being used too much
        self.images_to_draw = {}
        self.set_images_for_ui()
        self.changed = True

    def get_item(self, i):
        return self.inventory.get_item(i)

    def set_draw_offset(self, offset):
        self.x, self.y = offset

    def get_images_for_ui(self):
        if self.changed:
            self.set_images_for_ui()
            self.changed = False
            return self.images_to_draw
        else:
            return None

    def set_images_for_ui(self):
        self.images_to_draw = {i: [self.get_item(i).image, [0, 0]] for i in self.inventory.f_inv}

    def inventory_changed(self):
        self.changed = True

    def drop_item(self, pos):
        del self.inventory.f_inv[pos]

    def move_item(self, old_pos, new_pos):
        print(new_pos)
        # TODO probably a better way to do this
        if new_pos[0] >= self.inventory_size[0] or new_pos[1] >= self.inventory_size[1] or new_pos[0] < 0 \
                or new_pos[1] < 0:
            self.drop_item(old_pos)
            self.inventory.filled_cells.remove(old_pos)
            self.changed = True
            return 0
        if new_pos in self.inventory.f_inv:
            self.inventory.f_inv[new_pos], self.inventory.f_inv[old_pos] = self.inventory.f_inv[old_pos], \
                                                                           self.inventory.f_inv[new_pos]
        else:
            self.inventory.f_inv[new_pos] = self.inventory.f_inv[old_pos]
            del self.inventory.f_inv[old_pos]
            self.inventory.filled_cells.add(new_pos)
            self.inventory.filled_cells.remove(old_pos)
        self.changed = True
