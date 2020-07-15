from hringhorni import Hringhorni
import matplotlib.pyplot as plt

grid = Hringhorni(10)
grid.random_spawn(n_cells=10)
T = 1

s_0 = grid.raw_obs()
grid.display()

# taking T steps
for i in range(T):
    grid.step()
    
s_t = grid.raw_obs()
grid.display()

plt.figure(1)
plt.subplot(121)
plt.imshow(s_0, cmap="gray")
plt.title("Original")

plt.subplot(122)
plt.imshow(s_t, cmap="gray")
plt.title("T = {}".format(T))

plt.show()