import random, time, sys, math

from classes.playerClass import PlayerClass
from classes import enemyClass
from equipment import potions
from equipment import scrolls
import functions as f


#############
# Main Loop #
############
name = input("Enter your name:\n>> ")
player = PlayerClass(name=name)

while player.alive:
    numberOfEnemyCombatants = math.ceil(player.level / 2)
    enemiesInFight = f.randomEncounter(numberOfEnemyCombatants, player)

    combat = True
    while player.alive and combat:
        time.sleep(1)

        print("\n" + player.name + ": " + str(player.current_health) + " health" + "\nlevel: " + str(player.level))
        time.sleep(1)

        f.playerTurn(player, enemiesInFight)
        if player.specialCooldown > 0:
            player.specialCooldown -= 1
        f.enemyTurn(player, enemiesInFight)
        if len(enemiesInFight) <= 0:
            combat = False
    while player.xp >= 5 + player.level and player.alive:
        player.xp -= 5 + player.level
        player.advanceLevel()
        print("{0.name} reached level {0.level}".format(player))
        time.sleep(1)

    # TODO: add between combat action options
print("{0.name} reached level {0.level}".format(player))
sys.exit()
