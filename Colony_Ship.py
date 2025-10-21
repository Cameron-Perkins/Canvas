import random

# This is the colony ship game.
# You travel from island to island trying to find a place to settle.

# This is the colony ship class.
# This holds the attibutes for the colony ship.

# Here I can either make events or create a system for isalnd iscriptiongs.
# I will make the system of island descriptions, bc there are less variables.
# So we have the arrtibutes of the islands we can use thresholds to categorize them.
# Maybe we can have ranges to make things make more sense. Aslo we can shift some of the numbers.
# For example we can make the tempeture celcius.
# The system to describe islands will be complicated.
# We can break up the settings into zones.
# We will combine water sources on the island with sky precipitation.
# Things can range from none, to desolate, sparce, some, aboundunt, and pleantiful.
# The most complicated thing will be combining different elements to produce new results.
# For example a heavily forest place with lots of food will have forest animals, but a place with less timber might have goats and plains.
# So what to do.
# Firstly break things up into thresholds then produce text based on what they fall into.
# The last thing to build is the events that will hurt the ship.
# We should brain storm some events.
# Pirate attack, dease, storm, meeting mermaid, meeting calypso, fining treasure, ship materials, fining food source.

# A random event needs the following, a name
# flavour text, list of effects on the attributes.
# The events will be functions.
# The functions only need to take and return the ship object.


class ColonyShip():
    def __init__(self, name = "Test", crew_size = 1000, supplies = 1000, health = 1000, culture = 100, science = 100):
        self.name = name
        self.crew_size = crew_size
        self.supplies = supplies
        self.health = health
        self.culture = culture
        self.science = science
    
    def get_ship_status(self):
        print(f"Ship Name: {self.name}")
        print(f"Crew Size: {self.crew_size}")
        print(f"Supplies: {self.supplies}")
        print(f"Health: {self.health}")
        print(f"Culture: {self.culture}")
        print(f"Science: {self.science}")
    

# This is the class that stores the attibutes of each island.
class Island():
    def __init__(self, climate = 0, water = 0, soil = 0, wildlife = 0, timber = 0):
        self.climate = climate
        self.water   = water
        self.soil    = soil
        self.fish    = wildlife
        self.timber  = timber

    # This randomly generates the attributes for the island.
    def generate_attributes(self):
        import random
        self.climate = random.randint(0,100)
        self.water   = random.randint(0,100)
        self.soil    = random.randint(0,100)
        self.fish    = random.randint(0,100)
        self.timber  = random.randint(0,100)

    # This prints the description of the island.
    def Island_Description(self):
        thresholds = [0, 25, 50, 75, 100]
        text = ''

        if self.climate <= 25:
            text += "The island is freezing, water little water there is has been frozen."
        elif self.climate <= 50:
            text += "The island is cold, water sources are scarce."
        elif self.climate <= 75:
            text += "The island has a temperate climate, water sources are adequate."
        else:
            text += "The island is tropical, water sources are abundant."
        
        if self.soil <= 25:
            text += "The soil is poor, farming will be difficult."
        elif self.soil <= 50:
            text += "The soil is fair, farming will be possible with effort."
        elif self.soil <= 75:
            text += "The soil is good, farming will be successful."
        else:
            text += "The soil is excellent, farming will be bountiful."

        if self.fish <= 25:
            text += "The island has little fish, fishing will be difficult."
        elif self.fish <= 50:
            text += "The island has some fish, fishing will be possible with effort."
        elif self.fish <= 75:
            text += "The island has plenty of fish, fishing will be successful."
        else:
            text += "The island has abundant fish, fishing will be bountiful."

        if self.timber <= 25:
            text += "The island has little timber, building will be difficult."
        elif self.timber <= 50:
            text += "The island has some timber, building will be possible with effort."
        elif self.timber <= 75:
            text += "The island has plenty of timber, building will be successful."
        else:
            text += "The island has abundant timber, building will be bountiful."

        print(text)


# This is an event where mermaids are encountered and lead the ship to food.
def mermaid_event(ship):
    print("You encounter a group of mermaids who offer to lead you to a nearby island rich in food resources.")
    ship.supplies += 200
    print("Your supplies have increased by 200.")
    return ship

# This is an event where some of the crew gets sick.
def illness_event(ship):
    print("A sickness spreads through the crew, killing some crew members.")
    ship.crew_size -= 150
    print("Your ship's health has decreased by 150.")
    return ship

# This is an event where the ship hits rocks.
def rock_event(ship):
    print("The ship hits hidden rocks, causing damage to the hull.")
    ship.health -= 200
    print("Your ship's health has decreased by 200.")
    return ship

# I need this to produce a score based on the island attributes and the ships attributes.
def create_end_story(score):
        if score <= 25:
            print("Overall, this island is a poor choice for settlement. The colonists did not survive.")
        elif score <= 50:
            print("Overall, this island is a fair choice for settlement. The colonists struggled to survive.")
        elif score <= 75:
            print("Overall, this island is a good choice for settlement. The colonists thrived.")
        else:
            print("Overall, this island is an excellent choice for settlement. The colonists prospered.")



def game_over(ship):
    if ship.crew_size <= 0:
        print("All crew members have perished. Game Over.")
        return True
    if ship.supplies <= 0:
        print("The ship has run out of supplies. Game Over.")
        return True
    if ship.health <= 0:
        print("The ship is no longer seaworthy. Game Over.")
        return True
    return False 

# This calculates the score of the island.
def calculate_score(island):
    score = (island.climate + island.water + island.soil + island.fish + island.timber) / 5
    return score

# game loop 
loop = True
island = Island()
ship = ColonyShip('Test', 1000, 1000, 100)

print("This is the colony ship. You are a sailor in the 1700s looking for a place to land.")

# This is the main game loop.
while loop == True:
    island.generate_attributes()

    ship.get_ship_status()
    island.Island_Description()

    print("Do you want to land. y/n")
    i = input()

    # This is where a random event is can occur.
    random_int = random.randint(0,100)
    print(random_int)

    if i == 'y':
        print("You landed good luck with your colony")
        print("Your island score is: ")
        score = calculate_score(island)
        print(score)
        loop = False
        create_end_story(score)
    else:
        print("You decided not to settle and move on to another island.")


    if random_int <= 50:
        event_int = random.randint(0,100)
        if event_int <= 33:
            ship = mermaid_event(ship)
        elif event_int <= 66:
           ship = rock_event(ship)
        else:
            ship = illness_event(ship)

    if game_over(ship) == True:
        loop = False
        print("I'm afraid you ship and crew is no longer sea worth. Game Over.")