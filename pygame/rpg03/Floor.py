import Tile
from Groups import floor_sprites


class Floor(Tile.Tile):
    def __init__(self, image, x, y):
        group = floor_sprites
        Tile.Tile.__init__(self, image, x, y, group)
