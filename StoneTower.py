
import pygame
class StoneTower:
    range = 5
    attackspeed = 6
    cost = 75
    dmg = 50
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getRange(self):
        return StoneTower.range
    def getAASpeed(self):
        return StoneTower.attackspeed
    def getCost(self):
        return StoneTower.cost
    def getDmg(self):
        return StoneTower.dmg
    def getImg(self):
        knightImg = pygame.image.load('StoneTower.jpg').convert_alpha()
        knightImg = pygame.transform.scale(knightImg, (49, 49))
        return knightImg
    def getImg2(self):
        return 'StoneTower.jpg'