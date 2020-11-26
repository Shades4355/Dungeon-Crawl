import random, time, sys

import classes.enemyClass as enemyClass

def playerTurn(player:object, enemiesInFight:list):
    _COMBAT_ACTIONS = {
    "inventory": player.showInventory,
    "special": player.showSpecialMoves,
    }

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
      # TODO: add check to avoid crashing when a non-int is entered
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

def enemyTurn(player:object, enemiesInFight:list):
    """Currently, enemies attack once and that's all"""
    for enemy in enemiesInFight:
        player.take_damage(enemy.attack)
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
        elif randomNum == 2:
            g += 1
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
