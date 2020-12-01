import random

class EnemyClass(object):
    """Generic Enemy class from which specific enemies are based"""
    def __init__(self, name='template', health=1, attack=0, defense=0, min_damage=1, max_damage=4, ac=9, lives=1, grantXP=1):
        self.name = name
        self.max_hit_points = health
        self.current_hit_points = health
        self.attack = attack
        self.defense = defense
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.ac = ac
        self.grantXP = grantXP
        self.lives = lives
        self.alive = True

    def doDamage(self):
        return random.randint(self.min_damage, self.max_damage)

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
        self.max_damage = 6
        self.grantXP = 2


class Wolf(EnemyClass):
    """A basic wolf"""
    def __init__(self, name):
        super().__init__(name=name, health=4, max_damage=4, defense=0)


class DireWolf(Wolf):
    """An advanced wolf"""
    def __init__(self, name):
        super().__init__(name=name)
        self.max_hit_points = 6
        self.current_hit_points = 6
        self.attack = 1
        self.ac = 10
        self.grantXP = 2
        self.min_damage = 2
        self.max_damage = 6
        self.grantXP = 2


class Undead(EnemyClass):
    """"A generic undead"""
    def __init__(self, name):
        super().__init__(name=name, max_damage=6, defense=2, health=6, grantXP=2)


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


# TODO: add vampires, Vampire Lords, and Thralls
class Vampire(Undead):
    """A basic vampire"""
    def __init__(self, name):
        super().__init__(name=name)
        self.max_damage = 4
        self.current_hit_points = random.randint(3, self.max_hit_points)
        self.grantXP = 3
        self.lives = 2

    def doDamage(self):
        damage = random.randint(self.min_damage, self.max_damage)

        if self.current_hit_points + damage >= self.max_hit_points:
            self. current_hit_points = self.max_hit_points
        else:
            self.current_hit_points += damage

        return damage


class VampireLord(Vampire):
    # multiple lives
    # self.grantXP = 4
    # self.min_damage = 2
    # self.max_damage = 6
    pass


class Thrall(Undead):
    # multiple lives
    def doDamage(self):
        damage = random.randint(self.min_damage, self.max_damage)

        if self.current_hit_points < self.max_hit_points:
            self. current_hit_points =+ 2

        return damage
    pass
