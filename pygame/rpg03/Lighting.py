# from Constants import *
# import pygame
# from random import randint
#
#
# class Lighting:
#     def __init__(self):
#         self.tiles = {}
#
#         self.screen = pygame.display.get_surface()
#         for y in range(HEIGHT//32):
#             for x in range(WIDTH//32):
#                 _ = pygame.Surface((STEP, STEP))
#                 alphaval = randint(0, 255)
#                 _.set_alpha(alphaval)
#                 _.fill((0, 0, 0 ))
#                 self.tiles[x, y] = _
#
#     def draw(self):
#         for y in range(HEIGHT//32):
#             for x in range(WIDTH//32):
#                 self.screen.blit(self.tiles[x, y], (x * 32, y * 32, 32, 32))




''' use this shit to make variable lighting based on player pos or something to have a light  effect. then make 4 rects, filled black to cover the rest of the screen.'''
