import pygame as pg
import numpy as np
from random import *

pg.init()
pg.font.init()
FPS = 60
SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class Gun():

    def __init__(self):
        self.x = SCREEN_SIZE[0] / 2
        self.y = SCREEN_SIZE[1]
        self.size = 40
        self.r = 2 * self.size
        self.speed = 1
        self.dir = False
        self.active = False
        self.step_activ = False

    def draw_body(self):
        pg.draw.rect(screen, GREEN,
                     (int(self.x - self.size/2), int(self.y - self.size),
                      int(self.size),  int(self.size)), 0)

    def draw_huy(self):
        angle = np.arctan2((pg.mouse.get_pos()[0] - self.x), -pg.mouse.get_pos()[1] + SCREEN_SIZE[1] - 5*self.size/6)
        pg.draw.line(screen, GREEN, (int(self.x), int(self.y - 5*self.size/6)),
                     (int(self.x + np.sin(angle)*self.r), int(self.y - 5*self.size/6 - np.cos(angle)*self.r)), 5)

    def draw(self):
        self.draw_huy()
        self.draw_body()

    def strike(self):
        angle = np.arctan2((pg.mouse.get_pos()[0] - self.x), -pg.mouse.get_pos()[1] + SCREEN_SIZE[1] - 5*self.size/6)
        bullet = Bullet([int(self.x + np.sin(angle)*self.r), int(self.y - 5*self.size/6 - np.cos(angle)*self.r)],
                        [int(np.sin(angle)*self.speed), int(-np.cos(angle)*self.speed)])
        self.active = False
        self.speed = 1
        return bullet

    def activate(self):
        self.active = True

    def gain(self):
        if self.active:
            self.speed += 0.2
        if self.step_activ:
            if not self.dir and self.x < SCREEN_SIZE[0] - self.size/2:
                self.x += 1
            elif self.dir and self.x > self.size/2:
                self.x -= 1

    def move(self, dir):
        self.dir = dir
        self.step_activ = True

    def stop(self):
        self.step_activ = False


class Target:
    pass


class Bullet():

    def __init__(self, coord, vel, rad=20, color=None):
        self.coord = coord
        self.vel = vel
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True

    def move(self, grav = 0.2):
        self.vel[1] += grav
        for i in range(2):
            self.coord[i] += self.vel[i]

    def draw(self):
        pg.draw.circle(screen, self.color, list(map(int, self.coord)), self.rad)


class Manager():

    def __init__(self):
        self.gun = Gun()
        self.bullets = []

    def process(self, events):
        done = self.event_handler(events)

        self.draw()
        self.move()

        return done

    def event_handler(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.activate()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.bullets.append(self.gun.strike())
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.gun.move(False)
                elif event.key == pg.K_LEFT:
                    self.gun.move(True)
            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.gun.stop()
                elif event.key == pg.K_LEFT:
                    self.gun.stop()
        return done

    def draw(self):
        self.gun.draw()
        for bullet in self.bullets:
            bullet.draw()

    def move(self):
        self.gun.gain()
        for bullet in self.bullets:
            bullet.move()


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
