class Potion(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def heal():
        player.current_health += self.number
        if player.current_health > player.max_health:
          player.current_health = player.max_health
