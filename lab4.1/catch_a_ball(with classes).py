import pygame
from pygame.draw import *
from numpy import *
from random import randint
pygame.init()

#video settings
W = 700
H = 700
FPS = 60
screen = pygame.display.set_mode((W, H))

#scores block
SCRW = 0; HISC = []; MOVES = 99; FINISHED = False

#balls characteristics
N = 10; V = 10

#bombs characteristics
Nb = 10; Vb = 10; Sb = 60

#colors
RED = (255, 0, 0); BLUE = (0, 0, 255); YELLOW = (255, 255, 0)
GREEN = (0, 255, 0); MAGENTA = (255, 0, 255); CYAN = (0, 255, 255)
BLACK = (0, 0, 0); WHITE = (255, 255, 255)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball():
    def __init__(self):
        self.x = randint(100, 500)
        self.y = randint(100, 600)
        self.vx = randint(-V, V)
        self.vy = randint(-V, V)
        self.r = randint(20, 40)
        self.color = COLORS[randint(0,4)]
    def move(self):
        if self.color == BLACK:
            self.color = COLORS[randint(0,4)]
            self.r = randint(20, 40)
            self.x = randint(self.r, W - (100 + self.r))
            self.y = randint(self.r, H - self.r)
            self.vx = randint(-V, V)
            self.vy = randint(-V, V)
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= W - 100 or self.x - self.r <= 0:
            self.vx = -1 * self.vx
        if self.y + self.r >= H or self.y - self.r <= 0:
            self.vy = -1 * self.vy
        circle(screen, self.color, (int(self.x), int(self.y)), int(self.r))

class Bomb():
    def __init__(self):
        self.x = randint(100, 500)
        self.y = randint(100, 600)
        self.vx = randint(-Vb, Vb)
        self.vy = randint(-Vb, Vb)
        self.r = randint(20, 40)
        self.color = RED
    def move(self):
        if self.color == BLACK:
            self.color = RED
            self.x = randint(Sb, W - (100 + Sb))
            self.y = randint(Sb, H - Sb)
            self.vx = randint(-Vb, Vb)
            self.vy = randint(-Vb, Vb)
        self.x += self.vx
        self.y += self.vy
        if self.x + Sb >= W - 100 or self.x <= 0:
            self.vx = -1 * self.vx
        if self.y + Sb >= H or self.y <= 0:
            self.vy = -1 * self.vy
        rect(screen, self.color, (int(self.x), int(self.y), Sb, Sb), 0)
    
#read HS history
out = open('HS.txt', 'r')
for a in range (0, 5):
    HISC.append(int(out.readline()))
out.close()

#init balls
ball = []  
for i in range (0, N): ball.append(Ball())      

#draw balls
def new_ball():
    for i in range (0, N): 
        ball[i].move()    

#init bombs
bomb = []  
for i in range (0, Nb): bomb.append(Bomb())    
        
#draw bombs        
def new_bomb():
    for i in range (0, Nb): 
        bomb[i].move()    
   

#count scores       
def click(event):
    global SCRW, V, REC, Sb, MOVES, FINISHED
    for i in range(0,N):
        if ((event.pos[0] - ball[i].x)**2 + (event.pos[1] - ball[i].y)**2 
            <= ball[i].r**2):
            SCRW += 1
            ball[i].r = 0
            ball[i].color = BLACK 
            V += 1
    for i in range(0,Nb):
        if ((event.pos[0] - bomb[i].x <= Sb and event.pos[1] - bomb[i].y <= Sb 
            and event.pos[0] - bomb[i].x >= 0 and event.pos[1] - bomb[i].y >= 0)):
            SCRW -= 1
            bomb[i].color = BLACK
            Sb += 5
    MOVES -= 1
    if MOVES == 0: FINISHED = True

#print scores
def counter():
    surf = pygame.Surface((100, 30))
    surf.fill((0, 0, 0))
    rect(surf, WHITE, (0,0, 100,30), 5)
    font = pygame.font.Font(None, 25)
    text = font.render('Scores: ' + str(SCRW), True, WHITE)
    surf.blit(text, (10,5))
    screen.blit(surf, (0, 0))
    surf1 = pygame.Surface((100, 122))
    surf1.fill((0, 0, 0))
    font1 = pygame.font.Font(None, 20)
    line(screen, WHITE, (W - 100, 0), (W - 100, H), 3)
    line(surf1, WHITE, (0, 20), (100, 20), 3)
    rect(surf1, WHITE, (0, 0, 100, 120), 3)
    for i in range (1, 6):
        line(surf1, WHITE, (0, 20*(i + 1)), (100, 20*(i + 1)), 3)
        text = font1.render(str(HISC[i-1]), True, WHITE)
        surf1.blit(text, (10, 5 + 20*i))
    text = font1.render('HighScores', True, WHITE)
    surf1.blit(text, (10, 5))
    font = pygame.font.Font(None, 42)
    text = font.render('Moves', True, WHITE)
    screen.blit(text, (605, 350))
    text = font.render(str(MOVES), True, WHITE)
    screen.blit(text, (630, 380))
    screen.blit(surf1, (W - 100, 0))
    

pygame.display.update()
clock = pygame.time.Clock()

while not FINISHED:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            FINISHED = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    new_ball()
    counter()
    new_bomb()
    pygame.display.update()
    screen.fill(BLACK)
           
#rewrite HS history
if SCRW > HISC[4]: HISC[4] = SCRW
HISC.sort(reverse = True)
inp = open('HS.txt', 'w')
inp.flush()
for i in range(0, 5):
    inp.write(str(HISC[i]) + '\n')
inp.close()

print(SCRW)
pygame.quit()