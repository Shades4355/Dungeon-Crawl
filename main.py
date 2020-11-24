import random, time

from classes.playerClass import PlayerClass
import classes.enemyClass as enemyClass
import parser as par

###################################
# player needs to be defined here #
###################################
name = input("Enter your name:\n>> ")

player = PlayerClass(name=name)
from inventory.potions import Potion as Potion

#############
# Functions #
#############
def parseInput():
  ret = input(">> ")
  par.Lexicon.scan(ret)

def combatEngine(player, enemy, _COMBAT_ACTIONS):
  print(MAINCOMBATDISPLAY_PIC)
  choice = input(">> ").lower()

  if choice in _COMBAT_ACTIONS:
      _COMBAT_ACTIONS[choice]()
  elif choice == "quit":
    print("Goodbye")
    sys.exit()
  else:
    print('Invalid command; please try again')

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
"attack": player.attack,
"inventory": player.showInventory,
}

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


    #################
    # Combat start #
    ################

combat = True
while combat:
    while player.current_health > 0 and [i.alive for i in enemiesInFight]:
        time.sleep(1)

        print("\n" + player.name + ": " + str(player.current_health) + "\n")
        time.sleep(1)

        print("Pick Target:")
        for i in range(len(enemiesInFight)):
            print(str(i + 1) + ": " + enemiesInFight[i].name)
        target = int(input(">> "))
        enemy = enemiesInFight[target - 1]

        combatEngine(player, enemy, _COMBAT_ACTIONS)
