from DItems import MODIFIERS


class Weapon:

    def __init__(self, image, name, description, damage, speed, attack_range, weight, value, rarity, enhancement):
        self.type = "weapon" # TODO
        self.image = image
        self.name = name
        self.description = description
        self.enchantment_description = None
        self.damage = damage
        self.speed = speed
        self.attack_range = attack_range
        self.weight = weight
        self.value = value
        self.rarity = rarity
        self.enhancement = self.get_enhancement(enhancement)


    def __str__(self):
        return f'a {self.enhancement} {self.name}! {self.description} {self.enchantment_description}!! damage: {self.damage}, speed: {self.speed},\
         range: {self.attack_range}, weight: {self.weight}, value: {self.value}, rarity: {self.rarity}'

    def get_enhancement(self, enhancement):
        e = MODIFIERS[enhancement[1:]]
        self.damage += e[1]
        self.speed += e[2]
        self.attack_range += e[3]
        self.weight += e[4]
        self.value += e[5]
        self.rarity += e[6]
        self.enchantment_description = e[7]
        return e[0]

