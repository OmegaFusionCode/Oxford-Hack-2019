import random

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
        print(currentX)
        for func in self.levels:
            currentX += func(currentX)
            print(currentX)
    
    def level1(self, initialX):
        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+205, 70), 100, 10, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+295, 70), 100, 10, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+250, 125), 10, 100, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+205, 180), 100, 10, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+295, 180), 100, 10, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+250, 235), 10, 100, metal)


        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)

        return 500

    def level2(self, initialX):
        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+105, 70), 100, 10, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+195, 70), 100, 10, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+205, 70), 100, 10, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+295, 70), 100, 10, metal)
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+305, 70), 100, 10, metal)
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+395, 70), 100, 10, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+150, 125), 10, 100, metal)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+250, 125), 10, 100, metal)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+350, 125), 10, 100, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+105, 180), 100, 10, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+195, 180), 100, 10, metal)
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+305, 180), 100, 10, metal)
        blockUpper4 = Block(self.screen, self.space, self.entities, (initialX+395, 180), 100, 10, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+150, 235), 10, 100, metal)
        blockTop2 = Block(self.screen, self.space, self.entities, (initialX+350, 235), 10, 100, metal)


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

        return 500

    def level3(self, initialX):
        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+105, 70), 100, 10, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+195, 70), 100, 10, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+205, 70), 100, 10, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+295, 70), 100, 10, metal)
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+305, 70), 100, 10, metal)
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+395, 70), 100, 10, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+150, 125), 10, 100, metal)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+250, 125), 10, 100, metal)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+350, 125), 10, 100, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+205, 180), 100, 10, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+295, 180), 100, 10, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+250, 235), 10, 100, metal)


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

        return 500