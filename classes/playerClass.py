import random

from functions import functions as f
from equipment import potions
from equipment import scrolls
from equipment import weapons as w

class PlayerClass:
    """A starting Player"""
    def __init__(self, name='Tim(?)', health=25, weapon=w.Unarmed(), defense=0, attack=0, ac=10, special=["stab"], inventory=["cure light potion", "cure light potion"], gold=0):
        self.name = name
        self.current_health = health
        self.max_health = health
        self.weapon = weapon
        self.defense = defense
        self.attack= attack
        self.ac = ac
        self.level = 1
        self.xp = 0
        self.specialCooldown = 0
        self.inventory = inventory
        self.gold = gold
        self.lives = 1
        self.alive = True

    def doDamage(self):
        return random.randint(self.weapon.min_damage, self.weapon.max_damage)

    def showSpecialMoves(self, playerTurn, player:object, enemy:object, enemiesInFight:list):
        if self.specialCooldown == 0:
            print('Special Moves', end=': ')
            print(", ".join(self.weapon.special))
            choice = ''
            while choice not in self.weapon.special and choice.lower() != "back":
                choice = input(">> ")
            if choice in self.weapon.special:
                if choice.lower() == "cleave":
                    f.cleave(player, enemy, enemiesInFight)
                elif choice.lower() == "flurry":
                    enemy = random.choice(enemiesInFight)
                    enemy.take_damage(player.doDamage())
                    enemy = random.choice(enemiesInFight)
                    enemy.take_damage(player.doDamage())
                elif choice.lower() == "fireball":
                    for enemy in enemiesInFight:
                        enemy.take_damage(4)
                elif choice.lower() == "stab":
                    enemy.take_damage(player.doDamage()*2)
                elif choice.lower() == "magic missile":
                    enemy.take_damage(6)
                self.specialCooldown = 4

            elif choice.lower() == "back":
                playerTurn(player, enemiesInFight)
        else:
            print("Special on cooldown for {} more turns".format(self.specialCooldown))
            playerTurn(player, enemiesInFight)

    def showInventory(self, playerTurn, player:object, enemiesInFight:list):
        cure_light = potions.Cure_Light()
        cure_moderate = potions.Cure_Moderate()
        scroll_escape = scrolls.Escape()

        print("\nInventory ", end=': ')
        print(", ".join(self.inventory))
        choice = ''
        while choice not in self.inventory and choice.lower() != "back":
            choice = input(">> ")
        if choice in self.inventory:
            if choice == "cure light potion":
                cure_light.heal(player)
            elif choice.lower() == "cure moderate potion":
                cure_moderate.heal(player)
            elif choice.lower() == "scroll of escape":
                scroll_escape.escape(player)
            self.inventory.remove(choice)

        elif choice.lower() == "back":
            if len(enemiesInFight) > 0:
                playerTurn(player, enemiesInFight)

    def checkInventory(self):
        while len(self.inventory) > 5:
            print("\nToo many items, pick one to discard:")
            print(", ".join(self.inventory))

            choice = ""
            while choice not in self.inventory:
                choice = input(">> ")
            self.inventory.remove(choice)

    def take_damage(self, damage:int):
        postDR = damage - self.defense
        if postDR > 0:
            hurt = postDR
        else:
            hurt = 0
        remaining_points = self.current_health - hurt
        if remaining_points > 0 :
            self.current_health = remaining_points
            print("{} took {} damage, and have {} health left".format(self.name, hurt, self.current_health))
        else:
            self.lives -= 1
            if self.lives > 0:
                self.current_health = self.max_health
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead".format(self))
                self.current_health = 0
                self.alive = False

    def advanceLevel(self):
        self.level += 1
        self.max_health += 5
        self.current_health = self.max_health
        self.attack == self.level // 3
