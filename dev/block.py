import pymunk

from gameobjects import Entity


class Block(Entity):

    def __init__(self, screen, space, entities, pos, height, width, material):
        super().__init__(screen, space, entities)
        self.material = material
        self.height = height
        self.width = width
        self.mass = material.getMass(height * width)
        self.body = pymunk.Body(self.mass, pymunk.moment_for_box(self.mass, (width, height)))
        self.body.position = pos
        self.shape = pymunk.Poly.create_box(self.body, (width, height))

        self.space.add(self.body, self.shape)