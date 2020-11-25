class PlayerClass:
    """A starting Player"""
    def __init__(self, name='Tim(?)', health=25, damage=2, defense=1, special=[], inventory=["potion: Cure Light", "scroll: Escape"]):
        self.name = name
        self.current_health = health
        self.max_health = health
        self.damage = damage
        self.defense = defense
        self.special = special
        self.inventory = inventory
        self.lives = 1
        self.alive = True

    def showSpecialMoves(self, playerTurn, player, enemiesInFight):
        print('Special Moves', end=': ')
        print(", ".join(self.special))
        playerTurn(player, enemiesInFight)

    def showInventory(self, playerTurn, player, enemiesInFight):
        print("Inventory ", end=': ')
        print(", ".join(self.inventory))
        playerTurn(player, enemiesInFight)

    def take_damage(self, damage):
        postDR = damage - self.defense
        if postDR > 0:
            hurt = postDR
        else:
            hurt = 0
        remaining_points = self.current_health - hurt
        if remaining_points > 0 :
            self.current_health = remaining_points
            print("{} took {} damage, and have {} health left".format(self.name, hurt, self.current_health))
        else:
            self.lives -= 1
            if self.lives > 0:
                self.current_health = self.max_health
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.current_health = 0
                self.alive = False
