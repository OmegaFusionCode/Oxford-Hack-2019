class Material(object):

    def __init__(self, density, texture, strength, breakType=0):
        """breakType specifies whether the material does nothing,
        shatters, or breaks into pieces when hit.
        """
        self.density = density
        self.texture = texture
        self.breakType = breakType

    def getMass(self, volume):
        mass = volume * self.density
        return mass
