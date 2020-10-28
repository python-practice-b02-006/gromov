import pygame as pg
import  numpy as np

pg.init()
FPS = 60
SCREEN_SIZE = (800,600)

class Gun():
    pass

class Target():
    pass

class Bullet():
    pass

class Manager():

    def process(self, events):
        done = self.event_handler(events)
        return done

    def event_handler(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        return done;


clock = pg.time.Clock()
done = False
screen = pg.display.set_mode(SCREEN_SIZE)
mgr = Manager()

while not done:
    clock.tick(FPS)
    done = mgr.process(pg.event.get())

pg.quit()

