import random as rand
import numpy as np

# We want to make some improvements.
# We want to fix the movement function there is an issue where I can only move down and anything north is a void

size = 20  # Define the size of the square matrix
matrix = [[0 for _ in range(size)] for _ in range(size)]

matrix[10][19] = "G"

# This function is used to generate a list of tiles that are valid given some tile t.
# The function takes a list of two numbers and creates of a list of all list around is excluding those that are out of bounds.
# For example if t = [0,0] then the function will return [[1,0],[1,1],[0,1]].
# The function takes two inputs a list of two numbers t and a list of list of previous tiles.
# The second parameter defaults to an empty list.
# The function return a list of valid tiles.

#This is the wumpus the horrific monster the player must avoid
class Wumpus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kill = False
    
    def Move(self, x, y, matrix):
        x1 = self.x
        x2 = self.y
        self.x+=x
        self.y+=y
        # This check if you are about to step into the void. Here if the tile you want to step into is out side the matrix or into a void which is zero the program will return you to the previous square.
        if self.y > len(matrix)-1 or self.x > len(matrix[0])-1 or self.y < 0 or self.x < 0:
            self.x = x1
            self.y = x2

    def Actions(self, direction, matrix, prev="E"):
        matrix[self.y][self.x] = prev
        direction = rand.randint(0,7)
        print('direction is ',direction)
        if direction == 0:
            self.Move(0,-1,matrix)
        elif direction == 1:
            self.Move(0,1,matrix)
        elif direction == 2:
            self.Move(1,0,matrix)
        elif direction == 3:
            self.Move(-1,0,matrix)
        elif direction == 4:
            self.Move(-1,-1,matrix)
        elif direction == 5:
            self.Move(1,-1,matrix)
        elif direction == 6:
            self.Move(-1,1,matrix)
        elif direction == 7:
            self.Move(1,1,matrix)


        curr = matrix[self.y][self.x]
        matrix[self.y][self.x] = "W"
        print(self.x, self.y)
        return matrix, curr

class Jack:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.gold = False
    
    def pick_up_gold_or_end(self, matrix, curr):
        if curr == "G":
            self.gold = True
        if self.x == 0 and self.y == 0 and self.gold == True:
            print("You win!")
        elif self.gold == True and (player.x == 0 or player.y == 0):
            print("Have gold not at entrence")

    # This function moves the player to a position, and check if the players move is valid. If it is not valid is places the player in original loacation and prints a message saying to try again.
    def Move(self, x, y, matrix):
        x1 = self.x
        x2 = self.y
        self.x+=x
        self.y+=y
        # This check if you are about to step into the void. Here if the tile you want to step into is out side the matrix or into a void which is zero the program will return you to the previous square.
        if self.y > len(matrix)-1 or self.x > len(matrix[0])-1 or self.y < 0 or self.x < 0 or matrix[self.y][self.x] == 0:
            self.x = x1
            self.y = x2
            print("You tried to step into the void missed move")

        
    def Actions(self, direction, matrix, prev="E"):
        matrix[self.y][self.x] = prev
        if direction == "n":
            self.Move(0,-1,matrix)
        elif direction == "s":
            self.Move(0,1,matrix)
        elif direction == "e":
            self.Move(1,0,matrix)
        elif direction == "w":
            self.Move(-1,0,matrix)
        elif direction == "nw":
            self.Move(-1,-1,matrix)
        elif direction == "ne":
            self.Move(1,-1,matrix)
        elif direction == "sw":
            self.Move(-1,1,matrix)
        elif direction == "se":
            self.Move(1,1,matrix)
        elif direction == "p":
            if prev == "G":
                print("Picked up gold.")
                self.gold = True
                matrix[self.y][self.x] = "E"
            if self.gold == True and (self.x == 0 and self.y == 0):
                print("You win!")

        curr = matrix[self.y][self.x]
        matrix[self.y][self.x] = "P"
        return matrix, curr



def generate_valid_tiles(t, previous_tiles=[]):
    tiles = [[t[0]-1,t[1]-1], [t[0]-1,t[1]], [t[0]-1,t[1]+1], [t[0],t[1]-1], [t[0],t[1]+1], [t[0]+1,t[1]-1], [t[0]+1,t[1]], [t[0]+1,t[1]+1]]
    tile=0
    while tile < len(tiles):
        i = tiles[tile]
        if i[0] < 0 or i[1] < 0 or i[0] > size-1 or i[1] > size-1:
            tiles.remove(i)
            tile=-1
        tile+=1
    
    for i in previous_tiles:
        if i in tiles:
            tiles.remove(i)
    return tiles

def add_tile_to_board(matrix, t):
    matrix[t[0]][t[1]] = "E"
    return matrix

def generate_board(matrix):
    edge_tiles = [[0,0]]
    previous_tiles = []
    while edge_tiles:
        # We will take a random tile from the edge tiles this will be put into previous tiles and in generate vaild tiles
        r = rand.randint(0,len(edge_tiles)-1)
        e = edge_stiles[r]
        previous_tiles.append(e)
        # We will then generate a random number 1 through 8
        n = rand.randint(1,8)
        # This will be the number of tiles added to the board
        valid_tiles = generate_valid_tiles(e)
        
        if e == [10,19]:
            break

        for i in range(n):
            r = rand.randint(0,len(valid_tiles)-1)
            matrix = add_tile_to_board(matrix, valid_tiles[r])
            edge_tiles.append(valid_tiles[r])
        
        for i in previous_tiles:
            if i in edge_tiles:
                edge_tiles.remove(i)

    return matrix



name = "Wumpus_World.py"
if __name__ == "__main__":
    size = 10
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    matrix = generate_board(matrix)
    matrix[2][2] = "G"
    matrix[0][0] = "P"
    matrix[9][9] = "W"


    Game = True
    player = Jack()
    wumpus = Wumpus(9,9)
    curr = "E"

    #Game loop
    while Game:
        for i in matrix:
            print(i)
        i = input()
        matrix, curr = player.Actions(i, matrix, curr)
        matrix, curr = wumpus.Actions(i, matrix, curr)

        print(player.gold)

        if player.x == wumpus.x and player.y == wumpus.y:
            Game = False
            print("You lose!")
        if player.x == 0 and player.y == 0 and player.gold == True:
            Game = False
            print("You win!")

