import pygame
from pygame.draw import *
from numpy import *

def bird(x, y, k=1):
    '''
    draw a bird
    
    Parameters
    ----------
    x : intger
        x coordinate of a bird.
    y : integer
        y coordinate of a bird.
    k : float, optional
        size of a bird. The default is 1.

    Returns
    -------
    None.

    '''
    surface1 = pygame.Surface([int(32*k), int(8*k)], pygame.SRCALPHA)
    ellipse(surface1, BROWN, [0, 0, int(32*k), int(20*k)])
    surface1_rot = pygame.transform.rotate(surface1, -30)
    screen.blit(surface1_rot, [x - int(10.5*k), y])
    
    surface2 = pygame.Surface([int(32*k), int(8*k)], pygame.SRCALPHA)
    ellipse(surface2, BROWN, [0, 0, int(32*k), int(20*k)])
    surface2_rot = pygame.transform.rotate(surface2, 30)
    screen.blit(surface2_rot, [x + int(10.5*k), y])

ORANGE = (255, 160, 40)
PURPLE = (190, 70, 60)
PEACH = (255, 213, 170)
PURPLE_WHITE = (250, 214, 195)
YELLOW = (255, 255, 0)
VIOLET = (183, 131, 158)
DARK_VIOLET = (51, 0, 41)
BROWN = (51, 26, 0)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 600))

def back():
    '''
    set a background

    Returns
    -------
    None.

    '''
    rect(screen, PEACH, (0, 0, 900, 600)) 
    polygon(screen, PURPLE, [(0, 429), (0, 319), (155, 399), (197, 336), (261, 369),
                         (289, 290), (370, 309), (430, 354), (516, 335), (656, 265),
                         (693, 296),
                         (737, 336),
                         (775, 292), (814, 310), (830, 275), (869, 280), (900, 235),
                         (900, 429)])
    ellipse(screen, PURPLE, (555, 253, 733, 377))
    ellipse(screen, PEACH, (552, -339, 446, 657))
    rect(screen, PURPLE_WHITE, (0, 130, 900, 130))  # the sky stripe
    polygon(screen, PURPLE, [(746, 370), (737, 338), (775, 292), (814, 316),
                         (830, 289), (869, 293), (900, 241), (900, 429)])
    circle(screen, PURPLE, (614, 334), 63)

    surface = pygame.Surface([200, 100], pygame.SRCALPHA)
    ellipse(surface, PURPLE, [0, 0, 204, 80])
    surface_rot = pygame.transform.rotate(surface, 37)
    screen.blit(surface_rot, [470, 230])
 
    polygon(screen, ORANGE, [(5, 300), (12, 266), (143, 193), (185, 149),
                         (221, 156), (233, 175), (347, 251), (405, 242),
                         (439, 254), (481, 214), (522, 225), (541, 206),
                         (649, 134), (673, 139), (714, 177), (750, 168),
                         (809, 197), (838, 181), (900, 211)])
    ellipse(screen, PURPLE, (21, 264, 138, 309))

    ellipse(screen, PURPLE_WHITE, (437, -152, 219, 359))
    ellipse(screen, PURPLE_WHITE, (-274, -327, 500, 596))
    rect(screen, PEACH, (0, 0, 900, 129))
    circle(screen, YELLOW, (450, 120), int( 40*(2 + sin(x/50))))
    polygon(screen, ORANGE, [(5, 300), (12, 266), (143, 193), (185, 149),
                         (221, 156), (233, 175), (347, 251), (405, 242),
                         (439, 254), (481, 214), (522, 225), (541, 206),
                         (649, 134), (673, 139), (714, 177), (750, 168),
                         (809, 197), (838, 181), (900, 211)])
    polygon(screen, ORANGE, [(166, 168), (185, 149), (221, 156), (233, 175)])
    polygon(screen, ORANGE, [(673, 139), (714, 177), (655, 182)])
    ellipse(screen, ORANGE, (624, 125, 61, 103))
    ellipse(screen, ORANGE, (620, 130, 67, 96))
    ellipse(screen, ORANGE, (617, 137, 73, 73))
    ellipse(screen, ORANGE, (722, 173, 64, 53))

    polygon(screen, VIOLET, [(0, 420), (900, 400), (900, 600), (0, 600)])
    

    polygon(screen, DARK_VIOLET, [(0, 323), (105, 354), (193, 466), (283, 560),
                              (467, 575), (556, 509), (690, 547), (900, 396),
                             (900, 600), (0, 600)])

    ellipse(screen, VIOLET, (281, 514, 205, 75))

    surface = pygame.Surface([350, 130], pygame.SRCALPHA)
    ellipse(surface, VIOLET, [0, -340, 330, 438])
    screen.blit(surface, [517, 450])

    surface = pygame.Surface([350, 130], pygame.SRCALPHA)
    ellipse(surface, DARK_VIOLET, [0, 0, 170, 270])
    screen.blit(surface, [808, 377])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

x = 10
while not finished:
    clock.tick(10)
    back()
    bird(345, 216 + 100*sin(x/50))
    bird(427, 223 + 100*sin(x/50 + 23))
    bird(425, 253 + 100*sin(x/50 + 21))
    bird(357, 280 + 100*sin(x/50 + 10))
    bird(715, 433 + 100*sin(x/50 + 14))
    bird(614, 451 + 100*sin(x/50 + 112))
    bird(699, 482 + 100*sin(x/50 + 17), 1.5)
    bird(564, 406 + 100*sin(x/50 + 135), 1.3)

    x += 10

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
