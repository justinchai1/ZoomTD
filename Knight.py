import pygame
from ZoomGame import*
class Knight:
    speed=25
    health=175
    lives=1
    loot=50
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
        return Knight.speed
    def getHealth(self):
        return Knight.health
    def setHealth(self,health):
        Knight.health=health
    def getLivesMinus(self):
        return Knight.lives
    def getLoot(self):
        return Knight.loot
    def getImg(self):
        knightImg = pygame.image.load('knight.png').convert_alpha()
        knightImg = pygame.transform.scale(knightImg, (49, 49))
        return knightImg
    def getImg2(self):
        return 'knight.png'




