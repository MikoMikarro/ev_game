import random
from random import randint
class area:

    def __init__(self,pos_x,pos_y,food,capacity):
        self.poblation = []
        self.x = pos_x
        self.y = pos_y
        self.f = food
        self.c = capacity
    def add_colony(self,num,id_):
        for i in range(num):
            self.poblation.append(individue(id_,self.x,self.y))
class individue:
    def __init__ (self,id_,pos_x,pos_y):
        self.i = id_
        self.x = pos_x
        self.y = pos_y
    def __str__ (self):
        print id_
    def move(self,x = 0,y = 0):
        old_x = 0
        old_x += self.x
        old_y = 0
        old_y += self.y
        new_x = self.x+x
        new_y = self.y+y
        while True:
            if new_x > colums-1:
                new_x -=colums
            elif new_x < 0:
                new_x +=colums
            else:
                break
        while True:
            if new_y > (rows-1):
                new_y -= rows
            elif new_y < 0:
                new_y += rows
            else:
                break
        self.y = new_y
        self.x = new_x
        grid[self.y][self.x].poblation.append(self)
        grid[old_y][old_x].poblation.remove(self)


# inum = 10
# ids = []
# for i in range(inum):
#     ids.append("id:"+str(i+1))
#
rows  = 10
colums = 10
#
grid = []
for i in range(rows):
    grid.append([])
for i in range(rows):
    for l in range(colums):
        if randint(0,1) == 1:
            grid[i].append(area(i,l,randint(10,100),randint(1,10)))
        else:
            grid[i].append(area(i,l,0,randint(1,10)))

# for i in grid:
#     for l in i:
#         if randint(0,1)==1:
#             l.add_colony(randint(0,l.c-1),ids[randint(0,len(ids)-1)])
grid[0][0].add_colony(1,"id:1")

while True:
    orders = []
    for i in range(rows):
        for l in range(colums):
            if len(grid[i][l].poblation) !=0:
                orders.append([])
                orders[-1].append("m")
                orders[-1].append(randint(1-colums,colums-1))
                orders[-1].append(randint(1-rows,rows-1))
                orders[-1].append(grid[i][l].poblation[0])
    for i in orders:
        if i[0] == 'm':
                i[3].move(i[1],i[2])
    txt = ""
    for i in range(rows):
        for l in range(colums):
            try:
                txt += "[ "+str(grid[i][l].poblation[0].i)+" ]"
            except:
                txt += "[ 0 ]"
        txt += "\n"
    print txt
    a  = raw_input()
