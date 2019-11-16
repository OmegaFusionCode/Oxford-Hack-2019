import sys
import time
import math
import random

import pygame
import pymunk
from pymunk.pygame_util import DrawOptions

from gameobjects import TargetLine, Character, Projectile, Floor
from materials import Material, metal, stone, glass
from block import Block
from levelmaker import LevelMaker


FRAMERATE = 30
INITIAL_X = 0


def gameloop(func):
    def wrapper(*args, **kwargs):
        while True:
            func(*args, **kwargs)
    return wrapper



class GameWindow(object):

    def __init__(self, screenX, screenY, gameName):
        self._setupGeneral()
        self._setupPygame(screenX, screenY, gameName)
        self._setupSpace()

    def _setupGeneral(self):
        self.entities = []
        self.count = 0
        self.dt = 0

    def _setupPygame(self, screenX, screenY, gameName):
        pygame.init()
        pygame.display.set_mode((screenX, screenY))
        pygame.display.set_caption(gameName)
        self.screen = pygame.display.get_surface()
        self.screenX = screenX
        self.screenY = screenY
        self.options = DrawOptions(self.screen)
        self.clock = pygame.time.Clock()
    
    def _setupSpace(self):
        self.space = pymunk.Space()
        self.space.gravity = 0, -1000

        #self.entities.append(Character(self.screen, self.space, self.entities, (100, 600)))
        self.entities.append(Floor(self.screen, self.space, self.entities, 0, self.screen.get_width()))

        # Make the level parts

        LevelMaker(self.screen, self.space, self.entities).makeLevels(INITIAL_X)

        #self.floor = pymunk.Segment(self.space.static_body, (0, 5), (self.screenX, 5), 10)
        #self.floor.body.position = 0, 5
        #self.floor.elasticity = 0.2
        #self.floor.friction = 0.2

        #self.space.add(self.floor)

    @gameloop
    def gameLoop(self):
        self.dt = self.clock.tick(FRAMERATE) / 1000
        self.space.step(1/60)
        self._handleEvents()
        self._executeLogic()
        self._drawObjects()

    def _handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for entity in self.entities:
                entity.handleEvent(event)

    def _executeLogic(self):
        for entity in self.entities:
            entity.update(self.dt)

    def _drawObjects(self):
        self.screen.fill((0,0,0))
        self.space.debug_draw(self.options)
        for entity in self.entities:
            entity.draw()
        pygame.display.flip()

    def run(self):
        self.gameLoop()
        pygame.quit()


if __name__ == "__main__":
    myWindow = GameWindow(1500, 500, "Test")
    myWindow.run()