import math

import pygame
import pymunk
from pymunk.vec2d import Vec2d

import functions



class Entity(object):

    def __init__(self, screen, space, entities):
        self.screen = screen
        self.space = space
        self.entities = entities

    def update(self, dt):
        pass

    def draw(self):
        pass

    def handleEvent(self, event):
        pass

    def remove(self):
        self.entities.remove(self)
        try:
            self.space.remove(self.body)
            self.space.remove(self.shape)
        except:
            pass


class Character(Entity):

    def __init__(self, screen, space, entities, pos):
        super().__init__(screen, space, entities)
        mass = 1
        self.body = pymunk.Body(mass, pymunk.inf)
        self.body.position = pos
        self.x = pos[0]
        self.shape = pymunk.Poly.create_box(self.body, (2,50), 10)
        self.space.add(self.body, self.shape)
        self.target = TargetLine(self.screen, self.space, self.entities, self, 75, -1 * math.pi, math.pi * 1/12)
        self.entities.append(self.target)


    def update(self, dt):
        self.body.position = (self.x, self.body.position[1])
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.body.apply_force_at_local_point(Vec2d(0,2000), self.body.center_of_gravity)


class TargetLine(Entity):

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

    #def handleEvent(self, event):
    #    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
    #        self.createProjectile()

    def update(self, dt):
        if pygame.key.get_pressed()[pygame.K_s]:
            if self.currAngle < self.maxAngle:
                self.currAngle += math.pi / 48
        if pygame.key.get_pressed()[pygame.K_w]:
            if self.currAngle > self.minAngle:
                self.currAngle -= math.pi / 48
        if pygame.mouse.get_pressed()[0] and self.cooldown <= 0:
            self.createProjectile()
            self.cooldown = 1
        self.cooldown -= dt
        self.centreX, self.centreY = functions.convert(self.parent.body.position)
        self.endX = self.centreX + self.length * math.cos(self.currAngle)
        self.endY = self.centreY + self.length * math.sin(self.currAngle)

    def draw(self):
        pygame.draw.line(self.screen, (255,255,255), (self.centreX, self.centreY), (self.endX, self.endY))


class Projectile(Entity):

    def __init__(self, screen, space, entities, pos, velocity, angle):
        super().__init__(screen, space, entities)
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 5))
        self.body.position = functions.convert(pos)
        self.body.velocity = (1000*math.cos(angle), velocity[1]-1000*math.sin(angle))

        self.shape = pymunk.Circle(self.body, 5)
        self.shape.collision_type = 1

        self.space = space
        self.space.add(self.body, self.shape)

#        self.coll_handler = self.space.add_wildcard_collision_handler(1)
#        self.coll_handler.begin = self.coll_begin

#        self.removed = False

    def coll_begin(self, arbiter, space, data):
        if not self.removed:
            self.removed = True
            self.remove()
        return True

    def update(self, dt):
        if self.body.position[0] < -5 or self.body.position[0] > self.screen.get_width() + 5 or self.body.position[1] < -5:
            self.remove()