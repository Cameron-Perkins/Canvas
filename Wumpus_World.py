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

for i in matrix:
    print(i)