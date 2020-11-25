import random, time, sys


def playerTurn(player:object, enemiesInFight:list):
    _COMBAT_ACTIONS = {
    "inventory": player.showInventory,
    "special": player.showSpecialMoves,
    }

    MAINCOMBATDISPLAY_PIC = '''
    ########################
    #  attack  #   defend  #
    # special  # inventory #
    ########################
    '''

    print("Pick Target:")
    for i in range(len(enemiesInFight)):
        print(str(i + 1) + ": " + enemiesInFight[i].name)

    # targeting #
    target = 0
    while target - 1 not in range(len(enemiesInFight)):
      target = int(input(">> "))
      # TODO: add check to avoid crashing when a non-int is entered
    enemy = enemiesInFight[target - 1]

    print("Enemy has {} health and {} lives".format(enemy.current_hit_points, enemy.lives))

    # action choice #
    choice = None
    while choice not in _COMBAT_ACTIONS:
        print(MAINCOMBATDISPLAY_PIC)
        choice = input(">> ").lower()

        if choice in _COMBAT_ACTIONS:
            _COMBAT_ACTIONS[choice](playerTurn, player, enemiesInFight)
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

def randomEncounterChooser(_RANDOM_ENCOUNTER):
    enemyType = random.choice(list(_RANDOM_ENCOUNTER.values()))
    return enemyType
  # TODO: fix - returning copies of duplicate enemies, instead of uniques of same type
  # IE two wolfs share the same current_hit_points
