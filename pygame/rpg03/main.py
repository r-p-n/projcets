from Game import Game
import cProfile as profile
from HomeScreen import HomeScreen
import pygame
from Constants import WIDTH, HEIGHT, TITLE

home = HomeScreen()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    while True:
        home.run()
        if home.start:
            game = Game()
            home.kill()
            break
    while game.is_running():
        game.update()
        game.draw()


# profile.run('main()')
main()

''' pygame stuff should be initiated in one place, not multiple... 
    put something between pressing button and loading game. maybe a fade in/fade out 
'''
