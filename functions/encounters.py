import random, time, sys

import from classes import enemyClass

def randomEncounter(numOfFoes:int, player:object):
    if player.level <= 3:
        encounters = [goblinEncounter, wolfEncounter]
    elif player.level <= 6:
        encounters = [goblinEncounter, wolfEncounter, undeadEncounter]
    else:
        encounters = [goblinEncounter, wolfEncounter, undeadEncounter, vampireEncounter]

    randomChoice = random.choices(encounters)[0]

    return randomChoice(numOfFoes)

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

def vampireEncounter(numOfFoes:int):
    """An encounter table for a random undead encounter"""
    list = []
    v = 0
    l = 0
    t = 0
    for i in range(numOfFoes):
        randomNum = random.randint(1, 3)

        if randomNum == 1:
            v += 1
            list.append(enemyClass.Vampire(name = "Vampire {}".format(v)))
        elif randomNum == 2:
            if l == 0:
                l += 1
                list.append(enemyClass.VampireLord(name = "Vampire Lord {}".format(l)))
            else:
                v += 1
                list.append(enemyClass.Vampire(name = "Vampire {}".format(v)))
        elif randomNum == 3:
            t += 1
            list.append(enemyClass.Thrall(name = "Thrall {}".format(t)))

    return list
