import gym
from gym import spaces
import numpy as np

class WumpusWorldEnv(gym.Env):
    def __init__(self):
        super(WumpusWorldEnv, self).__init__()
        
        self.board_size = 5  # 5x5
        self.action_space = spaces.Discrete(5)  # up, down, left, right, pickup
        
        # Example: observation is flattened board plus player & wumpus pos
        self.observation_space = spaces.Box(low=0, high=1, shape=(5*5 + 4,), dtype=np.float32)
        
        self.reset()

    def reset(self):
        self.player = Player()
        self.wumpus = Wumpus()
        self.gold = [3,3]
        self.wall = [[1,2],[2,3],[3,4]]
        self.done = False
        return self._get_obs()
    
    def _get_obs(self):
        # Example: flatten the board into 0/1 representation + player and wumpus pos
        board_flat = np.zeros(5*5)
        # Could also encode walls, gold, player, wumpus separately
        # Here’s a minimal example
        idx_p = self.player.pos[0]*5 + self.player.pos[1]
        idx_w = self.wumpus.pos[0]*5 + self.wumpus.pos[1]
        idx_g = self.gold[0]*5 + self.gold[1] if self.gold != [-1, -1] else -1

        obs = []
        for i in range(5*5):
            if i == idx_p:
                obs.append(1)
            elif i == idx_w:
                obs.append(-1)
            elif i == idx_g:
                obs.append(0.5)
            else:
                obs.append(0)
        obs.extend(self.player.pos + self.wumpus.pos)
        return np.array(obs, dtype=np.float32)
    
    def step(self, action):
        # Player’s turn
        dir = action_to_dir(action)
        if action == 4:  # pickup
            if self.player.pos == self.gold:
                pick_up_gold(self.player, self.gold)
        else:
            self.player.move(dir)
        
        # Wumpus’s random move
        wumpus_dir = move_wumpus(rand.randint(1,4))
        self.wumpus.move(wumpus_dir)
        
        # Determine rewards
        reward = -0.1
        if self.player.pos == self.wumpus.pos:
            reward = -10
            self.done = True
        elif self.player.pos == [0,0] and 'g' in self.player.inv:
            reward = 10
            self.done = True
        
        return self._get_obs(), reward, self.done, {}
    
    def render(self):
        board = update_board(board, self.player, self.wumpus, self.gold, self.wall)
        for row in board:
            print(row)
        print()
