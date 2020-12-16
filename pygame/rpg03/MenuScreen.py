from Constants import *


class MenuScreen:
    def __init__(self):
        self.screen = None
        self.clock = None
        self.pygame_init()
        self.surface = pygame.Surface((WIDTH, HEIGHT))

    def pygame_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)

    def update(self):
        self.surface.set_alpha(1)
        self.get_events()

    def draw(self):
        self.surface.fill((100, 100, 100))
        self.screen.blit(self.surface, (0, 0, 0, 0))
        pygame.display.update()
        self.clock.tick(TIC_RATE)

    def run(self):
        self.update()
        self.draw()

    def get_events(self):
        for event in pygame.event.get():
            pass
