import random, time, sys

def roll(bonus:int):
    """rolls 3d6 + bonus"""
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + bonus

def playerTurn(player:object, enemiesInFight:list):
    _COMBAT_ACTIONS = ["attack", "inventory", "special", "quit"]

    MAINCOMBATDISPLAY_PIC = '''
    ########################
    #  attack  # inventory #
    #  special #   quit    #
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

    # Checks if enemies are dead
    for i in range(len(enemiesInFight) - 1, -1, -1):
        enemy = enemiesInFight[i]
        if not enemy.alive:
            player.xp += enemy.grantXP
            player.gold += enemy.loot
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

def equipmentDrop(player:object):
    _WEAPON_LOOT_TABLE = [
        {"Greatsword": ["cleave",],
         "min_damage":2,
         "max_damage": 10},
        {"Longsword": ["stab"],
         "min_damage":1,
         "max_damage": 6},
        {"Dagger": ["flurry",],
         "min_damage":2,
         "max_damage": 4},
        {"Staff": ["fireball", "magic missile"],
         "min_damage":1,
         "max_damage": 4},
        {"Twin Swords": ["flurry"],
         "min_damage":2,
         "max_damage": 6}
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
        "scroll of escape",
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
        weaponMinDamage = list(weaponDic.values())[1]
        weaponmaxDamage = list(weaponDic.values())[2]
        # Equip Weapon
        if choice.lower().startswith("y"):
            player.special = weaponSpecial
            print("Special: " + ", ".join(player.special))
            player.min_damage = weaponMinDamage
            player.max_damage = weaponmaxDamage
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
        itemName = random.choices(_ITEM_LOOT_TABLE, weights=(3,1,2), k=1)[0]
        choice = input("\nEquip " + str(itemName) + "? (y/n)\n>> ")
        # Equip item
        if choice.lower().startswith("y"):
            player.inventory.append(itemName)
            player.inventory.sort()
            print("Inventory: " + ", ".join(player.inventory))
        else:
            print("discarding " + itemName)
        while len(player.inventory) > 5:
            print("\nToo many items, pick one to discard:")
            print(", ".join(player.inventory))

            choice = ""
            while choice not in player.inventory:
                choice = input(">> ")
            player.inventory.remove(choice)

def cleave(player:object, enemy:object, enemiesInFight:list):
    """An attack that hits your target, and each adjacent foe"""
    if len(enemiesInFight) > 3:
        enemyIndex = enemiesInFight.index(enemy)

        # first target
        if enemyIndex - 1 >= 0:
            enemiesInFight[enemyIndex - 1].take_damage(player.doDamage())
        else:
            enemiesInFight[-1].take_damage(player.doDamage())
        # second target
        enemy.take_damage(player.doDamage())
        # third target
        if enemyIndex + 1 <= len(enemiesInFight) - 1:
            enemiesInFight[enemyIndex + 1].take_damage(player.doDamage())
        else:
            enemiesInFight[0].take_damage(player.doDamage())
    else: # if 3 or fewer foes, attack all foes
        for foe in enemiesInFight:
            foe.take_damage(player.doDamage())

def shop(player:object):
    items = [
        {"name": "cure light potion",
         "type": "item",
         "price": 1},
        {"name": "cure moderate potion",
         "type": "item",
         "price": 3},
        {"name": "scroll of escape",
         "type": "item",
         "price": 2},

        {"name": "leather",
         "type": "armor",
         "armor": 1,
         "price": 5},
        {"name": "chain",
         "type": "armor",
         "armor": 2,
         "price": 10},

        {"name": "longsword",
         "type": "weapon",
         "price": 3,
         "special": ["stab"],
         "min damage": 1,
         "max damage": 6},
         {"name": "dagger",
          "type": "weapon",
          "price": 1,
          "special": ["flurry"],
          "min damage": 2,
          "max damage": 4},
    ]

    back = {
        "name": "back",
        "type": "back",
        "price": 0
    }

    # pick items for sale
    forSaleList = random.choices(items, k=3)
    forSaleList.append(back)

    # choose an item to buy; or leave
    inShop = True
    while inShop == True:
        choice = ''
        while choice not in [i["name"] for i in forSaleList]:
            print()
            print("Player gold: " + str(player.gold))
            for item in forSaleList:
                print(item["name"] + "\n\tPrice: " + str(item["price"]))
            choice = input("What would you like to buy?\n>> ")

        index = [i["name"] for i in forSaleList].index(choice)
        choice = forSaleList[index]

        if choice["name"] == "back": # leave shop
            inShop = False
        elif player.gold >= choice["price"]:
            player.gold -= choice["price"]
            if choice["type"] == "item":
                player.inventory.append(choice["name"])
            elif choice["type"] == "armor":
                player.defense = choice["armor"]
            elif choice["type"] == "weapon":
                player.special = choice["special"],
                player.min_damage = choice["min damage"]
                player.max_damage = choice["max damage"]
            forSaleList.remove(choice)
        else:
            print("You can't afford that.\n")
            choice = ''
