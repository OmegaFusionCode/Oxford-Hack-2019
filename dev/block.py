import pymunk, pygame, math
import functions
import os
from gameobjects import Entity


class Block(Entity):

    def __init__(self, screen, space, entities, pos, height, width, material, angle=0):
        super().__init__(screen, space, entities)
        self.material = material
        self.height = height
        self.width = width
        self.mass = material.getMass(height * width)
        self.body = pymunk.Body(self.mass, pymunk.moment_for_box(self.mass, (width, height)))
        self.body.position = pos
        self.body.angle = angle
        self.body.entity_ref = self
        self.shape = pymunk.Poly.create_box(self.body, (width, height))
        self.shape.friction = material.friction
        self.shape.collision_type = 3
        self.health = material.strength

        self.texture = pygame.transform.scale(self.material.texture, (self.width, self.height))

        self.space.add(self.body, self.shape)

    def takeDamage(self, damage):
        self.health = self.health - damage

        soundString = ""
        if self.material.matType == 0:
            soundString = "metal_collision.wav"
        elif self.material.matType == 1:
            soundString = "stone_collision.wav"
        elif self.material.matType == 2:
            soundString = "glass_collision.wav"

        dir_path = os.path.dirname(os.path.realpath(__file__))
        ext_path = os.path.join(dir_path, "sounds/sound_effects")
        hitSound = pygame.mixer.Sound(os.path.join(ext_path, soundString))
        hitSound.set_volume(0.15)
        pygame.mixer.Channel(1).play(hitSound)

        if self.health <= 0:
            self.remove()

    def update(self, dt):
        if self.body.position[1] < -200:
            self.remove()
        if self.health <= 0:
            print("Block died")
            self.remove()

    def draw(self):
        functions.rotate(self.screen, self.texture, functions.convert(self.body.position), (9, self.height//2), math.degrees(self.body.angle))