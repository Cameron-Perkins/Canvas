import random as rand
import gym
import Wumpus_World_Gym
import torch
import torch.optim as optim
import random
import numpy as np
from collections import deque

class Player():
    def __init__(self):
        self.pos = [0,0]
        self.inv = []
        self.board = [[]]

    def change_pos(self, dir):
        self.pos[0] += dir[0]
        self.pos[1] += dir[1]

    def Is_valid_move(self, dir):
        new_row = player.pos[0] + dir[0]
        new_col = player.pos[1] + dir[1]
        
        if not (0 <= new_row < len(board)) or not (0 <= new_col < len(board[0])):
            return False
        elif '0' in board[self.pos[0]+dir[0]][self.pos[1]+dir[1]]:
            return False
        else:
            return True

    def move(self, dir):
        if self.Is_valid_move(dir):
            self.change_pos(dir)
        else:
            print('Invalid move')
        

class Wumpus():
    def __init__(self):
        self.pos = [4,4]

    def change_pos(self, dir):
        self.pos[0] += dir[0]
        self.pos[1] += dir[1]
        
    def Is_valid_move(self, dir):
        new_row = wumpus.pos[0] + dir[0]
        new_col = wumpus.pos[1] + dir[1]
        
        if not (0 <= new_row < len(board)) or not (0 <= new_col < len(board[0])):
            return False
        else:
            return True
        
    def move(self, dir):
        if self.Is_valid_move(dir):
            self.change_pos(dir)
        else:
            pass


board = [['.','.','.','.','.'],
         ['.','.','.','.','.'],
         ['.','.','.','.','.'],
         ['.','.','.','.','.'],
         ['.','.','.','.','.']]


wall = [[1,2],[2,3],[3,4]]
gold = [3,3]


# This is a function that will update the board
# Takes in paraemters of board player wupus and gold.
# Then returns a board that contains the walls player wumpus and the gold.
def update_board(board, player, wumpus, gold, wall):
    board_dim = [len(board),len(board[0])]
    
    board = [['.'] * board_dim[1] for _ in range(board_dim[0])]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if [i,j] == player.pos:
                board[i][j] += 'p'
            if [i,j] == wumpus.pos:
                board[i][j] += 'w'
            if gold == [i,j]:
                board[i][j] += 'G'
            if [i,j] in wall:
                board[i][j] += '0'

    return board

def move_wumpus(inp):
    if inp == 1:
        return [-1,0]
    if inp == 2:
        return [1,0]
    if inp == 3:
        return [0,-1]
    if inp == 4:
        return [0,1]

def move_command(inp):
    if inp == 'w':
        return [-1,0]
    if inp == 's':
        return [1,0]
    if inp == 'a':
        return [0,-1]
    if inp == 'd':
        return [0,1]
    if inp == 'p':
        return [0,0]
    
def pick_up_gold(player, gold):
    gold[0] = -1
    gold[1] = -1
    player.inv.append('g')


player = Player()
wumpus = Wumpus()

i = True
while i == True:
    for j in board:
        print(j)
    print()

    inp = input()
    if inp in ['w','a','s','d']:
        dir = move_command(inp)
        player.move(dir)
    elif inp == 'p':
        pick_up_gold(player, gold)

    if player.pos == [0,0] and 'g' in player.inv:
        print('You win')
        i = False
    if player.pos == wumpus.pos:
        i = False
        print("You lose")
 
    # Move Wumpus
    r = rand.randint(1,4)
    mdir = move_wumpus(r)
    wumpus.move(mdir)
    board = update_board(board, player, wumpus, gold, wall)




#def Wumpus_World_2():


#if __name__ == "Wumpus_World_2":
#    Wumpus_World_2() 