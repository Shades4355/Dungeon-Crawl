import random, time, sys

import classes.enemyClass as enemyClass

def roll(bonus:int):
    """rolls 3d6 + bonus"""
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + bonus

def playerTurn(player:object, enemiesInFight:list):
    _COMBAT_ACTIONS = ["attack", "inventory", "special", "quit"]

    MAINCOMBATDISPLAY_PIC = '''
    ########################
    #  attack  # inventory #
    # special  #   quit    #
    ########################
    '''

    print("\nPick Target:")
    for i in range(len(enemiesInFight)):
        print(str(i + 1) + ": " + enemiesInFight[i].name)

    # targeting #
    target = 0
    while target - 1 not in range(len(enemiesInFight)):
      target = input(">> ")
      try:
          target = int(target)
      except:
          target = 0

    enemy = enemiesInFight[target - 1]

    print("Enemy has {} health and {} lives".format(enemy.current_hit_points, enemy.lives))

    # action choice #
    choice = None
    while choice not in _COMBAT_ACTIONS:
        print(MAINCOMBATDISPLAY_PIC)
        choice = input(">> ").lower()

        if "inventory" in choice.lower():
            player.showInventory(playerTurn, player, enemiesInFight)
        elif "special" in choice.lower():
            player.showSpecialMoves(playerTurn, player, enemiesInFight)
        elif choice == "attack":
            attack = roll(player.attack)
            if attack > enemy.ac:
                enemy.take_damage(player.damage)
            else:
                print(player.name, "missed")
                player.xp += 1
            break
        elif choice == "quit":
            print("Goodbye")
            sys.exit()

    if not enemy.alive:
        player.xp += enemy.grantXP
        del enemiesInFight[target - 1]

def enemyTurn(player:object, enemiesInFight:list):
    """Currently, enemies roll to attack once and that's all"""
    for enemy in enemiesInFight:
        attack = roll(enemy.attack)
        if attack > player.ac:
            player.take_damage(enemy.damage)
        else:
            print(enemy.name, "missed")
    # TODO: make this more interesting?

def goblinEncounter(numOfFoes:int):
    """An encounter table for a random goblin encounter

    Includes golbins, wolves, and hobgoblins"""
    list = []
    w = 0
    h = 0
    g = 0
    for i in range(numOfFoes):
        randomNum = random.randint(1, 3)

        if randomNum == 1:
            w += 1
            list.append(enemyClass.Wolf(name = "Wolf {}".format(w)))
        elif randomNum == 2:
            g += 1
            list.append(enemyClass.Goblin(name = "Goblin {}".format(g)))
        elif randomNum == 3:
            h += 1
            list.append(enemyClass.Hobgoblin(name = "Hobgoblin {}".format(h)))
    return list

def wolfEncounter(numOfFoes:int):
    """An encounter table for a random wolf encounter

    Includes wolves, and dire wolves"""
    list = []
    w = 0
    d = 0
    for i in range(numOfFoes):
        randomNum = random.randint(1, 2)

        if randomNum == 1:
            w += 1
            list.append(enemyClass.Wolf(name = "Wolf {}".format(w)))
        elif randomNum == 2:
            d += 1
            list.append(enemyClass.DireWolf(name = "Dire Wolf {}".format(d)))
    return list

def randomEncounter(numOfFoes:int):
    randomNum = random.randint(1, 2)
    if randomNum == 1:
        return wolfEncounter(numOfFoes)
    elif randomNum == 2:
        return goblinEncounter(numOfFoes)
