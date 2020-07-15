from hringhorni import Hringhorni

grid = Hringhorni(10)
all_points = [[3, 3], [2, 4], [0, 9], [0, 7], [9, 9], [8, 9]]
grid.populate(all_points)

grid.display()