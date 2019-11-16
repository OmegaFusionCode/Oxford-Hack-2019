import math

import pygame
import pymunk
import functions

from pymunk.vec2d import Vec2d

from gameobjects import Entity, Projectile


class Enemy(Entity):
    def __init__(self, screen, space, entities, pos, moment, shape, mass, health, player):
        super().__init__(screen, space, entities)
        self.body = pymunk.Body(mass, moment)
        self.body.position = pos
        self.x = pos[0]
        self.shape = shape
        self.shape.body = self.body
        self.space.add(self.body, self.shape)
        self.health = health
        self.player = player
    def takeDamage(self, damage):
        self.health = self.health - damage
        if(self.health) <= 0:
            self.die()
    def die(self):
        # remove all attached entities then remove itself
        for entity in self.entities():
            entity.remove()
        self.remove()
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.takeDamage(35)
class Enemy1(Enemy):
    def __init__(self, screen, space, entities, pos, player):
        mass = 10
        size = (50,30)
        moment = pymunk.moment_for_box(mass, size)
        shape = pymunk.Poly.create_box(None, size, 0)
        health = 100
        super().__init__(screen, space, entities, pos, moment, shape, mass, health, player)

        # Add the turret barrel as an attached entity
        self.barrel = Barrel(self.screen, self.space, self.entities, self, 70, 0, math.pi)
        self.entities.append(self.barrel)

class Barrel(Entity):
    def __init__(self, screen, space, entities, parent, length, minAngle, maxAngle):
        super().__init__(screen, space, entities)
        self.parent = parent
        self.length = length
        self.maxAngle = maxAngle
        self.minAngle = minAngle
        self.currAngle = (minAngle + maxAngle) / 2
        self.time = 0
        self.cooldown = 0
        self.update(0)
    def createProjectile(self):
        self.entities.append(Projectile(self.screen, self.space, self.entities, (self.endX, self.endY), self.parent.body.velocity, self.currAngle))
    
    def update(self, dt):
        currentPos = functions.convert(self.parent.body.position)
        characterPos = functions.convert(self.parent.player.body.position)

        self.baseX = currentPos[0]
        self.baseY = currentPos[1]
        self.targetX = characterPos[0]
        self.targetY = characterPos[1]

        delta_x = self.targetX - self.baseX
        delta_y = self.targetY - self.baseY
        self.currAngle = math.atan2(delta_y, delta_x)

        print(self.currAngle * (180/math.pi))

        self.endX = self.baseX + self.length * math.cos(self.currAngle)
        self.endY = self.baseY + self.length * math.sin(self.currAngle)

        if self.cooldown <= 0:
            self.createProjectile()
            self.cooldown = 1
        self.cooldown -= dt

    def draw(self):
        pygame.draw.line(self.screen, (255,0,0), (self.baseX, self.baseY), (self.endX, self.endY))