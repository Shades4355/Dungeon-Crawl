class Potion(object):
    """Simple healing potion class"""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def heal(self, player:object):
        print("{0.name} healed for {1}".format(player, self.number))
        player.current_health += self.number
        if player.current_health > player.max_health:
          player.current_health = player.max_health

class Cure_Light(Potion):
    """The weakest of healing potions"""
    def __init__(self, name="Cure Light"):
        super().__init__(name=name, number=5)
