import pygame
class UltraKnight:
    speed=10
    health=500
    lives=2
    loot=150
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
        return UltraKnight.speed
    def getHealth(self):
        return UltraKnight.health
    def getLivesMinus(self):
        return UltraKnight.lives
    def setHealth(self,health):
        UltraKnight.health=health
    def getLoot(self):
        return UltraKnight.loot
    def getImg(self):
        knightImg = pygame.image.load('ultraknight.png').convert_alpha()
        knightImg = pygame.transform.scale(knightImg, (49, 49))
        return knightImg
    def getImg2(self):
        return 'ultraknight.png'