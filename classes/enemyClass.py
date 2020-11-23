class EnemyClass(object):
    def __init__(self, name='template', health=1, attack=1, defense=0, lives=1):
        self.name = name
        self.max_hit_points = health
        self.current_hit_points = health
        self.attack = attack
        self.defense = defense
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self.current_hit_points - damage
        if remaining_points >= 0 :
            self.current_hit_points = remaining_points
            print("I took {} damage, and have {} left".format(damage, self.current_hit_points))
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
    def __init__(self, name):
        super().__init__(name=name, health=4, attack=1)


class Hobgoblin(Goblin):
    def __init__(self, name):
        super().__init__(name=name)
        self.health = 6
        self.defense = 2


class Wolf(EnemyClass):
    def __init__(self, name):
        super().__init__(name=name, health=5, attack=2, defense=1)
