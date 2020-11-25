class EnemyClass(object):
    """Generic Enemy class from which specific enemies are based"""
    def __init__(self, name='template', health=1, attack=1, defense=0, lives=1):
        self.name = name
        self.max_hit_points = health
        self.current_hit_points = health
        self.attack = attack
        self.defense = defense
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        postDR = damage - self.defense
        if postDR > 0:
            hurt = postDR
        else:
            hurt = 0
        remaining_points = self.current_hit_points - hurt
        if remaining_points > 0 :
            self.current_hit_points = remaining_points
            print("{} took {} damage, and have {} left".format(self.name, hurt, self.current_hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                self.current_hit_points = self.max_hit_points
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.current_hit_points = 0
                self.alive = False



class Goblin(EnemyClass):
    """A lowly Goblin"""
    def __init__(self, name):
        super().__init__(name=name, health=4, attack=1)


class Hobgoblin(Goblin):
    """A leader among Goblins"""
    def __init__(self, name):
        super().__init__(name=name)
        self.health = 6
        self.defense = 1


class Wolf(EnemyClass):
    """A basic wolf"""
    def __init__(self, name):
        super().__init__(name=name, health=3, attack=2, defense=1)
