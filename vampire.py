import tkinter as tk


class Window:
    def __init__(self, root, game_master):
        self.root = root
        self.game_master = game_master
        self.location = "Home"
        self.label = tk.Label(self.root, text=self.location)
        self.but1 = tk.Button(self.root, text="Go to Forest", command=lambda: self.game_master.change_location("forest"))
        self.but2 = tk.Button(self.root, text="Go to road", command=lambda: self.game_master.change_location("road"))
        self.but3 = tk.Button(self.root, text="Go to village", command=lambda: self.game_master.change_location("village"))

        self.label.grid(row=0, column=1)
        self.but1.grid(row=1, column=0)
        self.but2.grid(row=1, column=1)
        self.but3.grid(row=1, column=2)

    def destroy_all_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    

class Vampire:
    def __init__(self, name):
        self.name = name
        self.intelligence = 1
        self.speech = 1
        self.beauty = 1
        self.strength = 6
        self.speed = 6
        self.dexterity = 6
        self.blood = 1
        self.health = 10


class GameMaster:
    def __init__(self, vampire, root):
        self.vampire = vampire
        self.location = "Home"

        self.root = root
        self.window = Window(self.root, self)


    def find_deer(self):
        # Create a string listing the vampire's stats neatly
        stats = (
            f"Intelligence: {self.vampire.intelligence}, "
            f"Speech: {self.vampire.speech}, "
            f"Beauty: {self.vampire.beauty}, "
            f"Strength: {self.vampire.strength}, "
            f"Speed: {self.vampire.speed}, "
            f"Dexterity: {self.vampire.dexterity}, "
            f"Blood: {self.vampire.blood}, "
            f"Health: {self.vampire.health}"
        )
        
        self.window.label.config(text=f"You find a deer in the forest. You find that it quells the beast a little.\nYour stats are: {stats}")
        
        # Update the vampire's blood attribute
        self.vampire.blood += 1

    def enter_house(self):
        self.window.label.config(text="You sneak into a house and take a little blood from a sleeping person. He will be non the wiser.")
        self.vampire.blood += 1

    def find_camp(self):
        self.window.label.config(text="You find a camp with a sleeping knight. You're able to quench your thirst a little")
        self.vampire.blood += 1


    def explore(self):

        if self.window.location == "forest":
            self.find_deer()
        elif self.window.location == "village":
            self.enter_house()
        elif self.window.location == "road":
            self.find_camp()
        

    def change_location(self, new_location):
        self.window.location = new_location
        
        self.window.destroy_all_widgets()
        self.window.label = tk.Label(self.root, text=self.window.location)

        if new_location == "forest":
            self.window.but1 = tk.Button(self.root, text="Explore", command=lambda: self.explore())
            self.window.but2 = tk.Button(self.root, text="Go home", command=lambda: self.change_location("home"))

            self.window.label.grid(row=0, column=1)
            self.window.but1.grid(row=1, column=0)
            self.window.but2.grid(row=1, column=1)
             
        elif new_location == "village":
            self.window.but1 = tk.Button(self.root, text="Explore", command=lambda: self.explore())
            self.window.but2 = tk.Button(self.root, text="Go home", command=lambda: self.change_location("home"))

            self.window.label.grid(row=0, column=1)
            self.window.but1.grid(row=1, column=0)
            self.window.but2.grid(row=1, column=1)
        
        elif new_location == "road":
            self.window.but1 = tk.Button(self.root, text="Explore", command=lambda: self.explore())
            self.window.but2 = tk.Button(self.root, text="Go home", command=lambda: self.change_location("home"))

            self.window.label.grid(row=0, column=1)
            self.window.but1.grid(row=1, column=0)
            self.window.but2.grid(row=1, column=1)
        
        elif new_location == "home":
            self.window.but1 = tk.Button(self.root, text="Go to forest", command=lambda: self.change_location("forest"))
            self.window.but2 = tk.Button(self.root, text="Go to village", command=lambda: self.change_location("village"))
            self.window.but3 = tk.Button(self.root, text="Go to road", command=lambda: self.change_location("road"))
        
            self.window.label.grid(row=0, column=1)
            self.window.but1.grid(row=1, column=0)
            self.window.but2.grid(row=1, column=1)
            self.window.but3.grid(row=1, column=2)

        # I want to create an explore feature
        # An explore feature may trigger random events
        # I will make a random event for each location
        # There will be two types of events
        # Story events where the player will have agency
        # Regular events where the player will recieve some stats benifit

    
root = tk.Tk()
vampire = Vampire("Dracula")

gameMaster = GameMaster(vampire, root)

root.mainloop()
