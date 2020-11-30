import random, time, sys

import enemyClass as enemyClass
import potions as potions

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
            player.showSpecialMoves(playerTurn, player, enemy, enemiesInFight)
        elif choice == "attack":
            attack = roll(player.attack)
            if attack > enemy.ac:
                damage = player.doDamage()
                enemy.take_damage(damage)
            else:
                print(player.name, "missed")
                player.xp += 1
            break
        elif choice == "quit":
            print("Goodbye")
            print("{0.name} reached level {0.level}".format(player))
            sys.exit()

    for i in range(len(enemiesInFight) - 1, -1, -1):
        enemy = enemiesInFight[i]
        if not enemy.alive:
            player.xp += enemy.grantXP
            del enemiesInFight[i]
            equipmentDrop(player)

def enemyTurn(player:object, enemiesInFight:list):
    """Currently, enemies roll to attack once and that's all"""
    # TODO: make this more interesting?
    for enemy in enemiesInFight:
        attack = roll(enemy.attack)
        if attack > player.ac:
            damage = enemy.doDamage()
            player.take_damage(damage)
        else:
            print(enemy.name, "missed")

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

def undeadEncounter(numOfFoes:int):
    """An encounter table for a random undead encounter"""
    list = []
    z = 0
    g = 0
    s = 0
    for i in range(numOfFoes):
        randomNum = random.randint(1, 3)

        if randomNum == 1:
            z += 1
            list.append(enemyClass.Zombie(name = "Zombie {}".format(z)))
        elif randomNum == 2:
            g += 1
            list.append(enemyClass.Ghoul(name = "Ghoul {}".format(g)))
        elif randomNum == 3:
            s += 1
            list.append(enemyClass.Skeleton(name = "Skeleton {}".format(s)))

    return list

def randomEncounter(numOfFoes:int, player:object):
    if player.level <= 3:
        encounters = [goblinEncounter, wolfEncounter]
    else:
        encounters = [goblinEncounter, wolfEncounter, undeadEncounter]

    randomChoice = random.choices(encounters)[0]

    return randomChoice(numOfFoes)

def equipmentDrop(player:object):
    _WEAPON_LOOT_TABLE = [
        {"Greatsword": ["cleave",],
         "damage": 10},
        {"Longsword": ["stab"],
         "damage": 6},
        {"Dagger": ["flurry",],
         "damage": 4},
        {"Staff": ["fireball", "magic missle"],
         "damage": 4},
        {"Twin Swords": ["flurry"],
         "damage": 6}
    ]
    _ARMOR_LOOT_TABLE = [
        {"leather": 1},
        {"chain": 2},
        {"half-plate": 3},
        {"full-plate": 4},
    ]
    _ITEM_LOOT_TABLE = [
        "cure light potion",
        "cure moderate potion",
    ]
    _LOOT_TABLE = [
        _WEAPON_LOOT_TABLE,
        _ARMOR_LOOT_TABLE,
        _ITEM_LOOT_TABLE,
    ]

    lootTable = random.choices(_LOOT_TABLE, weights=(2,1,2), k=1)[0]
    if lootTable == _WEAPON_LOOT_TABLE:
        weaponDic = random.choices(_WEAPON_LOOT_TABLE, weights=(2, 3, 3, 1, 3), k=1)[0]
        weaponName = list(weaponDic.keys())[0]
        choice = input("\nEquip " + str(weaponName) + "? (y/n)\n>> ")
        weaponSpecial = list(weaponDic.values())[0]
        weaponDamage = list(weaponDic.values())[1]
        # Equip Weapon
        if choice.lower().startswith("y"):
            player.special = weaponSpecial
            print("Special: " + ", ".join(player.special))
            player.damage = weaponDamage
        else:
            print("discarding " + weaponName)

    if lootTable == _ARMOR_LOOT_TABLE:
        armorDic = random.choices(_ARMOR_LOOT_TABLE, weights=(8,4,2,1), k=1)[0]
        armorName = list(armorDic.keys())[0]
        armorDefense = list(armorDic.values())[0]
        choice = input("\nEquip " + str(armorName) +
                       " (defense: " + str(armorDefense) + ")" + "?" + "\n(current armor " + str(player.defense) + ")" + " (y/n)\n>> ")
        # Equip Armor
        if choice.lower().startswith("y"):
            player.defense = armorDefense
        else:
            print("discarding " + armorName)

    if lootTable == _ITEM_LOOT_TABLE:
        itemName = random.choices(_ITEM_LOOT_TABLE, weights=(3,1), k=1)[0]
        choice = input("\nEquip " + str(itemName) + "? (y/n)\n>> ")
        # Equip item
        if choice.lower().startswith("y"):
            player.inventory.append(itemName)
            print("Inventory: " + ", ".join(player.inventory))
        else:
            print("discarding " + itemName)
