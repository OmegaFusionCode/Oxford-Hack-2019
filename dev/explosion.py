import pygame,functions,os
from gameobjects import Entity

class Explosion(Entity):
    def __init__(self, screen, pos):
        super().__init__(screen, space, entities)
        self.pos = pos
        self.index = 0
        self.screen = screen

    def update(self,dt):
        self.index+=0.25
        if self.index==9:
            self.remove()

    def draw(self):
        self.screen.blit(expSheet[int(self.index)], (200,200))

    def sidescroll(self):
        pass

expSheet = []
dir_path = os.path.dirname(os.path.realpath(__file__))
for i in range(1,9):
    x = (pygame.image.load(os.path.join(dir_path, "explosion_animation/tile"+str(i)+".png")).convert_alpha())
    x = pygame.transform.scale(x, (64,64))
    x = pygame.transform.scale(x, (128,128))
    expSheet.append(x)