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
name = input("Enter your name:\n>> ")
player = PlayerClass(name=name)

while player.alive:
    numberOfEnemyCombatants = random.randint(1,3)
    enemiesInFight = []
    for i in range(numberOfEnemyCombatants):
        encounter = f.randomEncounterChooser(_RANDOM_ENCOUNTER)
        enemiesInFight.append(encounter)

    combat = True
    while combat:
        time.sleep(1)

        print("\n" + player.name + ": " + str(player.current_health) + " health")
        time.sleep(1)

        f.playerTurn(player, enemiesInFight)
        f.enemyTurn(player, enemiesInFight)
        if len(enemiesInFight) <= 0:
            combat = False
    # TODO: add between combat action options
sys.exit()
