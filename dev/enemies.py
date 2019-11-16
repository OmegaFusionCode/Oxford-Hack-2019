import math

import pygame
import pymunk
from pymunk.vec2d import Vec2d

from gameobjects import Entity


class Enemy(Entity):
    def __init__(self, screen, space, entities, pos, moment, shape, mass):
        super().__init__(screen, space, entities)
        self.body = pymunk.Body(mass, moment)
        self.body.position = pos
        self.x = pos[0]
        self.shape = shape
        self.shape.body = self.body
        self.space.add(self.body, self.shape)
        self.health = 100
    def takeDamage(self, damage):
        self.health = self.health - damage
        if(self.health) <= 0:
            self.die()
    def die(self):
        self.space.remove(self)
        self.entities.remove(self)
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.takeDamage(35)
class Enemy1(Enemy):
    def __init__(self, screen, space, entities, pos):
        mass = 10
        size = (50,30)
        moment = pymunk.moment_for_box(mass, size)
        shape = pymunk.Poly.create_box(None, size, 0)
        super().__init__(screen, space, entities, pos, moment, shape, mass)
        self.health = 100
