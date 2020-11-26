import random, time, sys

from classes.playerClass import PlayerClass
import classes.enemyClass as enemyClass
import inventory.potions as potions
import functions as f


#############
# Main Loop #
############
name = input("Enter your name:\n>> ")
player = PlayerClass(name=name)

while player.alive:
    numberOfEnemyCombatants = random.randint(1,3)
    enemiesInFight = f.randomEncounter(numberOfEnemyCombatants)

    combat = True
    while player.alive and combat:
        time.sleep(1)

        print("\n" + player.name + ": " + str(player.current_health) + " health\nXP: " + str(player.xp))
        time.sleep(1)

        f.playerTurn(player, enemiesInFight)
        f.enemyTurn(player, enemiesInFight)
        if len(enemiesInFight) <= 0:
            combat = False
    while player.xp >= 5 + player.level:
        player.xp -= 5 + player.level
        player.advanceLevel()
        print("{0.name} reached level {0.level}".format(player))
        time.sleep(1)

    # TODO: add between combat action options
sys.exit()
