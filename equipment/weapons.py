

class Weapon(object):
    def __init__(self, name:str, min_damage:int=1, max_damage:int=4, special:list=["stab"]):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.special = special


class Greatsword(Weapon):
    def __init__(self, name="Greatsword"):
        super().__init__(name=name, min_damage=2, max_damage=10, special=["cleave"])


class Unarmed(Weapon):
    def __init__(self, name="Unarmed"):
        super().__init__(name=name)


class Longsword(Weapon):
    def __init__(self, name="Longsword"):
        super().__init__(name=name, max_damage=6, special=["stab"])


class Dagger(Weapon):
    def __init__(self, name="Dagger"):
        super().__init__(name=name, min_damage=2, special=["flurry"])


class Staff(Weapon):
    def __init__(self, name="Staff"):
        super().__init__(name=name, special=["fireball", "magic missile"])


class TwinSwords(Weapon):
    def __init__(self, name="Twin Swords"):
        super().__init__(name=name, min_damage=2, max_damage=6, special=["flurry"])
