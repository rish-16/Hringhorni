from hringhorni import Hringhorni

grid = Hringhorni(10)
grid.random_spawn()
states = []

# taking 10 steps
for i in range(10):
    state = grid.render()
    grid.step()
    states.append(state)
    
grid.animate(states)