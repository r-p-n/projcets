from UIElement import *


class UITextBox(UIElement):
    def __init__(self):
        left = WIDTH/4
        top = HEIGHT - HEIGHT/6
        width = WIDTH/2
        height = HEIGHT/6
        rect = pygame.Rect(left, top, width, height)
        self.height = height
        name = "text box"
        super().__init__(TEXTBOX, rect, name)
        self.removing = False
        self.adding = False
        self.shift = [0, 0]

    def draw(self):
        if self.removing:
            self.remove()
        if self.adding:
            self.add()
        if self.shift[1] != self.height:
            self.screen.blit(self.image, self.rect.move(self.shift))

    def remove(self):
        if self.shift[1] < self.height:
            self.removing = True
            self.shift[1] += 2
        else:
            self.removing = False
            self.visible = False

    def add(self):
        if self.shift[1] > 0:
            self.adding = True
            self.shift[1] -= 2
        else:
            self.adding = False
            self.visible = True

    def raise_or_lower(self):
        if not self.visible:
            self.add()
        elif self.visible:
            self.remove()





