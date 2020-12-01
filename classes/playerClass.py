import random

import functions as f
from equipment import potions
from equipment import scrolls

class PlayerClass:
    """A starting Player"""
    def __init__(self, name='Tim(?)', health=25, min_damage=1, max_damage=4, defense=0, attack=0, ac=10, special=[], inventory=["cure light potion", "cure light potion"]):
        self.name = name
        self.current_health = health
        self.max_health = health
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.defense = defense
        self.attack= attack
        self.ac = ac
        self.level = 1
        self.xp = 0
        self.special = special
        self.specialCooldown = 0
        self.inventory = inventory
        self.lives = 1
        self.alive = True

    def doDamage(self):
        return random.randint(self.min_damage, self.max_damage)

    def showSpecialMoves(self, playerTurn, player:object, enemy:object, enemiesInFight:list):
        if self.specialCooldown == 0:
            print('Special Moves', end=': ')
            print(", ".join(self.special))
            choice = ''
            while choice not in self.special and choice.lower() != "back":
                choice = input(">> ")
            if choice in self.special:
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
                    enemy.take_damage(player.doDamage())
                elif choice.lower() == "magic missle":
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

        print("Inventory ", end=': ')
        print(", ".join(self.inventory))
        choice = ''
        while choice not in self.inventory and choice.lower() != "back":
            choice = input(">> ")
        if choice in self.inventory:
            if choice == "cure light potion":
                cure_light.heal(player)
            elif choice.lower() == "cure moderate potion":
                cure_moderate.heal(player)
            self.inventory.remove(choice)

        elif choice.lower() == "back":
            playerTurn(player, enemiesInFight)

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
