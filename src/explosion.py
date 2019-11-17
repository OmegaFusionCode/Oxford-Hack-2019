import pygame,functions,os
from gameobjects import Entity
import functions

class Explosion(Entity):
    def __init__(self, screen, space, entities, pos):
        super().__init__(screen, space, entities)
        self.pos = functions.convert((pos[0]-96, pos[1]+96))
        self.index = 0
        self.screen = screen

    def update(self,dt):
        self.index+=0.25
        self.pos = (self.pos[0]-2, self.pos[1])

    def draw(self):
        try:
            self.screen.blit(expSheet[int(self.index)], self.pos)
        except IndexError:
            self.remove()

    def sidescroll(self):
        pass

expSheet = []
dir_path = os.path.dirname(os.path.realpath(__file__))
for i in range(1,9):
    x = (pygame.image.load(os.path.join(dir_path, "explosion_animation/tile"+str(i)+".png")).convert_alpha())
    x = pygame.transform.scale(x, (64,64))
    x = pygame.transform.scale(x, (128,128))
    expSheet.append(x)