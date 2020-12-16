import pygame
from pygame import math
from os import path

# SYSTEM SETTINGS
WIDTH = 1280
HEIGHT = 704
TIC_RATE = 128
ME_TIC_RATE = 60
STEP = 32
TILE_SHIFT = STEP/2
TITLE = "RPG03"
MAP_FORMAT = 5

# VARIABLES
DIRECTIONS = {"still": (0, 0), "up": (0, -STEP), "down": (0, STEP), "left": (-STEP, 0), "right": (STEP, 0)}
ZERO_VECTOR = math.Vector2(0, 0)
SPRITES = "Images"
UP = "up"  # TODO already have an enum with this
DOWN = "down"
LEFT = "left"
RIGHT = "right"
NO_MOVEMENT = "still"

# FONT
FONT = "arial"
FONT_SIZE = 10


#  TODO remove and add better system when more tiles are added
#  IMAGE PATHS
# image directories
FLOOR_GRASS_DIRECTORY = "Images\\floor\\grass\\"
WALL_STONE_DIRECTORY = "Images\\walls\\stone\\"


FLOOR_TILE_IMAGE_SETS = ["FNG"]
WALL_TILE_IMAGE_SETS = ["WNS"]
#  FLOOR IMAGES


# TODO automate this holy shit
FLOOR_IMAGES = {
    # GRASS NORMAL
    "FNG00": [21, None, ],  # for things like onwalk animation, tile color for minimap, etc
    "FNG01": path.join(FLOOR_GRASS_DIRECTORY, "01.png"),
    "FNG02": path.join(FLOOR_GRASS_DIRECTORY, "02.png"),
    "FNG03": path.join(FLOOR_GRASS_DIRECTORY, "03.png"),
    "FNG04": path.join(FLOOR_GRASS_DIRECTORY, "04.png"),
    "FNG05": path.join(FLOOR_GRASS_DIRECTORY, "05.png"),
    "FNG06": path.join(FLOOR_GRASS_DIRECTORY, "06.png"),
    "FNG07": path.join(FLOOR_GRASS_DIRECTORY, "07.png"),
    "FNG08": path.join(FLOOR_GRASS_DIRECTORY, "08.png"),
    "FNG09": path.join(FLOOR_GRASS_DIRECTORY, "09.png"),
    "FNG10": path.join(FLOOR_GRASS_DIRECTORY, "10.png"),
    "FNG11": path.join(FLOOR_GRASS_DIRECTORY, "11.png"),
    "FNG12": path.join(FLOOR_GRASS_DIRECTORY, "12.png"),
    "FNG13": path.join(FLOOR_GRASS_DIRECTORY, "13.png"),
    "FNG14": path.join(FLOOR_GRASS_DIRECTORY, "14.png"),
    "FNG15": path.join(FLOOR_GRASS_DIRECTORY, "15.png"),
    "FNG16": path.join(FLOOR_GRASS_DIRECTORY, "16.png"),
    "FNG17": path.join(FLOOR_GRASS_DIRECTORY, "17.png"),
    "FNG18": path.join(FLOOR_GRASS_DIRECTORY, "18.png"),
    "FNG19": path.join(FLOOR_GRASS_DIRECTORY, "19.png"),
    "FNG20": path.join(FLOOR_GRASS_DIRECTORY, "20.png"),
    "FNG21": path.join(FLOOR_GRASS_DIRECTORY, "21.png"),

}

#  WALL IMAGES
WALL_IMAGES = {
    # NORMAL STONE
    "WNS00": [9, None, ],
    "WNS01": path.join(WALL_STONE_DIRECTORY, "01.png"),
    "WNS02": path.join(WALL_STONE_DIRECTORY, "02.png"),
    "WNS03": path.join(WALL_STONE_DIRECTORY, "03.png"),
    "WNS04": path.join(WALL_STONE_DIRECTORY, "04.png"),
    "WNS05": path.join(WALL_STONE_DIRECTORY, "05.png"),
    "WNS06": path.join(WALL_STONE_DIRECTORY, "06.png"),
    "WNS07": path.join(WALL_STONE_DIRECTORY, "07.png"),
    "WNS08": path.join(WALL_STONE_DIRECTORY, "08.png"),
    "WNS09": path.join(WALL_STONE_DIRECTORY, "09.png"),

}

ALL_IMAGES = {**FLOOR_IMAGES, **WALL_IMAGES}

TEXTBOX = "Images/system/textbox1.png"
BLANK_BUTTON = "Images/system/blank.png"
CLEAR_BUTTON = "Images/system/clear.png"
FLOORS_BUTTON = "Images/system/floors.png"
ITEMS_BUTTON = "Images/system/items.png"
SAVE_BUTTON = "Images/system/save.png"
WALLS_BUTTON = "Images/system/walls.png"
INVENTORY_WINDOW = "Images/system/inventory_window_l.png"


#  UI IMAGES
INVENTORY_SCREEN = "Images/system/inventory.png"
SKILL_TREE = "Images/system/skill_tree.png"
MINIMAP = "Images/system/minimap.png"
INFO = "Images/system/info.png"
PLAYER_FRONT = "Images/system/player_front.png"
PLAYER_BACK = "Images/system/player_back.png"

STATS_BUTTON = "Images/system/stats_button.png"
SKILL_TREE_BUTTON = "Images/system/skill_tree_button.png"
INVENTORY_BUTTON = "Images/system/inventory_button.png"

UI_FRAME = "Images/system/UI_frame.png"
