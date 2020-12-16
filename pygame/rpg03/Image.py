import pygame


class Image:
    def __init__(self):
        self.color_key = pygame.Color(242, 0, 255)

    def load_image(self, image, color_key=False):
        try:
            image = pygame.image.load(image)
        except FileNotFoundError:
            pass
        image = image.convert()
        if color_key:
            image.set_colorkey(self.color_key)
        return image
