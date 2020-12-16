from Constants import *
from PlayerImages import *
from Groups import *
import DItems
from LootContainer import LootContainer


class Player(pygame.sprite.Sprite):
    def __init__(self, spawn, vel):
        # system stuff
        group = player_sprite
        pygame.sprite.Sprite.__init__(self, group)
        self.screen = pygame.display.get_surface()
        # image stuff
        starting_direction = DOWN
        self.facing_direction = starting_direction
        player_images = PlayerImages()
        player_images.load_default_images()  # TODO change when adding more player images
        self.images = {DOWN: player_images.down_image, UP: player_images.up_image,
                       LEFT: player_images.left_image, RIGHT: player_images.right_image}
        self.image = self.images[starting_direction]
        self.rect = self.image.get_rect()
        self.rect.left = spawn[0]
        self.rect.top = spawn[1]
        # movement stuff
        pos = spawn
        self.pos = pygame.math.Vector2(pos)
        self.walls = None
        self.vel = pygame.math.Vector2(vel)
        self.offset = [0, 0]
        self.speed = 8  # TODO
        self.moving = False
        self.smooth_movement = self.set_smooth_movement()
        facing_vector = DIRECTIONS[self.facing_direction]
        self.facing_vector = pygame.math.Vector2(facing_vector[0] // STEP, facing_vector[1] // STEP)
        self.movement_input = ["still"]
        self.clear_movement_input = ["still"]
        self.move_tic = 0
        self.game_tic = 0
        self.collision = False
        # game stuff
        # TODO refactor - make a separate class.

    def draw_inventory(self):  #TODO refactor - use a get_item fuction instead, send to ui class
        pass
        # for i in range(10):
        #     for j in range(4):
        #         try:
        #             item = self.inventory.get_item((i, j))
        #             self.screen.blit(item.image, (i * STEP, j * STEP))
        #         except:
        #             pass

    def get_inventory(self):
        # use this to convert inventory strings into objects
        # have to make item/weapon class. 
        pass

    def update(self):  # TODO check if shittier render time was because of overwritten update. maybe change name of this
        movement_direction = self.movement_input[-1]
        vel = DIRECTIONS[movement_direction]
        _move = self.pos + vel
        self.get_player_image()
        self.update_rect()
        self.update_pos(_move, movement_direction)

    def draw(self):
        self.screen.blit(self.image, self.rect.move(0, -8 - STEP //2))
        self.draw_inventory()  # TODO refactor

    def draw_top_layer(self):  # TODO refactor
        pass
        # pygame.draw.rect(self.screen, (25, 25, 25), self.item_menu_rect)

    # def inventory_clicked(self, coord): # TODO refactor
    #     self.inventory_selected = coord
    #     x, y = coord

    def update_pos(self, pos, facing):
        if self.can_move(self.game_tic):
            attempt_move = tuple(pos // STEP)
            self.collision = self.walls.get(attempt_move, False)
            self.moving = self.check_moving(pos)
            self.facing_direction = facing
        if self.moving and not self.collision:  # TODO maybe clean up a bit
            if self.facing_direction == RIGHT:
                self.pos.x += self.smooth_movement[self.move_tic]
            elif self.facing_direction == LEFT:
                self.pos.x -= self.smooth_movement[self.move_tic]
            elif self.facing_direction == DOWN:
                self.pos.y += self.smooth_movement[self.move_tic]
            elif self.facing_direction == UP:
                self.pos.y -= self.smooth_movement[self.move_tic]

    def update_rect(self):
        self.rect.x = self.pos.x + self.offset[0]
        self.rect.y = self.pos.y + self.offset[1]

    def update_facing(self, facing):
        self.facing_direction = facing

    def update_move_tic(self, _):
        self.move_tic = _

    def get_game_tic(self, tic):
        self.game_tic = tic

    def get_smooth_movement(self):
        return self.smooth_movement

    def set_smooth_movement(self):
        smooth_movement = []
        leftover_movement = STEP - STEP // self.speed * self.speed

        for i in range(self.speed):
            if leftover_movement:
                smooth_movement.append(STEP // self.speed + 1)
                leftover_movement -= 1
            else:
                smooth_movement.append(STEP // self.speed)
        # shuffle the list
        for i in range(len(smooth_movement) // 2):
            if i % 2:
                a = smooth_movement[i]
                b = smooth_movement[-(i + 1)]
                smooth_movement[i] = b
                smooth_movement[-(i + 1)] = a

        return smooth_movement

    def get_player_image(self):
        if not self.facing_direction == NO_MOVEMENT:
            self.image = self.images[self.facing_direction]

    def set_player_image(self):
        pass

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def set_walls(self, walls):
        self.walls = walls

    def get_facing_tile(self):
        return self.get_stood_tile() + self.facing_vector

    def get_behind_tile(self):
        return self.get_stood_tile() - self.facing_vector

    def get_stood_tile(self):
        return self.pos // STEP

    def check_moving(self, move):
        return self.pos != move

    def is_moving(self):
        return self.moving

    def can_move(self, tic):
        return not tic % self.speed

    def reset_vel(self):
        self.vel.update(0)

    def add_movement_input(self, m_input):
        self.movement_input.append(m_input)

    def remove_movement_input(self, m_input):
        self.movement_input.remove(m_input)

