import pygame
from pygame.draw import *
from random import *
from numpy import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 750))

def house(x, y, size):
    w = 100 * size
    rect(screen, (0, 0, 0), (int(x), int(y + w), int(w), int(w)), 2)
    rect(screen, (91, 58, 41), (int(x + 2), int(y + w) + 2, int(w - 2), int(w - 2)), 0)
    rect(screen, (122, 217, 255), (int(x + w/4), int(y + 5*w/4), int(w / 2), int(w / 2)), 0)
    rect(screen, (204, 119, 34), (int(x + w/4) - 2, int(y + 5*w/4) - 2, int(w / 2) + 2, int(w / 2) + 2), 2)
    polygon(screen, (255, 0, 0), [(int(x), int(y + w)), (int(x + w/2), int(y + w/2)), (int(x + w), int(y + w))], 0)
    polygon(screen, (0, 0, 0), [(int(x), int(y + w)), (int(x + w/2), int(y + w/2)), (int(x + w), int(y + w))], 3)
    
def cloud(x, y, size):
    w = 100 * size
    r = w / 3
    a = 1
    while a <= 10:
        xx = randint(int(x + r), int(x + 2*w - r))
        yy = randint(int(y + r), int(y + w - r))
        circle(screen, (255, 255, 255), (xx, yy), int(r), 0)
        circle(screen, (0, 0, 0), (xx, yy), int(r), 1)
        a += 1

def tree(x, y, size):
    w = 100 * size
    r = w / 3
    rect(screen, (0, 0, 0), (int(x + 7*w/12), int(y + w), int(w / 6), int(w)), 0)
    circle(screen, (0, 153, 0), (int(x + w/2), int(y + w)), int(r), 0)
    circle(screen, (0, 0, 0), (int(x + w/2), int(y + w)), int(r), 2)
    circle(screen, (0, 153, 0), (int(x + 5*w/6), int(y + w)), int(r), 0)
    circle(screen, (0, 0, 0), (int(x + 5*w/6), int(y + w)), int(r), 2)
    circle(screen, (0, 153, 0), (int(x + w/3), int(y + 2*w/3)), int(r), 0)
    circle(screen, (0, 0, 0), (int(x + w/3), int(y + 2*w/3)), int(r), 2)
    circle(screen, (0, 153, 0), (int(x + w), int(y + 2*w/3)), int(r), 0)
    circle(screen, (0, 0, 0), (int(x + w), int(y + 2*w/3)), int(r), 2)
    circle(screen, (0, 153, 0), (int(x + 3*w/4), int(y + 2*w/3)), int(r), 0)
    circle(screen, (0, 0, 0), (int(x + 3*w/4), int(y + 2*w/3)), int(r), 2)
    circle(screen, (0, 153, 0), (int(x + w/2), int(y + w/3)), int(r), 0)
    circle(screen, (0, 0, 0), (int(x + w/2), int(y + w/3)), int(r), 2)
    circle(screen, (0, 153, 0), (int(x + 5*w/6), int(y + w/3)), int(r), 0)
    circle(screen, (0, 0, 0), (int(x + 5*w/6), int(y + w/3)), int(r), 2)
   
def sun(x, y, size):
    R = 100 * size
    r = R - 10
    w = 100 * size
    a = 0
    b = 0
    n = 20
    pl = []
    while a < 6.28:
        xx = x + R*cos(a)
        yy = y + R*sin(a)
        a += 3.14/n
        xxx = x + r*cos(a)
        yyy = y + r*sin(a)
        pl.append((int(xx), int(yy)))
        pl.append((int(xxx), int(yyy)))
    polygon(screen, (254, 254, 34), pl, 0)
    polygon(screen, (0, 0, 0), pl, 1)
        
        

rect(screen, (30, 144, 255), (0, 0, 1200, 400), 0)
rect(screen, (0, 255, 0), (0, 400, 1200, 350), 0)
house(200, 150, 2)
house(600, 200, 1.5)
cloud(600, 100, 1.5)
cloud(300, 100, 1)
cloud(1000, 150, 1)
tree(800, 350, 1.5)
tree(450, 400, 1)
sun(100, 100, 0.7)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
