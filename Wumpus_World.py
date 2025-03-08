import random as rand
import numpy as np

size = 20  # Define the size of the square matrix
matrix = [[0 for _ in range(size)] for _ in range(size)]

matrix[10][19] = "G"

# This function is used to generate a list of tiles that are valid given some tile t.
# The function takes a list of two numbers and creates of a list of all list around is excluding those that are out of bounds.
# For example if t = [0,0] then the function will return [[1,0],[1,1],[0,1]].
# The function takes two inputs a list of two numbers t and a list of list of previous tiles.
# The second parameter defaults to an empty list.
# The function return a list of valid tiles.

class Jack:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.gold = False
    
    def pick_up_gold_or_end(self, matrix):
        print(self.x == 0 and self.y == 0 and self.gold == True)
        print(self.x == 0 and self.y == 0)
        print(self.gold == True)

        if matrix[self.y][self.x] == "G":
            self.gold = True
        if self.x == 0 and self.y == 0 and self.gold == True:
            print("You win!")
        elif self.gold == True and (player.x == 0 or player.y == 0):
            print("Have gold not at entrence")
        
    def move(self, direction, matrix):
        print(matrix[self.y][self.x])
        if matrix[self.y][self.x] == "G":
            self.gold = True
        matrix[self.y][self.x] = "P"
        matrix[self.y][self.x] = "E"
        if direction == "n":
            self.y += 1
        elif direction == "s":
            self.y -= 1
        elif direction == "e":
            self.x += 1
        elif direction == "w":
            self.x -= 1
        elif direction == "nw":
            self.y += 1
            self.x -= 1
        elif direction == "ne":
            self.y += 1
            self.x += 1
        elif direction == "sw":
            self.y -= 1
            self.x -= 1
        elif direction == "se":
            self.y -= 1
            self.x += 1
        elif direction == "p":
            print("in")
            self.pick_up_gold_or_end(matrix)
        print(self.x, self.y)
        return matrix


class Wumpus:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

def add_tile_to_board(matirx, t):
    matrix[t[0]][t[1]] = "E"
    return matrix

def generate_board(matrix):
    edge_tiles = [[0,0]]
    previous_tiles = []
    while edge_tiles:
        # We will take a random tile from the edge tiles this will be put into previous tiles and in generate vaild tiles
        r = rand.randint(0,len(edge_tiles)-1)
        e = edge_tiles[r]
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


    Game = True
    player = Jack()

    #Game loop
    while Game:
        for i in matrix:
            print(i)
        i = input()
        matrix = player.move(i, matrix)

