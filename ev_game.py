import pygame as py
from pygame.locals import *
import random
from random import randint
py.init()
py.font.init()

white = [255, 255, 255]
screen = py.display.set_mode((640, 480))
py.display.set_caption("Evolution simulator.")

class individuo:
    def __init__ (self,pos_x,pos_y,size,speed):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size
        self.speed = speed

    def mover():
        self.pos_x = randint(-1,1,2)*self.speed
        self.pos_y = randint(-1,1,2)*self.speed

a = individuo(320,240,10,3)

while True


# pobl = []
# for i in range(randint(10,100)):
#     pobl.append(individuo(0,0,0))

# check  = True
# while check:
#     for event in py.event.get():
#         if event.type == py.KEYDOWN:
#             if event.key == py.K_SPACE:
#                 check = False
#                 break
#     py.display.flip()

py.quit()
