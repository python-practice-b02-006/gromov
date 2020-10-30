import pygame as pg
import numpy as np
from random import *

pg.init()
pg.font.init()
FPS = 60
SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def rand_color():
    """
    set a random color
    Returns
    -------
    tuple(R,G,B)
    """
    return (randint(20, 255), randint(20, 255), randint(20, 255))


class Gun():
    """
    Gun class. Manages it's renderring, movement and striking.
    """

    def __init__(self):
        """
        Constructor method. Sets coordinate, direction, minimum and maximum power and color of the gun.
        """
        self.x = SCREEN_SIZE[0] / 2
        self.y = SCREEN_SIZE[1]
        self.size = 40
        self.r = 2 * self.size
        self.speed = 1
        self.speed_max = 30
        self.dir = False
        self.active = False
        self.step_active = False

    def draw_body(self):
        """
        Draw the body of the gun
        Returns
        -------
        None
        """
        pg.draw.rect(screen, GREEN,
                     (int(self.x - self.size / 2), int(self.y - self.size),
                      int(self.size), int(self.size)), 0)

    def draw_huy(self):
        """
        Draw the huy of the gun
        Returns
        -------
        None
        """
        angle = np.arctan2((pg.mouse.get_pos()[0] - self.x),
                           -pg.mouse.get_pos()[1] + SCREEN_SIZE[1] - 5 * self.size / 6)
        pg.draw.line(screen, GREEN, (int(self.x), int(self.y - 5 * self.size / 6)),
                     (int(self.x + np.sin(angle) * self.r), int(self.y - 5 * self.size / 6 - np.cos(angle) * self.r)),
                     5)

    def draw(self):
        """
        Draw the whole gun
        Returns
        -------
        None
        """
        self.draw_huy()
        self.draw_body()

    def strike(self):
        """
        Create a bullet according to actual position and power
        Returns
        -------
        Element of class Bullet
        """
        angle = np.arctan2((pg.mouse.get_pos()[0] - self.x),
                           -pg.mouse.get_pos()[1] + SCREEN_SIZE[1] - 5 * self.size / 6)
        bullet = Bullet(
            [int(self.x + np.sin(angle) * self.r), int(self.y - 5 * self.size / 6 - np.cos(angle) * self.r)],
            [int(np.sin(angle) * self.speed), int(-np.cos(angle) * self.speed)])
        self.active = False
        self.speed = 1
        return bullet

    def activate(self):
        """
        Make gun activated
        Returns
        -------
        None
        """
        self.active = True

    def gain(self):
        """
        Set the gun power
        Returns
        -------
        None
        """
        if self.active and self.speed <= self.speed_max:
            self.speed += 2 / self.speed
        if self.step_active:
            if not self.dir and self.x < SCREEN_SIZE[0] - self.size / 2:
                self.x += 1
            elif self.dir and self.x > self.size / 2:
                self.x -= 1

    def move(self, direct):
        """
        Control gan's movments
        Parameters
        ----------
        direct = bool (set a direction: True = Right)

        Returns
        -------
        None
        """
        self.dir = direct
        self.step_active = True

    def stop(self):
        """
        Make gun to stop
        Returns
        -------
        None
        """
        self.step_active = False


class Target():
    """
    Target class. Creates target, manages it's rendering and collision with a bullet event.
    """

    def __init__(self):
        """
        Constructor method. Sets coordinate, color and radius of the target.
        """
        self.size = 30
        self.dir = randint(0, 1)
        if self.dir == 0:
            self.x = 0 - 3 * randint(2, 5) * self.size
            self.speed = 3
        elif self.dir == 1:
            self.x = SCREEN_SIZE[0] + 3 * randint(2, 5) * self.size
            self.speed = -3
        self.y = 2 * randint(1, 6) * self.size
        self.color = rand_color()
        self.is_alive = True
        self.fired = False

    def move(self):
        """
        Control target's movements
        Returns
        -------
        None
        """
        self.x += self.speed
        if self.dir == 0:
            if self.x > SCREEN_SIZE[0] + 2 * self.size:
                self.is_alive = False
        elif self.dir == 1:
            if self.x < -2 * self.size:
                self.is_alive = False

    def draw(self):
        """
        Draw a target
        Returns
        -------
        None
        """
        pg.draw.rect(screen, self.color, (self.x, self.y, 2 * self.size, self.size), 0)

    def check_collision(self, bullet):
        """
        Control collision event
        Parameters
        ----------
        bullet = Bullet()

        Returns
        -------
        bool
        """
        if self.y + self.size > bullet.coord[1] > self.y and self.x + 2 * self.size > bullet.coord[0] > self.x:
            return True
        else:
            return False

    def strike(self, gun):
        """
        Control strike event
        Parameters
        ----------
        gun = Gun()

        Returns
        -------
        bool
        """
        if self.x + self.size / 2 <= gun.x + gun.size / 2 <= self.x + 3 * self.size / 2 and not self.fired:
            self.fired = True
            return True
        else:
            return False


class Bullet():
    """
    The bullet class. Creates a bullet, controls it's movement and implement it's rendering.
    """

    def __init__(self, coord, vel, rad=5, color=None):
        """
        Constructor method. Initializes bullet's parameters and initial values.
        """
        self.coord = coord
        self.vel = vel
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True

    def move(self, grav):
        """
        Control bullet's movments
        Parameters
        ----------
        grav = float

        Returns
        -------
        None
        """
        self.vel[1] += grav
        for i in range(2):
            self.coord[i] += self.vel[i]
        if self.coord[0] > SCREEN_SIZE[0] + self.rad \
                or self.coord[0] < -1 * self.rad \
                or self.coord[1] > SCREEN_SIZE[1] + self.rad \
                or self.coord[1] < -1 * self.rad:
            self.is_alive = False

    def draw(self):
        """
        Draw a bullet
        Returns
        -------
        None
        """
        pg.draw.circle(screen, self.color, list(map(int, self.coord)), self.rad)


class Bomb():
    """
    The bomb class. Creates a bomb, controls it's movement and implement it's rendering.
    """

    def __init__(self, y, x, speed):
        """
        Constructor method. Initializes bomb's parameters and initial values.
        """
        self.size = 20
        self.y = y
        self.speed = speed
        self.x = x
        self.is_alive = True

    def move(self):
        """
        Control bomb's movements
        Returns
        -------
        None
        """
        self.y += self.speed
        if self.y > SCREEN_SIZE[1]:
            self.is_alive = False

    def draw(self):
        """
        Draw a bomb
        Returns
        -------
        None
        """
        pg.draw.rect(screen, RED, (int(self.x) - int(3 * self.size / 2),
                                   int(self.y), int(self.size), int(self.size)), 0)

    def check_collision(self, gun):
        """
        Check a collision event
        Parameters
        ----------
        gun = Gun

        Returns
        -------
        bool
        """
        if self.y + self.size > gun.y - gun.size \
                and (self.x - self.size / 2 > gun.x - gun.size / 2
                     and gun.x + gun.size / 2 > self.x - 3 * self.size / 2):
            return True
        else:
            return False


class ScoreTable():
    """
    Score table class
    """

    def __init__(self, t_destr=0, lives=5):
        """
        Set initial scores and lives
        """
        self.t_destr = t_destr
        self.lives = lives
        self.font = pg.font.SysFont("dejavusansmono", 25)

    def score(self):
        return self.t_destr

    def draw(self, pow):
        """
        Print scores, lives, power
        Parameters
        ----------
        pow = int (the gun power)

        Returns
        -------
        None
        """
        pg.draw.rect(screen, BLACK, (SCREEN_SIZE[0], 0, 150, SCREEN_SIZE[1]), 0)
        pg.draw.line(screen, WHITE, (SCREEN_SIZE[0], 0), (SCREEN_SIZE[0], SCREEN_SIZE[1]), 5)
        score_surf = []
        score_surf.append(self.font.render("Destroyed: {}".format(self.t_destr), True, WHITE))
        score_surf.append(self.font.render("Lives: {}".format(self.lives), True, RED))
        for i in range(2):
            screen.blit(score_surf[i], [810, 10 + 30 * i])
        for i in range(int(pow)):
            pg.draw.rect(screen, RED, (SCREEN_SIZE[0] + 70, 550 - 15 * i, 10, 10), 0)
        screen.blit((self.font.render("POWER".format(self.t_destr), True, WHITE)), [845, 570])

    def loose(self):
        """
        Print final message
        Returns
        -------
        None
        """
        self.font = pg.font.SysFont("dejavusansmono", 100)
        screen.blit((self.font.render("YOU LOSE".format(self.t_destr), True, WHITE)), [300, 250])


class Manager():
    """
    Control all events and objects
    """

    def __init__(self):
        """
        Initialize objects and necessary variables
        """
        self.gun = Gun()
        self.bullets = []
        self.targets = []
        self.n_targets = 4
        self.bombs = []
        self.table = ScoreTable()
        self.grav = 0.3
        self.b_spd = 3

    def new_mission(self):
        """
        Start a new mission
        Returns
        -------
        None
        """
        for i in range(self.n_targets):
            self.targets.append(Target())

    def process(self, events):
        """
        Rule process
        Parameters
        ----------
        events = pg.event

        Returns
        -------
        bool
        """
        done = self.event_handler(events)
        self.draw()
        self.move()
        self.collide()
        if len(self.targets) == 0:
            self.new_mission()
        return done

    def event_handler(self, events):
        """
        Read events
        Parameters
        ----------
        events = pg.event

        Returns
        -------
        bool
        """
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
        """
        Draw all objects
        Returns
        -------
        None
        """
        self.gun.draw()
        for bullet in self.bullets:
            bullet.draw()
        for target in self.targets:
            target.draw()
        for bomb in self.bombs:
            bomb.draw()
        self.table.draw(self.gun.speed)

    def move(self):
        """
        Move all objects
        Returns
        -------
        None
        """
        self.gun.gain()
        dead_bullets = []
        for i, bullet in enumerate(self.bullets):
            bullet.move(self.grav)
            if not bullet.is_alive:
                dead_bullets.append(i)
        for i in reversed(dead_bullets):
            self.bullets.pop(i)
        dead_targets = []
        for i, target in enumerate(self.targets):
            target.move()
            if target.strike(self.gun):
                self.bombs.append(Bomb(target.y + target.size, target.x + target.size, self.b_spd))
            if not target.is_alive:
                dead_targets.append(i)
        for i in reversed(dead_targets):
            self.targets.pop(i)
        dead_bombs = []
        for i, bomb in enumerate(self.bombs):
            bomb.move()
            if not bomb.is_alive:
                dead_bombs.append(i)
        for i in reversed(dead_bombs):
            self.bombs.pop(i)

    def collide(self):
        """
        Check interactions between objects. Finish the game if you lose
        Returns
        -------
        None
        """
        collisions = []
        targets_c = []
        for i, bullet in enumerate(self.bullets):
            for j, target in enumerate(self.targets):
                if target.check_collision(bullet):
                    collisions.append([i, j])
                    targets_c.append(j)
        targets_c.sort()
        for j in reversed(targets_c):
            self.targets.pop(j)
            self.table.t_destr += 1
            self.b_spd += 0.3
        bombs_c = []
        for i, bomb in enumerate(self.bombs):
            if bomb.check_collision(self.gun):
                bombs_c.append(i)
        for i in reversed(bombs_c):
            self.bombs.pop(i)
            self.table.lives -= 1
            if self.table.lives == 0:
                screen.fill(BLACK)
                self.table.loose()
                pg.display.flip()
                pg.time.wait(2000)
                pg.quit()


clock = pg.time.Clock()
DONE = False
screen = pg.display.set_mode((SCREEN_SIZE[0] + 150, SCREEN_SIZE[1]))
mgr = Manager()

while not DONE:  # the main cycle of the program
    clock.tick(FPS)
    if pg.get_init():
        screen.fill(BLACK)
        DONE = mgr.process(pg.event.get())
    if pg.get_init():
        pg.display.flip()

pg.quit()
