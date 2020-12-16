import Tile
from Groups import wall_sprites


class Wall(Tile.Tile):
    def __init__(self, image, x, y):
        group = wall_sprites
        Tile.Tile.__init__(self, image, x, y, group)
