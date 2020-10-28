import pygame as pg
import numpy as np
import keyboard as kb

pg.init()
pg.font.init()
FPS = 60
SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


class Gun():

    def __init__(self):
        self.x = SCREEN_SIZE[0] / 2
        self.y = SCREEN_SIZE[1]
        self.size = 40
        self.r = 2 * self.size

    def draw_body(self):
        pg.draw.rect(screen, GREEN,
                     (int(self.x - self.size/2), int(self.y - self.size),
                      int(self.size),  int(self.size)), 0)

    def draw_huy(self):
        angle = np.arctan((pg.mouse.get_pos()[0] - self.x) / (-pg.mouse.get_pos()[1]+799))
        pg.draw.line(screen, GREEN, (int(self.x), int(self.y - 5*self.size/6)),
                     (int(self.x + np.sin(angle)*self.r),
                      int(self.y - np.cos(angle)*self.r)),
                     10)

    def draw(self):
        self.draw_huy()
        self.draw_body()


class Target:
    pass


class Bullet:
    pass


class Manager():

    def __init__(self):
        self.gun = Gun()

    def process(self, events):
        done = self.event_handler(events)

        self.gun.draw()

        return done

    def event_handler(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        return done


clock = pg.time.Clock()
DONE = False
screen = pg.display.set_mode(SCREEN_SIZE)
mgr = Manager()

while not DONE:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    DONE = mgr.process(pg.event.get())
    pg.display.flip()

pg.quit()
