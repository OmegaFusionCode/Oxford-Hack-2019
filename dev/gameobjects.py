import math
import os

import pygame
import pymunk
from pymunk.vec2d import Vec2d

import functions

pygame.init()

dir_path = os.path.dirname(os.path.realpath(__file__))
playerBulletImg = pygame.image.load(os.path.join(dir_path, "playerBullet.png")).convert_alpha()
enemyBulletImg = pygame.image.load(os.path.join(dir_path, "enemyBullet.png")).convert_alpha()

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
        try:
            self.entities.remove(self)
        except:
            pass
        try:
            self.space.remove(self.body)
            self.space.remove(self.shape)
        except:
            pass

    def sidescroll(self):
        self.body.position = (self.body.position[0]-2, self.body.position[1])


class Character(Entity):

    def __init__(self, screen, space, entities, pos):
        super().__init__(screen, space, entities)
        mass = 1
        self.height = 150
        self.body = pymunk.Body(mass, pymunk.inf)
        self.body.entity_ref = self
        self.body.position = pos
        self.x = pos[0]
        self.shape = pymunk.Poly.create_box(self.body, (30,self.height), 5)
        self.space.add(self.body, self.shape)
        self.shape.collision_type = 5
        self.target = TargetLine(self.screen, self.space, self.entities, self, 122, -11/24 * math.pi, math.pi * 7/24)
        self.entities.append(self.target)
        self.thrusting = False
        self.imageIndex = 0
        self.maxVel = 1500
        self.minVel = -1000
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.gunSound = pygame.mixer.Sound(os.path.join(dir_path, "sounds/sound_effects/Gun9.wav"))
        self.gunSound.set_volume(0.10)
        self.health = 500.0

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.shldrImg = pygame.image.load(os.path.join(dir_path, 'playerShoulder.png'))
        self.shldrImg = pygame.transform.scale(self.shldrImg, (256,256))

        thrustImg1 = pygame.image.load(os.path.join(dir_path, 'body1.png'))
        thrustImg1 = pygame.transform.scale(thrustImg1, (256,256))
        thrustImg2 = pygame.image.load(os.path.join(dir_path, 'body2.png'))
        thrustImg2 = pygame.transform.scale(thrustImg2, (256,256))
        thrustImg3 = pygame.image.load(os.path.join(dir_path, 'body3.png'))
        thrustImg3 = pygame.transform.scale(thrustImg3, (256,256))
        self.sheetThrust = [thrustImg1, thrustImg2, thrustImg3, thrustImg2]

        idleImg1 = pygame.image.load(os.path.join(dir_path, 'idle1.png'))
        idleImg1 = pygame.transform.scale(idleImg1, (256,256))
        idleImg2 = pygame.image.load(os.path.join(dir_path, 'idle2.png'))
        idleImg2 = pygame.transform.scale(idleImg2, (256,256))
        self.sheetIdle = [idleImg1,idleImg2]

        self.armImg = pygame.image.load(os.path.join(dir_path, 'playerArm.png'))
        self.armImg = pygame.transform.scale(self.armImg, (256,256))


    def update(self, dt):
        self.body.position = (self.x, self.body.position[1])

        topOfScreen = False
        if self.body.position[1] > (self.screen.get_size()[1] - (self.height / 2)):
            # if character is about to reach the top of the screen
            self.body.position = (self.body.position[0], self.screen.get_size()[1] - (self.height / 2))
            topOfScreen = True

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.thrusting = True
            if not topOfScreen:
                self.body.apply_force_at_local_point(Vec2d(0,8000), self.body.center_of_gravity)
        else:
            self.thrusting = False
            self.body.apply_force_at_local_point(Vec2d(0,-5000), self.body.center_of_gravity)

        if self.body.velocity[1] > self.maxVel:
            self.body.velocity = (self.body.velocity[0], self.maxVel)
        elif self.body.velocity[1] < self.minVel:
            self.body.velocity = (self.body.velocity[0], self.minVel)

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("You were killed!")
        else:
            print("Your health was reduced to",round(self.health))

    def draw(self):
        x,y = functions.convert(self.body.position)
        if self.thrusting:
            self.imageIndex += 0.5
            self.screen.blit(self.sheetThrust[int(self.imageIndex%4)], (x-100, y-120))
            functions.rotate(self.screen, self.armImg, (x-4,y-24), (96,96), -math.degrees(self.target.currAngle))
        else:
            self.imageIndex += 0.25
            self.screen.blit(self.sheetIdle[int(self.imageIndex%2)], (x-100, y-120))
            functions.rotate(self.screen, self.armImg, (x-4,y-24), (96,96), -math.degrees(self.target.currAngle))

        self.screen.blit(self.shldrImg, (x-100, y-120))

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
        if pygame.mixer.get_init() == None:
            pygame.mixer.pre_init(44100, -16, 1, 512)
            pygame.mixer.init()
        pygame.mixer.Sound.play(self.parent.gunSound)
        self.entities.append(Projectile(self.screen, self.space, self.entities, (self.endX,self.endY), 4000, self.parent.body.velocity, self.currAngle, 10, 125, True))

    #def handleEvent(self, event):
    #    if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
    #        self.createProjectile()

    def update(self, dt):
        #if pygame.key.get_pressed()[pygame.K_s]:
        #    if self.currAngle < self.maxAngle:
        #        self.currAngle += math.pi / 48
        #if pygame.key.get_pressed()[pygame.K_w]:
        #    if self.currAngle > self.minAngle:
        #        self.currAngle -= math.pi / 48
        self.centreX, self.centreY = functions.convert((self.parent.body.position[0]-4,self.parent.body.position[1]+24))
        mouseX, mouseY = pygame.mouse.get_pos()
        try:
            angle = math.atan((mouseY-self.centreY) / (mouseX-self.centreX))
            if angle >= self.minAngle and angle <= self.maxAngle:
                self.currAngle = angle
            elif angle < self.minAngle:
                self.currAngle = self.minAngle
            else:
                self.currAngle = self.maxAngle
        except:
            angle = math.pi/2

        if pygame.mouse.get_pressed()[0] and self.cooldown <= 0:
            self.createProjectile()
            self.cooldown = 0.25
        self.cooldown -= dt
        self.endX = self.centreX + self.length*math.cos(self.currAngle+0.40489)
        self.endY = self.centreY + self.length*math.sin(self.currAngle+0.40489)

    def sidescroll(self):
        pass

    """
    def draw(self):
        pygame.draw.line(self.screen, (255,255,255), (self.centreX, self.centreY), (self.endX, self.endY))
    """

class Projectile(Entity):

    def __init__(self, screen, space, entities, pos, speed, parentVelocity, angle, radius, mass, friendly = False):
        self.mass = mass
        self.radius = radius
        super().__init__(screen, space, entities)
        self.body = pymunk.Body(self.mass, pymunk.moment_for_circle(self.mass, 0, radius))
        self.body.entity_ref = self
        self.body.position = functions.convert(pos)
        self.body.velocity = (speed*math.cos(angle), parentVelocity[1]-speed*math.sin(angle))

        self.shape = pymunk.Circle(self.body, radius)

        if friendly:
            self.shape.collision_type = 1
            self.image = playerBulletImg
        else:
            self.shape.collision_type = 2
            self.image = pygame.transform.scale(enemyBulletImg, (radius*2, radius*2))

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

    def draw(self):
        self.screen.blit(self.image, functions.convert((self.body.position[0]-self.radius, self.body.position[1] + self.radius)))


class Floor(Entity):

    def __init__(self, screen, space, entities, startX, length):
        super().__init__(screen, space, entities)
        self.shape = pymunk.Segment(self.space.static_body, (startX, 5), (startX+length, 5), 10)
        self.shape.elasticity = 0.2
        self.shape.friction = 0.8
        self.body = self.shape.body
        self.body.entity_ref = self
        self.body.position = (startX, 5)
        self.space.add(self.shape)

    def sidescroll(self):
        pass