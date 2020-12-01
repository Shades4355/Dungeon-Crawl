import random

class EnemyClass(object):
    """Generic Enemy class from which specific enemies are based"""
    def __init__(self, name='template', health=1, attack=0, defense=0, damage=4, ac=9, lives=1, grantXP=1):
        self.name = name
        self.max_hit_points = health
        self.current_hit_points = health
        self.attack = attack
        self.defense = defense
        self.damage = damage
        self.ac = ac
        self.grantXP = grantXP
        self.lives = lives
        self.alive = True

    def doDamage(self):
        return random.randint(1, self.damage)

    def take_damage(self, damage:int):
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
        super().__init__(name=name, health=4)


class Hobgoblin(Goblin):
    """A leader among Goblins"""
    def __init__(self, name):
        super().__init__(name=name)
        self.max_hit_points = 6
        self.current_hit_points = 6
        self.defense = 1
        self.grantXP = 2
        self.damage = 6


class Wolf(EnemyClass):
    """A basic wolf"""
    def __init__(self, name):
        super().__init__(name=name, health=4, damage=2, defense=0)


class DireWolf(Wolf):
    """An advanced wolf"""
    def __init__(self, name):
        super().__init__(name=name)
        self.max_hit_points = 6
        self.current_hit_points = 6
        self.attack = 1
        self.ac = 10
        self.grantXP = 2
        self.damage = 6


class Undead(EnemyClass):
    """"A generic undead"""
    def __init__(self, name):
        super().__init__(name=name, damage=6, defense=2, health=6)


class Zombie(Undead):
    """A weak but hard to kill Zombie"""
    def __init__(self, name):
        super().__init__(name=name)
        self.defense = 3
        self.max_hit_points = 1
        self.current_hit_points = 1


class Ghoul(Undead):
    """A corse eating ghoul"""
    def __init__(self, name):
        super().__init__(name=name)
        self.current_health = random.randint(3, self.max_hit_points)


class Skeleton(Undead):
    """A basic Skeleton"""
    def __init__(self, name):
        super().__init__(name=name)
        self.current_hit_points = random.randint(1, self.max_hit_points)
