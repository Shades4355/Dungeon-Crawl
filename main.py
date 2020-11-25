import random, time, sys

from classes.playerClass import PlayerClass
import classes.enemyClass as enemyClass
import inventory.potions as potions
import functions as f



################
# dictionaries #
################

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
combat = True
while combat:
    name = input("Enter your name:\n>> ")
    player = PlayerClass(name=name)

    numberOfEnemyCombatants = 3 #
    enemiesInFight = []
    for i in range(numberOfEnemyCombatants):
        encounter = randomEncounterChooser(_RANDOM_ENCOUNTER)
        enemiesInFight.append(encounter)

    while player.alive and len(enemiesInFight) > 0:
        time.sleep(1)

        print("\n" + player.name + ": " + str(player.current_health) + " health" + "\n")
        time.sleep(1)

        playerTurn(player, enemiesInFight)
        enemyTurn(player, enemiesInFight)
    choice = input("Play again? (y/n)\n>> ")
    if not choice.startswith("y"):
        print('Goodbye')
        combat = False
sys.exit()
