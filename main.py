import random, time, sys

from classes.playerClass import PlayerClass
import classes.enemyClass as enemyClass
import inventory.potions as potions

###################################
# player needs to be defined here #
###################################
name = input("Enter your name:\n>> ")

player = PlayerClass(name=name)
from inventory.potions import Potion as Potion

#############
# Functions #
#############
def combatEngine(player, enemiesInFight, _COMBAT_ACTIONS):
    print("Pick Target:")
    for i in range(len(enemiesInFight)):
        print(str(i + 1) + ": " + enemiesInFight[i].name)

    # targeting #
    target = 0
    while target - 1 not in range(len(enemiesInFight)):
      target = int(input(">> "))
    enemy = enemiesInFight[target - 1]

    print("Enemy has {} health and {} lives".format(enemy.current_hit_points, enemy.lives))

    # action choice #
    choice = None
    while choice not in _COMBAT_ACTIONS:
        print(MAINCOMBATDISPLAY_PIC)
        choice = input(">> ").lower()

        if choice in _COMBAT_ACTIONS:
            _COMBAT_ACTIONS[choice](enemiesInFight=enemiesInFight, _COMBAT_ACTIONS=_COMBAT_ACTIONS, specialActions=specialActions, inventoryActions=inventoryActions)
        elif choice == "attack":
            enemy.take_damage(player.damage)
            break
        elif choice == "quit":
            print("Goodbye")
            sys.exit()
        else:
            print('Invalid command; please try again')
            time.sleep(1)

    if not enemy.alive:
        del enemiesInFight[target - 1]

################
# dictionaries #
################
MAINCOMBATDISPLAY_PIC = '''
########################
#  attack  #   defend  #
# special  # inventory #
########################
'''

_COMBAT_ACTIONS = {
"inventory": player.showInventory,
"special": player.showSpecialMoves,
}

inventoryActions = {
"potion: cure light": potions.Cure_Light.heal,
}

_RANDOM_ENCOUNTER = {e.name.casefold(): e for e in [
enemyClass.Goblin(name = "Goblin"),
enemyClass.Wolf(name = "Wolf"),
enemyClass.Hobgoblin(name = "Hobgoblin"),
]}


#############
# Main Loop #
############

def randomEncounterChooser():
  enemyType = random.choice(list(_RANDOM_ENCOUNTER.values()))
  return enemyType
  # TODO: fix - returning copies of duplicate enemies, instead of uniques of same type
  # IE two wolfs share the same current_hit_points


numberOfEnemyCombatants = 3 #
enemiesInFight = []
for i in range(numberOfEnemyCombatants):
  i = randomEncounterChooser()
  enemiesInFight.append(i)


    #################
    # Combat start #
    ################

combat = True
while combat:
    while player.current_health > 0 and enemiesInFight:
        time.sleep(1)

        print("\n" + player.name + ": " + str(player.current_health) + "\n")
        time.sleep(1)

        combatEngine(player, enemiesInFight, _COMBAT_ACTIONS)
