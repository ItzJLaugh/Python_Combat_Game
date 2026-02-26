import pandas as pd
import numpy as py
import random

# decision rpg game for first project
# - Character & Enemy is given name, level
# - Character & enermy can punch, kick, heal, or power move (every 5 moves)

# define actor health
character_health = 100
enemy_health = 100

turn = 0
last_kick = -2
last_heal = -2
last_powermove = -5

# create character class with various methods (actions users can take)
class character:
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 100
        
class enemy():
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        
player = character("Hero", 1)
enemy = enemy("Goblin")
    
# prompt user to provide input of what option they choose
while player.health > 0 and enemy.health > 0:
    turn += 1
    option = input("choose action (punch, kick, heal, powermove):  ")

    if option == "punch":
        enemy.health -= 10
   
    if option == "kick":
        if turn - last_kick < 2:
            print ("Kick is on cooldown")
        else:
            enemy.health -= 18
            last_kick = turn
        
    if option == "heal":
        if turn - last_heal < 2:
            print ("Heal is on cooldown")
        else:
            player.health += 10
            last_heal = turn
    
    if option == "powermove":
        if turn - last_powermove < 5:
            print ("POWERMOVE is on cooldown")
        else:
            enemy.health -= 30
            last_powermove = turn
        
    enemy_action = random.choice(["punch","kick","heal","powermove"])

    if enemy_action == "punch":
        player.health -= 10
        print ("enemy does punch")
        print (f"your health: {player.health}")
        print(f"Enemy health: {enemy.health}")
    
    if enemy_action == "kick":
        player.health -= 18
        print ("enemy does kick")
        print (f"your health: {player.health}")
        print(f"Enemy health: {enemy.health}")
    
    if enemy_action == "heal":
        enemy.health += 10
        print ("enemy heals")
        print (f"your health: {player.health}")
        print(f"Enemy health: {enemy.health}")

    if enemy_action == "powermove":
        player.health -= 30
        print ("enemy does POWERMOVE")
        print (f"your health: {player.health}")
        print(f"Enemy health: {enemy.health}")




    



    

    

    

    
    



    
    
    

        
