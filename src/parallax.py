import pygame,sys,os

class BackgroundLayer:
    def __init__(self, screen, image, speed, height):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.height = height
        self.screen = screen
        self.image = pygame.image.load(os.path.join(dir_path, "background\\"+image)).convert_alpha()
        #self.image = pygame.transform.scale(self.image, (1800,900))
        self.pos = [0,1800]
        self.speed = speed

    def update(self):
        self.pos = [self.pos[0]-self.speed,self.pos[1]-self.speed]
        if self.pos[0]<=-1800:
            self.pos = [1800, self.pos[1]]
        if self.pos[1]<=-1800:
            self.pos = [self.pos[0], 1800]

    def draw(self):
        self.screen.blit(self.image, (self.pos[0], self.height))
        self.screen.blit(self.image, (self.pos[1], self.height))