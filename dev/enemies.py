import math
import os
import random

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
        self.body.entity_ref = self
        self.x = pos[0]
        self.shape = shape
        self.shape.friction = 0.8
        self.shape.collision_type = 4
        self.shape.body = self.body
        self.space.add(self.body, self.shape)
        self.health = health
        self.player = player
        self.alive = True
    def takeDamage(self, damage):
        self.health = self.health - damage
        dir_path = os.path.dirname(os.path.realpath(__file__))
        hitSound = pygame.mixer.Sound(os.path.join(dir_path, "sounds/sound_effects/turret_hit.wav"))
        hitSound.set_volume(0.3)
        pygame.mixer.Channel(3).play(hitSound)
        if self.health <= 0:
            self.die()
    def die(self):
        self.alive = False
        self.remove()
    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.takeDamage(35)
    def update(self, dt):
        if self.body.position[1] < -200:
            print("Enemy Despawned")
            self.die()

class Enemy1(Enemy):
    def __init__(self, screen, space, entities, pos, player):
        mass = 1000
        size = (160/2,132/2)
        moment = pymunk.moment_for_box(mass, size)
        shape = pymunk.Poly.create_box(None, size, 0)
        health = 100
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.bodyImg = pygame.image.load(os.path.join(dir_path, "turretBody.png")).convert_alpha()
        self.bodyImg = pygame.transform.scale(self.bodyImg, (128,128))

        self.gunImg = pygame.image.load(os.path.join(dir_path, "turret1Gun.png")).convert_alpha()
        self.gunImg = pygame.transform.scale(self.gunImg, (128,128))

        super().__init__(screen, space, entities, pos, moment, shape, mass, health, player)

        # Add the turret barrel as an attached entity
        self.barrel = Barrel(self.screen, self.space, self.entities, self, 0, math.pi)

        self.cooldown = random.uniform(1, 2.5)

    def update(self, dt):
        super().update(dt)
        if self.alive:
            self.barrel.baseX, self.barrel.baseY = functions.convert((self.body.position[0], self.body.position[1]))

            self.barrel.endX = self.barrel.baseX - (92/2) * math.cos(self.barrel.currAngle)
            self.barrel.endY = self.barrel.baseY + (92/2) * math.sin(self.barrel.currAngle)

            characterPos = functions.convert(self.player.body.position)

            self.barrel.delta_x = characterPos[0] - self.barrel.baseX
            self.barrel.delta_y = characterPos[1] - self.barrel.baseY
            self.barrel.currAngle = math.pi-(math.atan2(self.barrel.delta_y, self.barrel.delta_x) + (20*(math.pi/180)))


            if self.barrel.cooldown <= 0:
                self.barrel.createProjectile(0)
                self.barrel.cooldown = random.uniform(2, 2.75)
                dir_path = os.path.dirname(os.path.realpath(__file__))
                gunSound = pygame.mixer.Sound(os.path.join(dir_path, "sounds/sound_effects/Gun8.wav"))
                gunSound.set_volume(0.15)
                pygame.mixer.Channel(2).play(gunSound)
            self.barrel.cooldown -= dt
        else:
            self.remove()

    def draw(self):
        functions.rotate(self.screen, self.bodyImg, functions.convert(self.body.position),(132/2,192/2), math.degrees(self.body.angle))
        self.barrel.draw()

class Enemy2(Enemy):
    def __init__(self, screen, space, entities, pos, player):
        mass = 1000
        size = (160/2,132/2)
        moment = pymunk.moment_for_box(mass, size)
        shape = pymunk.Poly.create_box(None, size, 0)
        health = 100
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.bodyImg = pygame.image.load(os.path.join(dir_path, "turretBody.png")).convert_alpha()
        self.bodyImg = pygame.transform.scale(self.bodyImg, (128,128))

        self.gunImg = pygame.image.load(os.path.join(dir_path, "turret1Gun.png")).convert_alpha()
        self.gunImg = pygame.transform.scale(self.gunImg, (128,128))

        super().__init__(screen, space, entities, pos, moment, shape, mass, health, player)

        # Add the turret barrel as an attached entity
        self.barrel = Barrel(self.screen, self.space, self.entities, self, 0, math.pi)

    def update(self, dt):
        super().update(dt)
        if self.alive:
            self.barrel.baseX, self.barrel.baseY = functions.convert((self.body.position[0], self.body.position[1]))

            self.barrel.endX = self.barrel.baseX - (92/2) * math.cos(self.barrel.currAngle)
            self.barrel.endY = self.barrel.baseY + (92/2) * math.sin(self.barrel.currAngle)

            characterPos = functions.convert(self.player.body.position)

            self.barrel.delta_x = characterPos[0] - self.barrel.baseX
            self.barrel.delta_y = characterPos[1] - self.barrel.baseY
            self.barrel.currAngle = math.pi-(math.atan2(self.barrel.delta_y, self.barrel.delta_x) + (10*(math.pi/180)))

            if self.barrel.cooldown <= 0:
                self.barrel.createProjectile(1)
                self.barrel.cooldown = random.uniform(2, 2.5)
                dir_path = os.path.dirname(os.path.realpath(__file__))
                gunSound = pygame.mixer.Sound(os.path.join(dir_path, "sounds/sound_effects/Gun8.wav"))
                gunSound.set_volume(0.15)
                pygame.mixer.Channel(2).play(gunSound)
            self.barrel.cooldown -= dt
        else:
            self.remove()

    def draw(self):
        functions.rotate(self.screen, self.bodyImg, functions.convert(self.body.position),(132/2,192/2), math.degrees(self.body.angle))
        self.barrel.draw()

class Barrel(Entity):
    def __init__(self, screen, space, entities, parent, minAngle, maxAngle):
        super().__init__(screen, space, entities)
        self.parent = parent
        self.maxAngle = maxAngle
        self.minAngle = minAngle
        self.currAngle = (minAngle + maxAngle) / 2
        self.time = 0
        self.cooldown = 1.5
        self.update(0)
    def createProjectile(self,projectileType):
        if projectileType == 0:
            shotSpeed = 1500
            self.entities.append(Projectile(self.screen, self.space, self.entities, (self.endX, self.endY), shotSpeed, self.parent.body.velocity, math.pi-self.currAngle, 10, 250))
        elif projectileType == 1:
            shotSpeed = 2000
            self.entities.append(Projectile(self.screen, self.space, self.entities, (self.endX, self.endY), shotSpeed, self.parent.body.velocity, (math.pi-self.currAngle) + (5 * (math.pi/180)), 7, 250))
            self.entities.append(Projectile(self.screen, self.space, self.entities, (self.endX, self.endY), shotSpeed, self.parent.body.velocity, math.pi-self.currAngle, 7, 250))
            self.entities.append(Projectile(self.screen, self.space, self.entities, (self.endX, self.endY), shotSpeed, self.parent.body.velocity, (math.pi-self.currAngle) - (5 * (math.pi/180)), 7, 250))

    def update(self, dt):
        """
        if(self.parent.alive):
            currentPos = functions.convert(self.parent.body.position)
            characterPos = functions.convert(self.parent.player.body.position)

            self.baseX = currentPos[0]
            self.baseY = currentPos[1]
            self.targetX = characterPos[0]
            self.targetY = characterPos[1]

            self.delta_x = self.targetX - self.baseX
            self.delta_y = self.targetY - self.baseY
            self.currAngle = math.atan2(self.delta_y, self.delta_x) + (20*(math.pi/180))

            if self.cooldown <= 0:
                self.createProjectile()
                self.cooldown = 1.5
            self.cooldown -= dt
        else:
            self.remove()
        """

    def draw(self):
        functions.rotate(self.screen, self.parent.gunImg, (self.baseX, self.baseY),(116/2,192/2), math.degrees(self.currAngle))