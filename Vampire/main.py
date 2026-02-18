import sys
import random as rand
import tkinter as tk
import os
from combat import Combat, Knight

# This is the user interface object. This will handle all the data that appears on the screen.
class UI:
    def __init__(self):
        self.root = tk.Tk()
        # Setting the size
        self.root.geometry("900x900")
        # Getting the icon
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "Vampire_Icon.png")

        self.icon = tk.PhotoImage(file=icon_path, master=self.root)
        self.root.iconphoto(True, self.icon)
        self.root.title("Return to Night")
        
        self.text_frame = tk.Frame(self.root)
        self.text_frame.grid(row=0, column=0)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=0)

        scrollbar = tk.Scrollbar(self.text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message = tk.Text(
            self.text_frame,
            height=15,
            width=100,
            yscrollcommand=scrollbar.set
        )
        self.message.pack(side=tk.LEFT,fill=tk.X)
        scrollbar.config(command=self.message.yview)
        # To store the last 20 
        self.buffer = []

    # This destories all buttons in the window
    def destroy_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()


    def add_to_message(self, msg):
        self.buffer.append(msg)
        if len(self.buffer) > 20:
            self.buffer.pop(0)
        
        self.message.config(state=tk.NORMAL)
        self.message.delete("1.0", tk.END)
        self.message.insert(tk.END, "\n".join(self.buffer))
        self.message.config(state=tk.DISABLED)

        # Scroll to the bottom
        self.message.see(tk.END)

        self.message.config(state=tk.DISABLED)

class Vampire:
    def __init__(self):
        self.name = "Dracula"
        self.gender = 0
        self.health = 100
        self.charisma = 2
        self.intelligence = 2
        self.looks = 2
        self.strength = 10
        self.speed = 10
        self.stealth = 3
        self.danger = 0
        self.blood = 1
        self.humanity = 10

        self.attacks = [["Bite", 20], ["Claw", 20] ]

    def displayAtack(self):
        print("Your attacks are:")
        for attack in self.attacks:
            print(attack)

class GameMaster:
    def __init__(self):
        self.vamp = Vampire()
        self.ui = UI()
        # This vairable will keep track of the choice the player made.
        self.choice = -1
    
    # This function is used when ending events. It ends the event and created any neccary changes to the player character.
    def handle_choice(self, text, effect: dict, stat_checks: dict = None, next_event=None):
        self.ui.add_to_message(text)

        for attr, delta in effect.items():
            if hasattr(self.vamp, attr):
                setattr(self.vamp, attr, getattr(self.vamp, attr) + delta)
                self.ui.add_to_message(f"{attr.capitalize()} changed by {delta}")
        
        if stat_checks:
            for attr, (threshold, func) in stat_checks.items():
                if getattr(self.vamp, attr, 0) >= threshold:
                    func() 
                    return
        
        if next_event:
            next_event()
        else:
            self.explore()

    # These are the windows that handle what actions a vampire may take 
    def VampireAttackWindow(self, attackie):
        self.ui.destroy_buttons()
        for i, attack in enumerate(self.vamp.attacks):
            tk.Button(self.ui.root, text=attack[0], command= lambda: self.attack(attack[1], attackie)).grid(row=1, column=i)

    def VampireDefendWindow():
        pass

    def VampireRunWindow():
        pass

    # This is an event where you find a deer in the forest
    def findDeer(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("You found a deer in a forest. Input 1 to eat it 0 to leave it alone.")
        
        leave_deer_alone_but = tk.Button(self.ui.root, text="Feed on deer", command=lambda: self.handle_choice("You ate the deer", {"blood":1}))
        eat_deer_but         = tk.Button(self.ui.root, text="Leave deer alone.", command=lambda: self.handle_choice("You left the deer alone", {"humanity":1}))

        leave_deer_alone_but.grid(column=0, row=1)
        eat_deer_but.grid(column=1, row=1)

    def HuntersCabin(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("You have stumbled upon a hunters cabin. There is a person inside. Do you feed.")

        but1 = tk.Button(self.ui.root, text = "Press to feed", command =lambda: self.handle_choice("You fed on the hunter.", {"blood":1}))
        but2 = tk.Button(self.ui.root, text="Leave hunter alone", command =lambda: self.handle_choice("You left the hunter alone", {"humanity": 1}))
        but1.grid(column=0, row=1)
        but2.grid(column=1, row=1)

    def OceanMermaid(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("You see a beautiful woman sitting on the beach. Do you feed.")
        self.ui.add_to_message("Press 0 to feed, 1 to leave.")

        but1 = tk.Button(self.ui.root, text = "Press to feed", command=lambda: self.handle_choice("The woman leaps into the water showing that where there should be legs there is a tail. Go away leech she yells.", {"blood":-1}))
        but2 = tk.Button(self.ui.root, text="Leave the woman alone.", command =lambda: self.handle_choice("The woman turns revealing her legs are actually a fish tail. Maybe there's some hope for you yet leech.", {"humanity": 1}))
        but1.grid(column=0, row=1)
        but2.grid(column=1, row=1)

    def knightEvent(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("You find a knight on the road. What will you do.")
        
        knight = Knight()
        combat_instance = Combat(self.vamp, self, knight)
        but1 = tk.Button(
            self.ui.root,
            text="Attack the knight.",
            command=lambda: self.handle_choice(
                "You attacked the knight",
                {},
                {"stealth": (self.vamp.stealth, lambda: combat_instance.playerTurn())}  # ✅ pass a lambda
            )
        )
        but2 = tk.Button(self.ui.root, text="Leave the knight.", command=lambda: self.handle_choice("You left the kinght alone", {"humanity": 1}))

        but1.grid(column=0, row=1)
        but2.grid(column=1, row=1)


    def FindTravelingNobel(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("You find the camp of travelling nobels What will you do.")

        but1 = tk.Button(text="Do you feed.", command=lambda: self.handle_choice("You ate the nobel." ,{"blood":1}))
        but2 = tk.Button(text="Or leave", command=lambda: self.handle_choice("You left them alone." ,{"humanity": 1}))
        
        but1.grid(column=0, row=1)
        but2.grid(column=1, row=1)
        
    # This is a village event where you break into a house and find a person inside.
    def BreakIntoHouse(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("You crawl into a window, into the bedroom of a sleep person. Do you feed?")
        self.ui.add_to_message("Press 0 to feed, 1 to leave.")
        
        but1 = tk.Button(text="Do you feed.", command=lambda: self.handle_choice("You ate the person." ,{"blood":1}))
        but2 = tk.Button(text="Or leave", command=lambda: self.handle_choice("You left them alone." ,{"humanity", 1}))
        
        but1.grid(column=0, row=1)
        but2.grid(column=1, row=1)    
        
    def FindBar(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("You hear the voices from a bar. All the sounds of laughter make you long to be human. You see a person on the side trying to stumble home. Do you feed?")
        self.ui.add_to_message("Press 0 to feed, 1 to leave.")
        
        but1 = tk.Button(text="Do you feed.", command=lambda: self.handle_choice("You ate the person." ,{"blood":1}))
        but2 = tk.Button(text="Or leave", command=lambda: self.handle_choice("You left them alone." ,{"humanity", 1}))
        
        but1.grid(column=0, row=1)
        but2.grid(column=1, row=1)


    def GetSeen(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("A person spots you in the village. She screams alerting her friends, what do you do?")

        but1 = tk.Button(text="You run away and excape the village.", command=lambda: self.handle_choice("You ate the person." ,{"blood":1}))
        but2 = tk.Button(text="You eat the person.", command=lambda: self.handle_choice("You ran away." ,{"humanity": 1}))
        
        but1.grid(column=0, row=1)
        but2.grid(column=1, row=1)


    def TravlingTroupe(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("You find a traveling troupe of actors. They are drunk and playing music by the road. Do you feed?")

        but1 = tk.Button(text="Do you feed.", command=lambda: self.handle_choice("You ate the person." ,{"blood":1}))
        but2 = tk.Button(text="Or leave", command=lambda: self.handle_choice("You ate the person." ,{"blood":1}))

        but1.grid(column=0, row=1)
        but2.grid(column=1, row=1)


        validChoice = True
        while validChoice:
            choice = int(input())
            if choice == 0:
                self.ui.add_to_message("You ate the actors. Plus 1 to blood.")
                self.vamp.blood += 1
                return
            elif choice == 1:
                self.ui.add_to_message("You left the actors alone. Plus 1 to humanity.")
                self.vamp.humanity += 1
                return
            else:
                self.ui.add_to_message("Invalid input please try again.")

    # The value of choice will be decided by the do event function.
    def doEvent(self, choice):
        # FOREST EVENTS

        event_map = {
            1: self.findDeer,
            2: self.HuntersCabin,
            3: self.OceanMermaid,
            4: self.knightEvent,
            5: self.FindTravelingNobel,
            6: self.TravlingTroupe,
            7: self.BreakIntoHouse,
            8: self.FindBar,
            9: self.GetSeen
        }
        event = event_map.get(choice)
        if event:
            event()
        else:
            self.ui.add_to_message("Invalid event choice. Please select a valid event.")
        
        return
    

        # Run into knights
    
    # Here we will give the player the choice to explore the forest or leave.
    def Forest(self):
        # We will use a random number generator to select from possible events
        num = rand.randint(1, 3)
        self.doEvent(num)

    def Road(self):
        num = rand.randint(4, 6)
        self.doEvent(num)

    def Village(self):
        num = rand.randint(7, 9)
        self.doEvent(num)

    def explore(self):
        self.ui.destroy_buttons()
        self.ui.add_to_message("Select the location you would like to explore.")
        self.ui.add_to_message("1 for forest, 2 for road, 3 for Village.")

        #knightFight(self, self.vamp)
        
        but1 = tk.Button(self.ui.root, text="Explore the forest", command=lambda: self.Forest())
        but2 = tk.Button(self.ui.root, text="Explore the Road", command=lambda: self.Road())
        but3 = tk.Button(self.ui.root, text="Explore the village", command=lambda: self.Village())

        but1.grid(row=1, column=0)
        but2.grid(row=1, column=1)
        but3.grid(row=1, column=2)


game = GameMaster()
loop = True

while loop:
    game.explore()
    game.ui.root.mainloop()

