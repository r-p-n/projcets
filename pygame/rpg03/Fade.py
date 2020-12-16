from Constants import WIDTH, HEIGHT
import pygame

''' for testing stuff '''


class Fade:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, WIDTH, HEIGHT)
        self.screen = pygame.display.get_surface()
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        self.alpha_val = 125
        self.decrease = False
        self.increase = False
        self.red = 0
        self.blue = 0
        self.green = 0
        self.surface.fill((self.red, self.green, self.blue), self.rect)

    def draw(self):
        self.surface.set_alpha(self.alpha_val)
        self.screen.blit(self.surface, self.rect)
        if self.alpha_val == 255:
            self.decrease = True
            self.increase = False
        elif self.alpha_val == 0:
            self.increase = True
            self.decrease = False
        if self.increase:
            self.increase_alpha()
        elif self.decrease:
            self.decrease_alpha()

    def increase_alpha(self):
        self.alpha_val += 1

    def decrease_alpha(self):
        self.alpha_val -= 1
