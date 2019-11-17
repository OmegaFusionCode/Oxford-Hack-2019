import random,math

from gameobjects import Floor
from materials import metal, stone, glass
from block import Block
from enemies import Enemy1, Enemy2


class LevelMaker(object):

    def __init__(self, screen, space, entities):
        self.screen = screen
        self.space = space
        self.entities = entities
        self.levels = [self.level1, self.level2, self.level3, self.level4, self.level5, self.level6, self.level7, self.level8, self.level9]
        random.shuffle(self.levels)

    def makeLevels(self, initialX, player):
        currentX = initialX
        for func in self.levels:
            currentX += func(currentX, player)

    def level1(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 900)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, stone())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, stone())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 200, 20, metal(),math.pi/2)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+310, 340), 200, 20, glass())
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+490, 340), 200, 20, glass())

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+400, 450), 200, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 60), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 500), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)

        return 900

    def level2(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 900)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal())
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal())
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal())
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+510, 120), 200, 20, metal())
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+200, 230), 200, 20, metal(), math.pi/2)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 200, 20, metal(), math.pi/2)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+600, 230), 200, 20, metal(), math.pi/2)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+110, 340), 200, 20, metal())
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+290, 340), 200, 20, metal())
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+510, 340), 200, 20, metal())
        blockUpper4 = Block(self.screen, self.space, self.entities, (initialX+690, 340), 200, 20, metal())

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+200, 450), 200, 20, metal(), math.pi/2)
        blockTop2 = Block(self.screen, self.space, self.entities, (initialX+600, 450), 200, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 280), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 60), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+600, 280), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)
        self.entities.append(blockBottom5)
        self.entities.append(blockBottom6)

        self.entities.append(blockMiddle1)
        self.entities.append(blockMiddle2)
        self.entities.append(blockMiddle3)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)
        self.entities.append(blockUpper3)
        self.entities.append(blockUpper4)

        self.entities.append(blockTop1)
        self.entities.append(blockTop2)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 900

    def level3(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 900)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal())
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal())
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal())
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+510, 120), 200, 20, metal())
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+200, 230), 200, 20, metal(), math.pi/2)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 200, 20, metal(), math.pi/2)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+600, 230), 200, 20, metal(), math.pi/2)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+310, 340), 200, 20, metal())
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+490, 340), 200, 20, metal())

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+400, 450), 200, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 60), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 60), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 280), player)
        enemy4 = Enemy1(self.screen, self.space, self.entities, (initialX+600, 60), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)
        self.entities.append(blockBottom5)
        self.entities.append(blockBottom6)

        self.entities.append(blockMiddle1)
        self.entities.append(blockMiddle2)
        self.entities.append(blockMiddle3)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)
        self.entities.append(enemy4)

        return 900

    def level4(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 900)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 220), 400, 20, metal())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 220), 400, 20, metal())
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+410, 120), 200, 20, metal())
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+590, 120), 200, 20, metal())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+500, 230), 200, 20, metal(), math.pi/2)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+410, 340), 200, 20, metal())
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+590, 340), 200, 20, metal())

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+200, 430), 200, 20, metal(), math.pi/2)
        blockTop2 = Block(self.screen, self.space, self.entities, (initialX+500, 450), 200, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 480), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+500, 60), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+500, 500), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)
        self.entities.append(blockTop2)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 900

    def level5(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 900)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal())
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+500, 120), 200, 20, metal())
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 600, 20, metal(), math.pi/2)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+310, 340), 200, 20, metal())
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+500, 340), 200, 20, metal())
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+690, 340), 200, 20, metal())

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+500, 450), 400, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+210, 60), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+405, 280), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+595, 60), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)
        self.entities.append(blockUpper3)

        self.entities.append(blockTop1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 900

    def level6(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 900)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+300, 120), 200, 20, metal())
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+300, 230), 400, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+205, 60), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+395, 60), player)
        enemy3 = Enemy2(self.screen, self.space, self.entities, (initialX+600, 60), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)

        self.entities.append(blockMiddle1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 900

    def level7(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 900)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 600, 20, metal(), math.pi/2)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+210, 340), 200, 20, metal())
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+590, 340), 200, 20, metal())

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+400, 450), 400, 20, metal(), math.pi/2)

        blockSky1 = Block(self.screen, self.space, self.entities, (initialX+310, 560), 200, 20, metal())
        blockSky2 = Block(self.screen, self.space, self.entities, (initialX+490, 560), 200, 20, metal())

        blockHeaven1 = Block(self.screen, self.space, self.entities, (initialX+400, 690), 200, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 60), player)
        enemy2 = Enemy2(self.screen, self.space, self.entities, (initialX+400, 280), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 500), player)
        enemy4 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 720), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)

        self.entities.append(blockSky1)
        self.entities.append(blockSky2)

        self.entities.append(blockHeaven1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)
        self.entities.append(enemy4)

        return 900

    def level8(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 1200)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+90, 120), 200, 20, metal())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+280, 120), 200, 20, metal())
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+470, 120), 200, 20, metal())
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+650, 120), 200, 20, metal())
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+840, 120), 200, 20, metal())
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+1030, 120), 200, 20, metal())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+280, 230), 400, 20, metal(), math.pi/2)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+840, 230), 200, 20, metal(), math.pi/2)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+560, 250), 400, 20, metal(), math.pi/2)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+110, 340), 200, 20, metal())
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+290, 340), 200, 20, metal())
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+830, 340), 200, 20, metal())
        blockUpper4 = Block(self.screen, self.space, self.entities, (initialX+1010, 340), 200, 20, metal())
        blockUpper5 = Block(self.screen, self.space, self.entities, (initialX+470, 360), 200, 20, metal())
        blockUpper6 = Block(self.screen, self.space, self.entities, (initialX+650, 360), 200, 20, metal())

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+200, 450), 200, 20, metal(), math.pi/2)
        blockTop2 = Block(self.screen, self.space, self.entities, (initialX+920, 450), 200, 20, metal(), math.pi/2)
        blockTop3 = Block(self.screen, self.space, self.entities, (initialX+560, 470), 200, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 280), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+920, 280), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+560, 300), player)
        enemy4 = Enemy2(self.screen, self.space, self.entities, (initialX+560, 60), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)
        self.entities.append(blockBottom5)
        self.entities.append(blockBottom6)

        self.entities.append(blockMiddle1)
        self.entities.append(blockMiddle2)
        self.entities.append(blockMiddle3)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)
        self.entities.append(blockUpper3)
        self.entities.append(blockUpper4)
        self.entities.append(blockUpper5)
        self.entities.append(blockUpper6)

        self.entities.append(blockTop1)
        self.entities.append(blockTop2)
        self.entities.append(blockTop3)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)
        self.entities.append(enemy4)

        return 1200

    def level9(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 900)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+250, 120), 200, 20, metal())
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+510, 120), 200, 20, metal())

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+380, 230), 600, 20, metal(), math.pi/2)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+90, 340), 200, 20, metal())
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+280, 340), 200, 20, metal())
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+480, 340), 200, 20, metal())
        blockUpper4 = Block(self.screen, self.space, self.entities, (initialX+670, 340), 200, 20, metal())

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+380, 450), 600, 20, metal(), math.pi/2)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 280), player)
        enemy2 = Enemy2(self.screen, self.space, self.entities, (initialX+380, 280), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+560, 280), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)
        self.entities.append(blockUpper3)
        self.entities.append(blockUpper4)

        self.entities.append(blockTop1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 900