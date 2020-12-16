from Image import Image


class PlayerImages:
    def __init__(self):
        self.img_loader = Image()
        self.down_image = None
        self.up_image = None
        self.left_image = None
        self.right_image = None

    def load_default_images(self):
        self.down_image = self.img_loader.load_image("Images\\player\\sprite\\player01.png", 1)
        self.up_image = self.img_loader.load_image("Images\\player\\sprite\\player04.png", 1)
        self.left_image = self.img_loader.load_image("Images\\player\\sprite\\player02.png", 1)
        self.right_image = self.img_loader.load_image("Images\\player\\sprite\\player03.png", 1)
