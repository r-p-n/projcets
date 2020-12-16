from Constants import *
from Image import *
from Floor import Floor
from Wall import Wall

import sys


class Map:
    def __init__(self, map_file, map_width, map_height, player_spawn_pos, camera_pos):
        self.player_spawn_point = player_spawn_pos
        self.map_file = map_file
        self.map_width = map_width
        self.map_height = map_height
        self.map_array = []
        self.tile_map = {}
        self.walls = {}
        self.seen_tiles = {}
        self.img_loader = Image()
        self.open_map_file()
        self.create_tile_map()
        self.camera_pos = camera_pos

    def open_map_file(self):
        with open(self.map_file, "r") as map_file:
            self.map_array = [[line[i:MAP_FORMAT + i] for i in range(0, len(line), MAP_FORMAT)]
                              for line in map_file.readlines()]

    def create_tile_map(self):
        for i, row in enumerate(self.map_array):
            row.remove("\n")
            for j, tile in enumerate(row):
                tile_type = tile[0]
                if tile not in self.seen_tiles:
                    image = self.img_loader.load_image(ALL_IMAGES[tile])
                    self.seen_tiles[tile] = image
                image = self.seen_tiles[tile]
                if tile_type == "F":  # TODO change this...
                    self.tile_map[j, i] = Floor(image, j, i)
                elif tile_type == "W":
                    self.tile_map[j, i] = Wall(image, j, i)
                    self.walls[j, i] = True

    def draw(self, offset):
        # for drawing the entire map at an offset of the screen
        for y in range(-offset[1] // STEP, int(HEIGHT / STEP) - offset[1] // STEP):
            for x in range(-offset[0] // STEP, int(WIDTH / STEP) - offset[0] // STEP):
                self.tile_map[x, y].draw(offset)

    def draw_single_tile(self, coordinates, offset):
        self.tile_map[coordinates[1], coordinates[0]].draw(offset)

    def get_tile_at_coord(self, y, x):
        return self.tile_map[x, y]

    def get_player_spawn_pos(self):
        return self.player_spawn_point

    def get_width(self):
        return self.map_width

    def get_height(self):
        return self.map_height

    def get_walls(self):
        return self.walls
