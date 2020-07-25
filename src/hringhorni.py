import copy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class Hringhorni:
    def __init__(self, n=8):
        self.grid = np.array([[0 for i in range(n)] for i in range(n)])
        assert n >= 8, "size `n` should be 8 and above"
        self.n = n
        
    def reset(self):
        self.grid = np.array([[0 for i in range(self.n)] for i in range(self.n)])
        
    def raw_obs(self):
        grid = copy.deepcopy(self.grid)
        return grid
        
    def display(self):
        for i in range(self.n):
            row = ""
            for j in range(self.n):
                row += "{:^3}".format(self.grid[i][j])
            print (row)
        print ()
                
    def render(self):
        state = plt.imshow(self.grid, animated=True)
        
        return [state]
        
    def populate(self, coords):
        for i in range(len(coords)):
            self.grid[coords[i][1]][coords[i][0]] = 255
        
    def random_spawn(self, n_cells=10):
        count = 0
        while count != n_cells:
            x = np.random.randint(0, self.n-1)
            y = np.random.randint(0, self.n-1)
            
            if self.grid[x][y] == 0:
                self.grid[x][y] = 255
                count += 1
                
    # cell spawning rules
    def judgement(self, i, j, n_neighbours):
        new_val = 0
        if self.grid[i][j] == 255: # alive
            if n_neighbours in [2, 3]: # stable population
                new_val = 255 
            else: # overpopulation
                new_val = 0
                
        elif self.grid[i][j] == 0: # dead
            if n_neighbours == 3: # reproduction
                new_val = 255
            else:
                new_val = 0
        
        return new_val
                
    def get_alive_neighbours(self, i, j):
        neighbours = [[x2, y2] for x2 in range(j-1, j+2)
                               for y2 in range(i-1, i+2)
                               if (-1 < j < self.n and
                                   -1 < i < self.n and
                                   (j != x2 or i != y2) and
                                   (0 <= x2 < self.n) and
                                   (0 <= y2 < self.n))]                  
                                   
        n_alive_neighbours = 0                                   
        for i in range(len(neighbours)):
            if self.grid[neighbours[i][0]][neighbours[i][1]] == 255: # alive
                n_alive_neighbours += 1
                                
        return n_alive_neighbours
                
    def step(self):
        """
        Get number of alive neighbours before spawning and killing cells
        """
        
        new_config = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                n_alive_neighbours = self.get_alive_neighbours(i, j)
                new_val = self.judgement(i, j, n_alive_neighbours)
                new_config[i][j] = new_val
                
        self.grid = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(len(new_config)):
            for j in range(len(new_config)):
                self.grid[i][j] = new_config[i][j]
                
        state = copy.deepcopy(self.grid)
        return state
        
    def set_shapes(self, shape_list):
        for i in range(len(shape_list)):
            cur_shape = shape_list[i]
            
            if cur_shape == "glider":
                random_x = self.n // 2
                random_y = self.n // 2
                
                self.grid[random_y][random_x-1] = 255
                self.grid[random_y][random_x+1] = 255
                self.grid[random_y-1][random_x+1] = 255
                self.grid[random_y+1][random_x] = 255
                self.grid[random_y+1][random_x+1] = 255
        
    def tstep_display(self, states, r, c):
        T = len(states) - 1 # ignore first state
        fig = plt.figure(1)
        plt.tight_layout()
        fig.suptitle("Cellular Automata for T = {}".format(T))
        
        for i in range(T):
            plt.subplot(r, c, i+1)
            plt.imshow(states[i], cmap="gray")
            plt.title("T = {}".format(i))
            plt.axis("off")

        plt.show()        
                
    def animate(self, frames):
        fig = plt.figure()
        print ("Animating...")
        anim = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=2000)
        return anim