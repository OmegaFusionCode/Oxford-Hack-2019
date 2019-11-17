import os, pygame

class Material(object):

    def __init__(self, texture, density, friction, strength, matType, breakType=0):
        """breakType specifies whether the material does nothing,
        shatters, or breaks into pieces when hit.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.texture = pygame.image.load(os.path.join(dir_path, texture)).convert_alpha()
        self.density = density
        self.friction = friction
        self.strength = strength
        self.breakType = breakType
        self.matType = matType

    def getMass(self, volume):
        mass = volume * self.density
        return mass

def metal():
    return Material("metal.png", 1.0, 0.9, 100, 0)

def stone():
    return Material("stone.png", 0.8, 0.9, 50, 1)

def glass():
    return Material("glass.png", 0.2, 0.9, 10, 2)