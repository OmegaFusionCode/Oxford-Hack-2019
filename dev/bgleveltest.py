import sys
import time
import math
import random
import os

import pygame
import pymunk
from pymunk.pygame_util import DrawOptions

from gameobjects import TargetLine, Character, Projectile, Floor
from materials import Material, metal, stone, glass
from block import Block
from levelmaker import LevelMaker
from parallax import BackgroundLayer


FRAMERATE = 60
INITIAL_X = 400

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
        self._setupCollisionHandlers()
        self._backgroundSetup()

    def _setupGeneral(self):
        self.entities = []
        self.count = 0
        self.dt = 0

    def _setupPygame(self, screenX, screenY, gameName):
        pygame.mixer.pre_init(22050, -16, 2, 512)
        pygame.mixer.init()
        pygame.init()
        pygame.display.set_mode((screenX, screenY))
        pygame.display.set_caption(gameName)
        self.screen = pygame.display.get_surface()
        self.screenX = screenX
        self.screenY = screenY
        self.options = DrawOptions(self.screen)
        self.clock = pygame.time.Clock()

        songs = ["sounds\music\drive_with_me_looped.wav","sounds\music\motivation_looped.wav"]

        dir_path = os.path.dirname(os.path.realpath(__file__))
        pygame.mixer.music.load(os.path.join(dir_path, random.choice(songs)))
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.35)

        
    def _setupSpace(self):
        self.space = pymunk.Space()
        self.space.gravity = 0, -1000

        player = Character(self.screen, self.space, self.entities, (100, 600))
        self.entities.append(player)
        self.entities.append(Floor(self.screen, self.space, self.entities, 0, 2*self.screen.get_width()))

    def _setupCollisionHandlers(self):

        def projectile_post_solve(arbiter, space, data):
            for shape in arbiter.shapes:
                if shape.collision_type == 1:
                    try:
                        self.entities.remove(shape.body.entity_ref)
                    except ValueError:
                        print("Exception Handled. list.remove(x): x not in list")
                        pass
                    self.space.remove(shape.body, shape)

        def enemy_projectile_begin(arbiter, space, data):
            return False

        self.enemyProjectileCollisionHandler = self.space.add_collision_handler(2,3)
        self.enemyProjectileCollisionHandler.begin = enemy_projectile_begin

        self.projectileCollisionHandler = self.space.add_wildcard_collision_handler(1)
        self.projectileCollisionHandler.post_solve = projectile_post_solve

    def _backgroundSetup(self):
        self.bg1 = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "background/bg.png")).convert_alpha()
        self.bgs = [BackgroundLayer(self.screen, "bg_mountains.png", 0.25, self.screen.get_size()[1]-800),
                    BackgroundLayer(self.screen, "bg_hills.png", 0.75, self.screen.get_size()[1]-500),
                    BackgroundLayer(self.screen, "bg_foreground.png", 1.5, self.screen.get_size()[1]-299)]

    @gameloop
    def gameLoop(self):
        self.dt = self.clock.tick(FRAMERATE) / 1000
        self.space.step(1/(2*FRAMERATE))
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
        for entity in self.entities:
            entity.sidescroll()
        for bg in self.bgs:
            bg.update()

    def _drawObjects(self):
        pygame.display.set_caption("FPS: " + str(self.clock.get_fps()))
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg1, (0,0))
        for bg in self.bgs:
            bg.draw()
        self.space.debug_draw(self.options)
        for entity in self.entities:
            entity.draw()
        pygame.display.flip()

    def run(self):
        self.gameLoop()
        pygame.quit()


if __name__ == "__main__":
    myWindow = GameWindow(1800, 900, "Test")
    myWindow.run()