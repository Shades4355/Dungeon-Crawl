class Potion(object):
    """Simple healing potion class"""
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def heal():
        player.current_health += self.number
        if player.current_health > player.max_health:
          player.current_health = player.max_health

class Cure_Light(Potion):
    """The weakest of healing potions"""
    def __init__(self, name="Cure Light"):
        super().__init__(name=name, number=5)
