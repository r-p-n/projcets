from UIElement import *


class UIInventory(UIElement):
    def __init__(self):
        self.x_image_offset = 0
        self.y_image_offset = STEP
        left = STEP // 2
        top = STEP // 2
        width = STEP * 10
        height = STEP * 5
        rect = pygame.Rect(left, top, width, height)
        image = INVENTORY_SCREEN
        name = "inventory"  # TODO make constant
        super().__init__(image, rect, name, 1)
        self.item_images = {}
        self.info_box = None
        self.pos = None

        self.surface1 = pygame.Surface((self.rect.width, self.rect.height - 32))
        self.surface1.fill((150, 50, 75))
        self.surface1.set_alpha(200)

    def draw(self):
        self.screen.blit(self.surface1, (16, 16 + 32))
        self.draw_icons()
        super().draw()
        self.draw_info_box()


    def set_item_images(self, dictionary):
        self.item_images = dictionary

    def draw_icons(self):
        for i in self.item_images:
            item_image = self.item_images[i]
            self.screen.blit(item_image[0], (i[0] * STEP + self.rect.x + self.x_image_offset + item_image[1][0],
                                             i[1] * STEP + self.rect.y + self.y_image_offset + item_image[1][1],
                                             STEP, STEP))

    def add_image_offset(self, index, offset):
        self.item_images[index][1] = offset

    #  TODO r-r-r-r-refactor
    def make_info_box(self, info, pos):
        self.info_box = pygame.Surface((160, 160))
        if info.type == "weapon":
            name = self.font_handler.get_font_object(f'{info.enhancement} {info.name}')
            damage = self.font_handler.get_font_object(f'Damage: {info.damage}')
            self.info_box.blit(damage, (10, 25))
            self.info_box.blit(name, (10, 0))
            self.pos = pos[0] + STEP, pos[1]
        elif info.type == "item":
            name = self.font_handler.get_font_object(f'{info.name}')
            health = self.font_handler.get_font_object(f'Health: {info.health}')
            self.info_box.blit(health, (10, 25))
            self.info_box.blit(name, (10, 0))
            self.pos = pos[0] + STEP, pos[1]

    def reset_info_box(self):
        self.info_box = None

    def draw_info_box(self):
        if self.info_box:
            self.screen.blit(self.info_box, (*self.pos, 160, 160))
