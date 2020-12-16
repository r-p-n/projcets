from Constants import *
from Directions import Directions
from Fade import Fade
from Groups import *
from Image import Image
from Maps.Map1.Map01 import Map01
from MenuScreen import MenuScreen
from Player import Player
from PlayerInventory import PlayerInventory
from UI import UI
from View import View


class Game:
    def __init__(self):
        # fps stuff
        self.print_fps = True
        self.fps_max = 0
        self.fps_min = 100000
        self.avg_fps = []
        self._draw_map_grid = False

        # system stuff
        self.screen = None
        self.clock = None
        self.pygame_init()
        self.running = True
        self.game_tic = 0
        self.move_tic = 0
        pygame.event.set_blocked(None)
        pygame.event.set_allowed(
            [pygame.KEYUP, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.QUIT,
             pygame.MOUSEMOTION])
        self.image_loader = Image()
        self.paused = False
        self.paused_movement_buffer = []

        # map stuff
        self.get_current_map()

        # player stuff
        player_spawn = self.current_map.get_player_spawn_pos()
        self.can_move = False
        self.player = Player(player_spawn, ZERO_VECTOR)
        self.player.set_walls(self.current_map.get_walls())  # TODO don't like this
        self.smooth_move_list = self.player.get_smooth_movement()  # TODO change to be hooked to viewable object
        self.directions = {LEFT: False, RIGHT: False, UP: False, DOWN: False}
        self.player_inventory = PlayerInventory()

        # viewable stuff
        self.bounds = {LEFT: WIDTH // 4, RIGHT: WIDTH // 2, UP: HEIGHT // 4, DOWN: HEIGHT // 2}
        self.bounding_rect = pygame.Rect(self.bounds[LEFT], self.bounds[UP], self.bounds[RIGHT], self.bounds[DOWN])
        self.camera_object = self.create_view_object()
        self.offset_value = (0, 0)
        self.need_to_redraw = True

        # UI stuff
        self.fade = Fade()
        self.ui = UI()
        self.menu_screen = MenuScreen()
        self.menu_is_open = False
        self.need_mouse_movement = False
        self.mouse_held = False
        self.inv_pickup = None
        self.inv_drop = None

    def update(self):
        self.get_events()
        self.update_player()
        self.check_bounds()  # todo move to other method with smooth scrolling
        self.smooth_scrolling()  # TODO
        self.get_fps()
        self.ui.update()
        if self.menu_is_open:
            self.menu_screen.update()

    def draw(self):
        self.check_redraw()
        self.get_offset()
        if not self.menu_is_open:
            self.draw_map()
            self.draw_ui()
            if self._draw_map_grid:  # TODO remove after testing
                self.draw_map_grid()
            # self.fade.draw()
            self.player.draw()
        if self.menu_is_open:
            self.menu_screen.draw()

        pygame.display.update()
        self.clock.tick(TIC_RATE)
        self.game_tic += 1
        self.player.get_game_tic(self.game_tic)  # TODO do a better way of giving player game tic
        self.need_to_redraw = True  # TODO change to false after testing

    def draw_ui(self):
        self.ui.draw()
        _ = self.player_inventory.get_images_for_ui()
        if _ is not None:
            self.ui.set_inventory_images(_)

    def open_menu(self):
        self.paused_movement_buffer = self.player.movement_input
        self.paused = True
        self.menu_is_open = True

    def close_menu(self):
        self.player.movement_input = self.paused_movement_buffer
        self.paused = False
        self.menu_is_open = False

    def get_events(self):
        _movement = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop_running()
            if event.type == pygame.KEYDOWN:
                _movement = self.key_down_event(_movement, event)

            elif event.type == pygame.KEYUP:
                _movement = self.key_up_event(_movement, event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down_event(event)

            elif event.type == pygame.MOUSEBUTTONUP:

                self.mouse_button_up_event(event)

            if self.need_mouse_movement:
                if event.type == pygame.MOUSEMOTION:
                    self.mouse_motion_event(event)

    def key_down_event(self, _movement, event):
        if event.key == pygame.K_d:
            _movement = Directions.RIGHT.value
        elif event.key == pygame.K_a:
            _movement = Directions.LEFT.value
        elif event.key == pygame.K_w:
            _movement = Directions.UP.value
        elif event.key == pygame.K_s:
            _movement = Directions.DOWN.value
        if event.key == pygame.K_ESCAPE:
            if not self.menu_is_open:
                self.open_menu()
            else:
                self.close_menu()
        if event.key == pygame.K_i:
            self.ui.inventory_visible = not self.ui.inventory_visible
            self.need_mouse_movement = not self.need_mouse_movement  # TODO do this differently.
        if self.paused:
            if _movement:  # todo refactor this. it's messy and has repeating code
                if _movement not in self.paused_movement_buffer:
                    self.paused_movement_buffer.append(_movement)
            _movement = None
            self.player.movement_input = ["still"]
        if _movement:
            if _movement not in self.player.movement_input:
                self.player.add_movement_input(_movement)
        return _movement

    def key_up_event(self, _movement, event):
        if event.key == pygame.K_d:
            _movement = Directions.RIGHT.value
        elif event.key == pygame.K_a:
            _movement = Directions.LEFT.value
        elif event.key == pygame.K_w:
            _movement = Directions.UP.value
        elif event.key == pygame.K_s:
            _movement = Directions.DOWN.value
        if self.paused:
            if _movement:
                if _movement in self.paused_movement_buffer:
                    self.paused_movement_buffer.remove(_movement)
            _movement = None
        if _movement:
            if _movement in self.player.movement_input:
                self.player.remove_movement_input(_movement)
        return _movement

    def mouse_button_down_event(self, event):
        self.inv_pickup = (event.pos[0] - STEP // 2) // 32, (event.pos[1] - STEP // 2 - STEP) // 32
        inv_clicked = self.ui.ui_clicked(event.pos)
        if inv_clicked and self.inv_pickup in self.player_inventory.inventory.filled_cells:
            self.mouse_held = True
        else:
            self.inv_pickup = None

    def mouse_button_up_event(self, event):
        self.inv_drop = (event.pos[0] - STEP // 2) // 32, (event.pos[1] - STEP // 2 - STEP) // 32
        if self.inv_pickup and self.inv_drop:
            self.player_inventory.move_item(self.inv_pickup, self.inv_drop)
        self.mouse_held = False
        self.inv_pickup = None
        self.inv_drop = None

    def mouse_motion_event(self, event):
        if self.mouse_held:
            self.ui.inventory.add_image_offset(self.inv_pickup,
                                               (event.pos[0] - 16 - 16 - (self.inv_pickup[0] * 32),
                                                event.pos[1] - 32 - 16 - 16 - (self.inv_pickup[1] * 32)))
        ui_hovering = self.ui.ui_hovering(event.pos)
        if ui_hovering is not None:
            if ui_hovering[1] == "inventory":  # TODO make constant
                item = self.player_inventory.get_item(ui_hovering[0])
                if item:
                    self.ui.inventory.make_info_box(item, event.pos)
                else:
                    self.ui.inventory.reset_info_box()
        else:
            self.ui.inventory.reset_info_box()

    def pygame_init(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def update_player(self):
        self.player.set_offset(self.offset_value)
        self.player.update()

    def draw_moving_tiles(self):
        self.current_map.draw_single_tile(self.player.get_stood_tile(), self.offset_value)
        self.current_map.draw_single_tile(self.player.get_facing_tile(), self.offset_value)
        self.current_map.draw_single_tile(self.player.get_behind_tile(), self.offset_value)

    def draw_map(self):
        if self.need_to_redraw:
            self.current_map.draw(self.offset_value)
        else:
            self.draw_moving_tiles()

    def get_offset(self):
        self.offset_value = self.camera_object.get_offset()

    def check_bounds(self):
        if self.player.pos[0] + self.offset_value[0] < self.bounding_rect.left:
            self.directions[LEFT] = True
        elif self.player.pos[0] + self.offset_value[0] > self.bounding_rect.right:
            self.directions[RIGHT] = True
        if self.player.pos[1] + self.offset_value[1] < self.bounding_rect.top:
            self.directions[UP] = True
        elif self.player.pos[1] + self.offset_value[1] > self.bounding_rect.bottom:
            self.directions[DOWN] = True

    def check_redraw(self):
        if self.camera_object.check_if_offset_changed(self.offset_value):
            self.need_to_redraw = True

    def smooth_map_scrolling(self):
        if self.player.is_moving():
            if self.directions[RIGHT]:
                self.move_cycle(-self.smooth_move_list[self.move_tic], 0)
            elif self.directions[LEFT]:
                self.move_cycle(self.smooth_move_list[self.move_tic], 0)
            if self.directions[DOWN]:
                self.move_cycle(0, -self.smooth_move_list[self.move_tic])
            elif self.directions[UP]:
                self.move_cycle(0, self.smooth_move_list[self.move_tic])
            self.tic_cycle()

    def smooth_scrolling(self):
        if any(list(self.directions.values())):
            self.smooth_map_scrolling()
        else:
            self.smooth_player_scrolling()
        self.reset_directions()

    def smooth_player_scrolling(self):
        if self.player.is_moving():
            self.tic_cycle()

    def reset_directions(self):
        for key in self.directions.keys():
            self.directions[key] = False

    def tic_cycle(self):
        self.move_tic += 1

        if self.move_tic == self.player.get_speed():
            self.move_tic = 0

        self.player.update_move_tic(self.move_tic)

    def move_cycle(self, x=0, y=0):
        self.camera_object.shift(x, y)

    def get_current_map(self):
        self.current_map = Map01()  # TODO get from file

    def is_running(self):
        return self.running

    def stop_running(self):
        self.running = False

    def start_running(self):
        self.running = True

    def create_view_object(self):
        return View(self.current_map, self.player, *self.current_map.camera_pos)

    def get_fps(self):
        fps = self.clock.get_fps()
        self.avg_fps.append(fps)
        if len(self.avg_fps) > 1000:
            del (self.avg_fps[0])
        avg = sum(self.avg_fps) // (len(self.avg_fps))
        self.fps_max = max(self.fps_max, fps)
        _min = min(self.fps_min, fps)
        if _min:
            self.fps_min = _min
        if self.print_fps:
            pygame.display.set_caption(f'fps: avg={avg:.0f} current={fps:.0f} min={self.fps_min:.0f},'
                                       f' max={self.fps_max:.0f}  TIC={self.game_tic}')

    def draw_map_grid(self):
        # for testing only. delete after testing
        for i in range(WIDTH // STEP):
            pygame.draw.line(self.screen, (0, 0, 0), (i * STEP, 0), (i * STEP, HEIGHT), 1)
        for i in range(HEIGHT // STEP):
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * STEP), (WIDTH, i * STEP), 1)
