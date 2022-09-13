import pygame
class MegaKnight:
    speed=5
    health=5000
    lives=3
    loot=300
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y
    def setAlive(self,alive):
        self.alive=alive
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getAliveStatus(self):
        return self.alive
    def getSpeed(self):
        return MegaKnight.speed
    def getHealth(self):
        return MegaKnight.health
    def getLivesMinus(self):
        return MegaKnight.lives
    def getLoot(self):
        return MegaKnight.loot
    def setHealth(self,health):
        MegaKnight.health=health
    def getImg(self):
        knightImg = pygame.image.load('MegaKnight.png').convert_alpha()
        knightImg = pygame.transform.scale(knightImg, (49, 49))
        return knightImg
    def getImg2(self):
        return 'MegaKnight.png'