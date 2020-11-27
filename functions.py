import random, time, sys

import classes.enemyClass as enemyClass
import inventory.potions as potions

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
        equipmentDrop(player)

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

def equipmentDrop(player:object):
    _WEAPON_LOOT_TABLE = [
        {"Greatsword": ["cleave",],
         "damage": 4},
        {"Dagger": ["flurry",],
         "damage": 2},
        {"Staff": ["fireball", "cleave"],
         "damage": 1}
    ]
    _ARMOR_LOOT_TABLE = [
        {"leather": 1},
        {"chain": 2},
        {"half-plate": 3},
        {"full-plate": 4},
    ]
    _ITEM_LOOT_TABLE = [
        "potion: cure light",
    ]
    _LOOT_TABLE = [
        _WEAPON_LOOT_TABLE,
        _ARMOR_LOOT_TABLE,
        _ITEM_LOOT_TABLE,
    ]

    lootTable = random.choice(_LOOT_TABLE)
    if lootTable == _WEAPON_LOOT_TABLE:
        weaponDic = random.choice(_WEAPON_LOOT_TABLE)
        weaponName = list(weaponDic.keys())[0]
        choice = input("Equip " + str(weaponName) + "?\n>> ")
        weaponSpecial = list(weaponDic.values())[0]
        weaponDamage = list(weaponDic.values())[1]
        # Equip Weapon
        if choice.lower().startswith("y"):
            player.special = weaponSpecial
            print(player.special)
            player.damage = weaponDamage
        else:
            print("discarding " + weaponName)

    if lootTable == _ITEM_LOOT_TABLE:
        itemName = random.choice(_ITEM_LOOT_TABLE)
        # itemName = list(itemDic.keys())[0]
        choice = input("Equip " + str(itemName) + "?\n>> ")
        # Equip item
        if choice.lower().startswith("y"):
            player.inventory.append(itemName)
            print(player.inventory)
        else:
            print("discarding " + itemName)

    if lootTable == _ARMOR_LOOT_TABLE:
        armorDic = random.choice(_ARMOR_LOOT_TABLE)
        armorName = list(armorDic.keys())[0]
        armorDefense = list(armorDic.values())[0]
        choice = input("Equip " + str(armorName) + " (defense: " + str(armorDefense) + ")" + "?\n>> ")
        # Equip Armor
        if choice.lower().startswith("y"):
            player.defense = armorDefense
        else:
            print("discarding " + armorName)
