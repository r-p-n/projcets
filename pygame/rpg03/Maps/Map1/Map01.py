from Constants import *
from Map import Map


class Map01(Map):
    def __init__(self):
        width = 117  # TODO
        height = 79  # TODO
        player_spawn = (10 * STEP, 10 * STEP)  # TODO - will be set by a point on the map.
        # TODO make better
        camera_pos = (0, 0)  # change to make offset
        map_file = "Maps\\Map1\\Map01"
        super().__init__(map_file, width, height, player_spawn, camera_pos)



