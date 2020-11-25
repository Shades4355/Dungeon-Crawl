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

  def showSpecialMoves(self, specialActions:object, enemiesInFight:list, _COMBAT_ACTIONS:object, *args):
    print('Special Moves', end=': ')
    print(self.special)

  def showInventory(self, inventoryActions:object, enemiesInFight:list, _COMBAT_ACTIONS:object, *args):
    print("Inventory ", end=': ')
    print(", ".join(self.inventory))
    choice = None
    while not choice in (self.inventory):
      choice = input('>> ').lower()
      if choice in inventoryActions:
        inventoryActions[choice]()
        combatEngine(player, enemiesInFight, _COMBAT_ACTIONS)
      elif choice == 'back':
        combatEngine(player, enemiesInFight, _COMBAT_ACTIONS)
