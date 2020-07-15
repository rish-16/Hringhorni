import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class Hringhorni:
    def __init__(self, n):
        self.grid = np.array([[0 for i in range(n)] for i in range(n)])
        self.n = n
        
    def reset(self):
        self.grid = np.array([[0 for i in range(self.n)] for i in range(self.n)])
        
    def render(self):
        state = plt.imshow(self.grid, animated=True)
        
        return [state]
        
    def random_spawn(self, n_cells=5):
        count = 0
        while count != n_cells:
            x = np.random.randint(0, self.n)
            y = np.random.randint(0, self.n)
            
            if self.grid[x][y] == 0:
                self.grid[x][y] = 255
                count += 1
                
    def step(self):
        print ("Updating state")
        # reset grid
        self.reset()
        self.random_spawn()
                
    def animate(self, frames):
        fig = plt.figure()
        print ("Animating...")
        anim = animation.ArtistAnimation(fig, frames, interval=50, blit=True, repeat_delay=2000)
        plt.show()