from pygame import font


class FontHandler:

    def __init__(self):
        font.init()
        self.default_font = font.SysFont("arial", 12)

        self.default_color = (255, 255, 255)
        self.special_color = (255, 125, 100)

    def get_font_object(self, string, font_type=0, color=0):
        font_color = None
        if color == 0:
            font_color = self.default_color
        elif color == 1:
            font_color = self.special_color
        if font_type == 0:
            return self.default_font.render(str(string), True, font_color)
