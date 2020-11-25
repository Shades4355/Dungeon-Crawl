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

  def attack(self, enemy):
    attackDamage = self.damage - enemy.defense
    if attackDamage > 0:
      enemy.health -= attackDamage
    else:
      print('Your attack fails to meaningfully injury your foe.')

  def showSpecialMoves(self):
    print('Special Moves', end=': ')
    print(self.special)

  def showInventory(self):
    print("Inventory ", end=': ')
    print(self.inventory)
    choice = ''
    while not choice in (self.inventory or _COMBAT_ACTIONS):
      choice = input('>> ').lower()
      if choice in _COMBAT_ACTIONS:
        _COMBAT_ACTIONS[choice]()
        combatEngine(player, enemy, _COMBAT_ACTIONS)
      elif choice == 'back':
        combatEngine(player, enemy, _COMBAT_ACTIONS)
