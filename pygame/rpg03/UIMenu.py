# from UIElement import *
# import Constants
# from Image import Image
#
#
# class UIMenu(UIElement):
#     def __init__(self):
#         img_loader = Image()
#         left = 0
#         top = HEIGHT - 32
#         width = 320
#         height = 32
#         rect = pygame.Rect(left, top, width, height)
#         inv_img = img_loader.load_image(INVENTORY_BUTTON)
#         stats_img = img_loader.load_image(STATS_BUTTON)
#         skill_tree_img = img_loader.load_image(SKILL_TREE_BUTTON)
#         blank_button = img_loader.load_image(BLANK_BUTTON)
#
#         surf = pygame.Surface((320, 32))
#         surf.blit(inv_img, (0, 0, 32, 32))
#         surf.blit(stats_img, (32, 0, 32, 32))
#         surf.blit(skill_tree_img, (64, 0, 32, 32))
#         surf.blit(blank_button, (96, 0, 32, 32))
#         surf.blit(blank_button, (128, 0, 32, 32))
#         surf.blit(blank_button, (160, 0, 32, 32))
#         surf.blit(blank_button, (192, 0, 32, 32))
#         surf.blit(blank_button, (224, 0, 32, 32))
#         surf.blit(blank_button, (256, 0, 32, 32))
#         surf.blit(blank_button, (288, 0, 32, 32))
#         super().__init__(surf, rect)
