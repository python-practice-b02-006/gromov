import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (169, 176, 184), (0, 0, 400, 400), 0)
circle(screen, (255, 255, 51), (200, 200), 150)
line(screen, (0, 0, 0), (70, 60), (180, 150), 20)
circle (screen, (255, 0, 0), (150, 165), 25)
circle (screen, (0, 0, 0), (150, 165), 10)
line(screen, (0, 0, 0), (220, 150), (330, 90), 20)
circle (screen, (255, 0, 0), (250, 165), 20)
circle (screen, (0, 0, 0), (250, 165), 10)
rect(screen, (0, 0, 0), (120, 260, 160, 30), 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
