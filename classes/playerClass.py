class PlayerClass:
  """A starting Player"""
  def __init__(self, name='Tim(?)', health=25, damage=2, defense=1, special=[], inventory=["potion: cure light", "scroll: Escape"]):
    self.name = name
    self.current_health = health
    self.max_health = health
    self.damage = damage
    self.defense = defense
    self.special = special
    self.inventory = inventory

  def showSpecialMoves(self):
    print('Special Moves', end=': ')
    print(", ".join(self.special))

  def showInventory(self):
    print("Inventory ", end=': ')
    print(", ".join(self.inventory))
    choice = None
    while not choice in (self.inventory):
        choice = input('>> ').lower()
        if choice != "back":
            # TODO: add actions
            print("stuff happens")
        elif choice == "back":
            break
