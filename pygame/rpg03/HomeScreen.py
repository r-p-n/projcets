import pygame
from Constants import *


class HomeScreen:
    def __init__(self):
        self.screen = None
        self.clock = None
        self.pygame_init()
        self.button = pygame.Rect((WIDTH/2 - WIDTH/12), HEIGHT / 4, WIDTH / 6, HEIGHT / 16)

        self.start = False

    def pygame_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.screen.fill((255, 125, 125))

    def update(self):
        self.get_events()

    def draw(self):
        self.screen.fill((255, 125, 125))

        pygame.draw.rect(self.screen, (255,255,255), self.button)
        pygame.display.update()
        self.clock.tick(TIC_RATE)

    def run(self):
        self.update()
        self.draw()

    def get_events(self):
        _movement = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos):
                    self.start = True

    def kill(self):
        self.screen.fill((0, 0, 0))
        del self
