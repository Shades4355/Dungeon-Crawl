import random

import classes.playerClass as playerClass
import classes.enemyClass as enemyClass

name = input("Enter your name:\n>> ")

player = playerClass.PlayerClass(name=name)

print("name:", player.name)
print("Inventory:", player.inventory)
print("Special Moves:", player.special)
print()


#############
# Main Loop #
############

_RANDOM_ENCOUNTER = {e.name.casefold(): e for e in [
enemyClass.Goblin(name = "Goblin"),
enemyClass.Wolf(name = "Wolf"),
enemyClass.Hobgoblin(name = "Hobgoblin"),
]}

def randomEncounterChooser():
  enemyType = random.choice(list(_RANDOM_ENCOUNTER.values()))
  return enemyType


numberOfEnemyCombatants = 3 #
enemiesInFight = []
for i in range(numberOfEnemyCombatants):
  i = randomEncounterChooser()
  enemiesInFight.append(i)

for i in range(len(enemiesInFight)):
    print("enemy " + str(i + 1) + ": " + enemiesInFight[i].name + " " + "; health: " + str(enemiesInFight[i].current_hit_points))
