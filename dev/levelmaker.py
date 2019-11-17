import random

from gameobjects import Floor
from materials import metal, stone, glass
from block import Block


class LevelMaker(object):

    def __init__(self, screen, space, entities):
        self.screen = screen
        self.space = space
        self.entities = entities
        self.levels = [self.level1, self.level2, self.level3]
        random.shuffle(self.levels)

    def makeLevels(self, initialX):
        currentX = initialX
        for func in self.levels:
            currentX += func(currentX)
    
    def level1(self, initialX):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 20, 200, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+310, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+490, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+400, 450), 20, 200, metal)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)

        return 800

    def level2(self, initialX):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal)
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+510, 120), 200, 20, metal)
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+200, 230), 20, 200, metal)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 20, 200, metal)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+600, 230), 20, 200, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+110, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+290, 340), 200, 20, metal)
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+510, 340), 200, 20, metal)
        blockUpper4 = Block(self.screen, self.space, self.entities, (initialX+690, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+200, 450), 20, 200, metal)
        blockTop2 = Block(self.screen, self.space, self.entities, (initialX+600, 450), 20, 200, metal)

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

        return 800

    def level3(self, initialX):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal)
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+510, 120), 200, 20, metal)
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+200, 230), 20, 200, metal)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 20, 200, metal)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+600, 230), 20, 200, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+310, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+490, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+400, 450), 20, 200, metal)

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

        return 800