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
N = 10; V = 10; X = []; Y = []; Vx = []; Vy = []; R = []; COLOR = []

#bombs characteristics
Nb = 5; Vb = 10; Xb = []; Yb = []; Vxb = []; Vyb = []; Sb = 40; COLORb = []

#colors
RED = (255, 0, 0); BLUE = (0, 0, 255); YELLOW = (255, 255, 0)
GREEN = (0, 255, 0); MAGENTA = (255, 0, 255); CYAN = (0, 255, 255)
BLACK = (0, 0, 0); WHITE = (255, 255, 255)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#set balls characteristics
for a in range(0, N):
    X.append(randint(100, 500))
    Y.append(randint(100, 600))
    Vx.append(randint(-V, V))
    Vy.append(randint(-V, V))
    R.append(randint(20, 40))
    COLOR.append(COLORS[randint(0, 4)])
    
#set bombs characteristics    
for a in range(0, Nb):
    Xb.append(randint(100, 500))
    Yb.append(randint(100, 600))
    Vxb.append(randint(-V, V))
    Vyb.append(randint(-V, V))
    COLORb.append(RED)

#read HS history
out = open('HS.txt', 'r')
for a in range (0, 5):
    HISC.append(int(out.readline()))
out.close()
        
#draw ball
def new_ball():
    global X, Y, R, Vx, Vy, COLOR
    a = 0
    while a < N:
        if COLOR[a] == BLACK:
            COLOR[a] = COLORS[randint(0, 4)]
            R[a] = randint(20, 40)
            X[a] = randint(R[a], W - (100 + R[a]))
            Y[a] = randint(R[a], H - R[a])
            Vx[a] = randint(-V, V)
            Vy[a] = randint(-V, V)
        X[a] = X[a] + Vx[a]
        Y[a] = Y[a] + Vy[a]
        if X[a] + R[a] >= W - 100 or X[a] - R[a] <= 0:
            Vx[a] = -1 * Vx[a]
        if Y[a] + R[a] >= H or Y[a] - R[a] <= 0:
            Vy[a] = -1 * Vy[a]
        circle(screen, COLOR[a], (int(X[a]), int(Y[a])), int(R[a]))
        a += 1
        
#draw bomb        
def new_bomb():
    global Xb, Yb, Rb, Vxb, Vyb, COLOR
    a = 0
    while a < Nb:
        if COLORb[a] == BLACK:
            COLORb[a] = RED
            Xb[a] = randint(Sb, W - (100 + Sb))
            Yb[a] = randint(Sb, H - Sb)
            Vxb[a] = randint(-Vb, Vb)
            Vyb[a] = randint(-Vb, Vb)
        Xb[a] = Xb[a] + Vxb[a]
        Yb[a] = Yb[a] + Vyb[a]
        if Xb[a] + Sb >= W - 100 or Xb[a] <= 0:
            Vxb[a] = -1 * Vxb[a]
        if Yb[a] + Sb >= H or Yb[a] <= 0:
            Vyb[a] = -1 * Vyb[a]
        rect(screen, COLORb[a], (int(Xb[a]), int(Yb[a]), Sb, Sb), 0)
        a += 1

#count scores       
def click(event):
    global SCRW, V, REC, Sb, MOVES, FINISHED
    for i in range(0,N):
        if (event.pos[0] - X[i])**2 + (event.pos[1] - Y[i])**2 <= R[i]**2:
            SCRW += 1
            R[i] = 0
            COLOR[i] = BLACK 
            V += 1
    for i in range(0,Nb):
        if (event.pos[0] - Xb[i] <= Sb and event.pos[1] - Yb[i] <= Sb and 
            event.pos[0] - Xb[i] >= 0 and event.pos[1] - Yb[i] >= 0 ):
            SCRW -= 1
            COLORb[i] = BLACK
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