# from Tile import Tile
# # scrapped for now
#
# class AnimatedTile(Tile):
#     def __init__(self, images, x, y, speed):
#         self.play_once = True
#         self.stop = False
#         self.image_index = 0
#         self.index_limit = len(self.images)
#         self.timer = 0
#         self.speed = speed
#         self.images = images
#         super().__init__(self, self.images[self.image_index], x, y)
#
#     def play(self):
#         self.image = self.images[self.image_index]
#         self.timer += 1
#         if not self.timer % self.speed:
#             self.image_index += 1
#
#         if self.play_once and self.image_index == self.index_limit:
#             self.stop = True
#
#
#
