from Constants import *
from FontHandler import FontHandler
from Image import Image


class UIElement:
    def __init__(self, img, rect, name, transparent=0):
        self.screen = pygame.display.get_surface()
        img_loader = Image()
        self.image = img_loader.load_image(img, transparent)
        self.rect = pygame.Rect(rect)
        self.visible = True
        self.name = name
        self.font_handler = FontHandler()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def format_position(self, pos):
        return (pos[0] - self.rect[0]) // 32, (pos[1] - self.rect[1]) // 32
