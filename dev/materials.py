class Material(object):

    def __init__(self, texture, density, friction, strength, breakType=0):
        """breakType specifies whether the material does nothing,
        shatters, or breaks into pieces when hit.
        """
        self.texture = texture
        self.density = density
        self.friction = friction
        self.strength = strength
        self.breakType = breakType

    def getMass(self, volume):
        mass = volume * self.density
        return mass


metal = Material("", 1.0, 0.9, 100)
stone = Material("", 0.8, 0.9, 50)
glass = Material("", 0.2, 0.9, 10)