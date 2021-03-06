import random, time, sys, math

from classes.playerClass import PlayerClass
from classes import enemyClass
from functions import functions as f
from functions import encounters as enc


#############
# Main Loop #
############
name = input("Enter your name:\n>> ")
player = PlayerClass(name=name)

while player.alive:
    numberOfEnemyCombatants = math.ceil(player.level / 2)
    enemiesInFight = enc.randomEncounter(numberOfEnemyCombatants, player)

    player.inCombat = True
    while player.alive and player.inCombat:
        time.sleep(1)

        print("\n" + player.name + ": " + str(player.current_health) + " health" + "\nlevel: " + str(player.level))
        time.sleep(1)

        f.playerTurn(player, enemiesInFight)
        if player.specialCooldown > 0:
            player.specialCooldown -= 1
        print()
        f.enemyTurn(player, enemiesInFight)
        if len(enemiesInFight) <= 0:
            player.inCombat = False
    while player.xp >= 5 + player.level and player.alive:
        player.xp -= 5 + player.level
        player.advanceLevel()
        print("{0.name} reached level {0.level}".format(player))
        time.sleep(1)
    player.specialCooldown = 0
    f.shop(player)
    print("\nUse an item before the next fight? ('back' to escape)")
    player.showInventory(f.playerTurn, player, enemiesInFight)
print("{0.name} reached level {0.level}".format(player))
input("[enter] to exit program")
sys.exit()
