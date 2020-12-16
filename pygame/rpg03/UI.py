from Constants import STEP
from UIInventory import UIInventory
from UITextBox import UITextBox


class UI:
    def __init__(self):
        self.all_visible = True
        self.text_box = UITextBox()
        self.inventory = UIInventory()
        self.pos_clicked = None
        self.element = None
        self.mouse_pos = None
        self.inventory_visible = False

    def update(self):
        self.reset()

    def draw(self):
        if self.all_visible:
            if self.inventory_visible:
                self.inventory.draw()

    def hide_all_elements(self):
        self.all_visible = False

    def show_all_elements(self):
        self.all_visible = True

    def ui_clicked(self, pos):
        if pos is not None:
            if self.inventory.rect.collidepoint(pos) and self.inventory_visible:
                self.pos_clicked = self.inventory.format_position(pos)
                return self.pos_clicked[0], self.pos_clicked[1] - 1  # TODO fix. this is because the rect for the inv picture goes above where stuff is meant to be drawn

    def ui_hovering(self, pos):
        if pos is not None:
            if self.inventory.rect.collidepoint(pos):
                return self.inventory.format_position((pos[0], pos[1] - STEP)), "inventory"  # TODO fix...

    def set_inventory_images(self, images):

        self.inventory.set_item_images(images)

    def set_mouse_pos(self, pos):
        self.mouse_pos = pos

    def reset(self):
        self.pos_clicked = None
        self.element = None
