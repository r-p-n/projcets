from DItems import MODIFIERS


class Item:

    def __init__(self, image, name, description, duration, health, max_health, damage, speed, weight, value, rarity):
        self.type = "item" # TODO
        self.image = image
        self.name = name
        self.description = description
        self.duration = duration
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.speed = speed
        self.weight = weight
        self.value = value
        self.rarity = rarity

    def __str__(self):
        return f'a {self.name}! {self.description}!'


