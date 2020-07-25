from hringhorni import Hringhorni

my_grid = Hringhorni(n=15)
my_grid.set_shapes(["glider"])

s_0 = my_grid.raw_obs()
all_states = [s_0]

T = 1
for i in range(T):
    state = my_grid.step()
    all_states.append(state)

my_grid.tstep_display(all_states, 1, 1)