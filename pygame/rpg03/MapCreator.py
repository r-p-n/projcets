import sys

import pygame

from Constants import *
from Floor import Floor
from Image import Image
from Wall import Wall


class MapCreator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.key.set_repeat(1, 10)
        self.clock = pygame.time.Clock()

        self.boarder_size = STEP * 10
        self.map_size_x = -(117 * STEP - WIDTH)  # TODO
        self.map_size_y = -(79 * STEP - HEIGHT)  # TODO

        self.map_file = "Maps\\Map1\\Map01"  # TODO
        self.map_array = []
        self.tile_map = {}
        self.seen_tiles = {}
        self.img_loader = Image()
        self.offset = [self.boarder_size, self.boarder_size]
        self.is_running = True
        self.open_map_file()
        self.create_tile_map()

        self.tile_view = pygame.Rect(self.boarder_size, 0, WIDTH - self.boarder_size, self.boarder_size)
        self.menu_select = pygame.Rect(0, 0, self.boarder_size, STEP)
        self.tile_group_select = pygame.Rect(0, STEP, self.boarder_size, HEIGHT - STEP)
        self.map_view = pygame.Rect(self.boarder_size, self.boarder_size, WIDTH, HEIGHT)

        self.boarder_color = (255, 125, 125)  # TODO

        self.selected_map_tile = None
        self.selected_draw_tile = None
        self.selected_tile_type = None
        self.selected_menu_item = None

        self.blank = self.img_loader.load_image(BLANK_BUTTON)
        self.clear = self.img_loader.load_image(CLEAR_BUTTON)
        self.floors = self.img_loader.load_image(FLOORS_BUTTON)
        self.items = self.img_loader.load_image(ITEMS_BUTTON)
        self.save = self.img_loader.load_image(SAVE_BUTTON)
        self.walls = self.img_loader.load_image(WALLS_BUTTON)

        self.system_buttons = [[self.clear, "clear"],
                               [self.floors, "floors"],
                               [self.walls, "walls"],
                               [self.items, "items"],
                               [self.blank, "blank"],
                               [self.blank, "blank"],
                               [self.blank, "blank"],
                               [self.blank, "blank"],
                               [self.blank, "blank"],
                               [self.save, "save"],
                               ]

        self.wall_images = {}
        self.floor_images = {}
        self.create_wall_buttons()
        self.create_floor_buttons()
        self.tile_group_button_clicked = None
        self.selected_tile = None
        self.selected_tile_set = None
        self.selected_new_tile = None
        self.selected_map_tile_up = None

        self.select_line_coord = None

    def update(self):
        self.get_events()
        self.get_selected_tile_name()
        self.replace_tile()
        self.bound_offset()

    def draw(self):
        self.draw_map()
        self.draw_rects()
        self.draw_lines()
        self.draw_system_buttons()
        if self.selected_menu_item == "walls":
            self.draw_wall_buttons()
        elif self.selected_menu_item == "floors":
            self.draw_floor_buttons()
        self.draw_chosen_tile_set()
        self.draw_map_grid()
        self.draw_selection_box()
        pygame.display.update()
        self.clock.tick(TIC_RATE)

    def get_events(self):
        _movement = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.offset[0] -= STEP
                elif event.key == pygame.K_a:
                    self.offset[0] += STEP
                elif event.key == pygame.K_w:
                    self.offset[1] += STEP
                elif event.key == pygame.K_s:
                    self.offset[1] -= STEP

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected_map_tile_up = None
                if self.map_view.collidepoint(event.pos):
                    self.selected_map_tile = [(event.pos[0] - self.offset[0]) // STEP,
                                              (event.pos[1] - self.offset[1]) // STEP]

                if self.menu_select.collidepoint(event.pos):
                    _n = event.pos[0] // STEP
                    self.selected_menu_item = self.system_buttons[_n][1]

                elif self.tile_view.collidepoint(event.pos):
                    _pos = (event.pos[0] - self.tile_view.x) // STEP, (event.pos[1] - self.tile_view.y) // STEP
                    if _pos[1]:
                        self.selected_tile = _pos[0] + _pos[1] * 38
                    else:
                        self.selected_tile = _pos[0]

                elif self.tile_group_select.collidepoint(event.pos):
                    _pos = (event.pos[0] - self.tile_group_select.x) // STEP, \
                           (event.pos[1] - self.tile_group_select.y) // STEP
                    if _pos[1]:
                        self.tile_group_button_clicked = f'{_pos[1]}{_pos[0]}'
                    else:
                        self.tile_group_button_clicked = _pos[0]

            if event.type == pygame.MOUSEBUTTONUP:
                if self.map_view.collidepoint(event.pos):
                    self.selected_map_tile_up = [(event.pos[0] - self.offset[0]) // STEP,
                                                 (event.pos[1] - self.offset[1]) // STEP]
            if event.type == pygame.MOUSEMOTION:
                if self.selected_map_tile:
                    self.select_line_coord = event.pos

    def draw_chosen_tile_set(self):
        try:
            if self.selected_menu_item == "walls":
                self.draw_walls()

            elif self.selected_menu_item == "floors":
                self.draw_floors()
            elif self.selected_menu_item == "items":
                pass
            elif self.selected_menu_item == "save":
                self.save_map()
                self.selected_menu_item = "blank"
        except TypeError:
            pass
        except IndexError:
            pass

    def draw_map(self):
        try:
            for y in range(-self.offset[1] // STEP + 10, int(HEIGHT / STEP) - self.offset[1] // STEP):
                for x in range(-self.offset[0] // STEP + 10, int(WIDTH / STEP) - self.offset[0] // STEP):
                    self.tile_map[x, y].draw(self.offset)
        except KeyError:
            pass

    def draw_floors(self):
        tile_set = FLOOR_TILE_IMAGE_SETS[self.tile_group_button_clicked]
        for i in range(FLOOR_IMAGES[f'{tile_set}00'][0]):
            if i < 9:
                img_path = FLOOR_IMAGES[f'{tile_set}0{i + 1}']
            else:
                img_path = FLOOR_IMAGES[f'{tile_set}{i + 1}']
            img = self.img_loader.load_image(img_path)
            self.screen.blit(img, (320 + 32 * i, 0))
            self.selected_tile_set = tile_set

    def draw_walls(self):
        tile_set = WALL_TILE_IMAGE_SETS[self.tile_group_button_clicked]
        for i in range(WALL_IMAGES[f'{tile_set}00'][0]):
            img_path = WALL_IMAGES[f'{tile_set}0{i + 1}']
            img = self.img_loader.load_image(img_path)
            self.screen.blit(img, (320 + 32 * i, 0))
            self.selected_tile_set = tile_set

    def draw_rects(self):
        self.screen.fill((100, 0, 0), self.tile_view)
        self.screen.fill((0, 100, 0), self.menu_select)
        self.screen.fill((0, 0, 100), self.tile_group_select)

    def draw_floor_buttons(self):
        for j, i in enumerate(FLOOR_TILE_IMAGE_SETS):
            image = self.floor_images[f'{i}01']
            self.screen.blit(image, (j * STEP, STEP))

    def draw_wall_buttons(self):
        for j, i in enumerate(WALL_TILE_IMAGE_SETS):
            image = self.wall_images[f'{i}01']
            self.screen.blit(image, (j * STEP, STEP))

    def draw_selection_box(self):
        if self.selected_map_tile and self.select_line_coord:
            pygame.draw.line(self.screen, (255, 255, 255), (self.selected_map_tile[0] * STEP + self.offset[0],
                                                            self.selected_map_tile[1] * STEP + self.offset[1]),
                             (self.selected_map_tile[0] * STEP + self.offset[0], self.select_line_coord[1]), 5)

            pygame.draw.line(self.screen, (255, 255, 255),
                             (self.selected_map_tile[0] * STEP + self.offset[0],
                              self.selected_map_tile[1] * STEP + self.offset[1]),
                             (self.select_line_coord[0], self.selected_map_tile[1] * STEP + self.offset[1]), 5)

            pygame.draw.line(self.screen, (255, 255, 255),
                             (self.selected_map_tile[0] * STEP + self.offset[0], self.select_line_coord[1]),
                             self.select_line_coord, 5)

            pygame.draw.line(self.screen, (255, 255, 255),
                             (self.select_line_coord[0], self.selected_map_tile[1] * STEP + self.offset[1]),
                             self.select_line_coord, 5)

    def draw_lines(self):
        pygame.draw.line(self.screen, self.boarder_color, (0, 0), (0, HEIGHT), 1)
        pygame.draw.line(self.screen, self.boarder_color, (0, 0), (WIDTH, 0), 5)
        pygame.draw.line(self.screen, self.boarder_color, (self.boarder_size, 0), (self.boarder_size, HEIGHT), 1)
        pygame.draw.line(self.screen, self.boarder_color, (0, HEIGHT), (self.boarder_size, HEIGHT), 5)
        pygame.draw.line(self.screen, self.boarder_color, (0, STEP), (self.boarder_size, STEP), 1)
        pygame.draw.line(self.screen, self.boarder_color, (self.boarder_size, self.boarder_size),
                         (WIDTH, self.boarder_size), 1)
        pygame.draw.line(self.screen, self.boarder_color, (WIDTH, 0), (WIDTH, self.boarder_size), 5)

    def draw_map_grid(self):
        for i in range(WIDTH // STEP):
            pygame.draw.line(self.screen, (0, 0, 0), (i * STEP, 0), (i * STEP, HEIGHT), 1)
        for i in range(HEIGHT // STEP):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * STEP), (WIDTH, i * STEP), 1)

    def draw_system_buttons(self):
        for i in range(10):
            self.screen.blit(self.system_buttons[i][0], self.menu_select.move((STEP * i, 0)))

    def create_tile_map(self):
        for i, row in enumerate(self.map_array):
            row.remove("\n")
            for j, tile in enumerate(row):
                tile_type = tile[0]
                if tile not in self.seen_tiles:
                    image = self.img_loader.load_image(ALL_IMAGES[tile])
                    self.seen_tiles[tile] = image
                image = self.seen_tiles[tile]
                if tile_type == "F":
                    self.tile_map[j, i] = Floor(image, j, i)
                elif tile_type == "W":
                    self.tile_map[j, i] = Wall(image, j, i)

    def create_wall_buttons(self):
        for i in WALL_TILE_IMAGE_SETS:
            button_image_name = f'{i}01'
            button_image = self.img_loader.load_image(WALL_IMAGES[button_image_name])
            self.wall_images[f'{i}01'] = button_image

    def create_floor_buttons(self):
        for i in FLOOR_TILE_IMAGE_SETS:
            button_image_name = f'{i}01'
            button_image = self.img_loader.load_image(FLOOR_IMAGES[button_image_name])
            self.floor_images[f'{i}01'] = button_image

    def open_map_file(self):
        with open(self.map_file, "r") as map_file:
            self.map_array = [[line[i:MAP_FORMAT + i] for i in range(0, len(line), MAP_FORMAT)]
                              for line in map_file.readlines()]

    def get_selected_tile_name(self):
        try:
            if self.selected_tile + 1 < 10:
                self.selected_new_tile = f'{self.selected_tile_set}0{self.selected_tile + 1}'
            else:
                self.selected_new_tile = f'{self.selected_tile_set}{self.selected_tile + 1}'
        except:
            pass

    def replace_tile(self):
        _ = self.selected_map_tile
        _u = self.selected_map_tile_up
        if self.selected_new_tile:
            try:
                if self.selected_new_tile not in self.seen_tiles:

                    image = self.img_loader.load_image(ALL_IMAGES[self.selected_new_tile])
                    self.seen_tiles[self.selected_new_tile] = image
            except KeyError:
                pass
        if _ == _u and _:
            try:
                if self.selected_new_tile and self.selected_map_tile:
                    self.tile_map[_[0], _[1]] = Wall(self.seen_tiles[self.selected_new_tile],
                                                     _[0], _[1])
                    self.map_array[_[1]][_[0]] = self.selected_new_tile
                self.selected_map_tile = None
            except KeyError:
                pass
        elif _ != _u and _u and _:
            try:
                for i in range(min(_[0], _u[0]), max(_[0], _u[0]) + 1):
                    for j in range(min(_[1], _u[1]), max(_[1], _u[1]) + 1):
                        if self.selected_new_tile and self.selected_map_tile:
                            self.tile_map[i, j] = Wall(self.seen_tiles[self.selected_new_tile],
                                                       i, j)
                            self.map_array[j][i] = self.selected_new_tile
                self.selected_map_tile = None
                self.selected_map_tile_up = None
            except KeyError:
                pass
            except TypeError:
                pass

    def bound_offset(self):
        self.offset[1] = min(self.boarder_size, self.offset[1])
        self.offset[1] = max(self.map_size_y, self.offset[1])

        self.offset[0] = min(self.boarder_size, self.offset[0])
        self.offset[0] = max(self.map_size_x, self.offset[0])

    def save_map(self):
        print("SAVING MAP...")
        with open(self.map_file, "w") as map_file:
            for i in self.map_array:
                for j in i:
                    map_file.write(str(j))
                map_file.write("\n")
        print("SAVED")


mp = MapCreator()


def main():
    while mp.is_running:
        mp.update()
        mp.draw()


main()
