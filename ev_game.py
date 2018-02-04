import random
from random import randint
class area:
    def __init__(self,pos_x,pos_y,food,capacity):
        self.x = pos_x
        self.y = pos_y
        self.f = food
        self.c = capacity

# class individue(pos_x,pos_y,id_,size):
#     self.i = id_
#     self.x = pos_x
#     self.y = pos_y

rows  = 5
colums = 3

grid = []
for i in range(rows):
    grid.append([])
for i in range(rows):
    for l in range(colums):
        if randint(0,1) == 1:
            grid[i].append(area(i,l,randint(10,100),randint(10,100)))
        else:
            grid[i].append(area(i,l,0,0))
