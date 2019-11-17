import os, pygame

class Material(object):

    def __init__(self, texture, density, friction, strength, breakType=0, name):
        """breakType specifies whether the material does nothing,
        shatters, or breaks into pieces when hit.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.texture = pygame.image.load(os.path.join(dir_path, texture)).convert_alpha()
        self.density = density
        self.friction = friction
        self.strength = strength
        self.breakType = breakType

    def getMass(self, volume):
        mass = volume * self.density
        return mass

def metal():
    return Material("metal.png", 1.0, 0.9, 100)

def stone():
    return Material("", 0.8, 0.9, 50)

def glass():
    return Material("", 0.2, 0.9, 10)