import random as rand
import sys
import tkinter as tk

class Knight:
    def __init__(self):
        self.name = "default"
        self.health = 100
        self.strength = 10


class Combat:
    def __init__(self, vampire, gameMaster, enemy):
        self.vampire = vampire
        self.gameMaster = gameMaster
        self.enemy = enemy
    
    def attack(self, val, attackie):
        self.gameMaster.ui.add_to_message(f"{attackie.name} health is now {attackie.health}")
        print(f"Attacking {attackie.name} {attackie.health}")
        attackie.health -= val
        if attackie.health <= 0:
            self.gameMaster.ui.add_to_message(f"You have defeated the {attackie.name}!")
            self.vampire.health = 100
            self.gameMaster.ui.root.after(self.gameMaster.explore())
        self.enemyTurn()

    def playerTurn(self):
        self.gameMaster.ui.destroy_buttons()
        self.gameMaster.ui.add_to_message("Entering the fight.")

        for i, attack in enumerate(self.vampire.attacks):
            # Attack is a function that takes in a character then subtracts its health by a given value.
            tk.Button(self.gameMaster.ui.root, text=attack[0], command= lambda: self.attack(attack[1], self.enemy)).grid(row=1, column=i)
                # Check if knight is defeated

    def enemyAttack(self, val):
        self.gameMaster.ui.add_to_message(f"You you were hurt,  -{val} to your self")
        self.vampire.health -= val

        if self.vampire.health <= 0:
            self.gameMaster.ui.add_to_message("You were defeated.")
            return
    
    def enemyTurn(self):
        self.gameMaster.ui.add_to_message(f"The {self.enemy.name} did {self.enemy.strength} damage to you.")
        self.enemyAttack(self.enemy.strength)
        # Check if knight is defeated
        if self.vampire.health <= 0:
            self.gameMaster.ui.add_to_message(f"You have defeated the {self.enemy.name}!")
            return
        self.playerTurn()

        


