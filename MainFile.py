import pygame
from Knight import *
from MegaKnight import *
from UltraKnight import *
from ZoomGame import *
from StoneTower import *


class Mon(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, health):
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([50, 50])
        self.image.fill(black)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speed = speed
        self.health = health

    def update(self, *args):
        if self.rect.x <= 150 and self.rect.y == 650:
            self.rect.x += self.speed
        if self.rect.x == 150 and self.rect.y >= 100:
            self.rect.y -= self.speed
        if self.rect.x <= 300 and self.rect.y == 100:
            self.rect.x += self.speed
        if self.rect.x == 300 and self.rect.y <= 750:
            self.rect.y += self.speed
        if self.rect.x < 450 and self.rect.y == 750:
            self.rect.x += self.speed
        if self.rect.x == 450 and self.rect.y >= 50:
            self.rect.y -= self.speed
        if self.rect.x <= 600 and self.rect.y == 50:
            self.rect.x += self.speed
        if self.rect.x == 600 and self.rect.y <= 750:
            self.rect.y += self.speed
        if self.rect.x <= 800 and self.rect.y == 750:
            self.rect.x += self.speed
        if self.rect.x == 800 and self.rect.y >= 150:
            self.rect.y -= self.speed
        if self.rect.x >= 800 and self.rect.x <= 1000 and self.rect.y == 150:
            self.rect.x += self.speed
        if self.rect.x == 1000 and self.rect.y <= 750:
            self.rect.y += self.speed
        if self.rect.x >= 1000 and self.rect.x <= 1300 and self.rect.y == 750:
            self.rect.x += self.speed
        if self.rect.x == 1300 and self.rect.y >= 600:
            self.rect.y -= self.speed
        if self.rect.x >= 1100 and self.rect.y == 600:
            self.rect.x -= self.speed
        if self.rect.x == 1100 and self.rect.y >= 450 and self.rect.y <= 600:
            self.rect.y -= self.speed
        if self.rect.x >= 1100 and self.rect.x <= 1250 and self.rect.y == 450:
            self.rect.x += self.speed
        if self.rect.x == 1250 and self.rect.y >= 250 and self.rect.y <= 450:
            self.rect.y -= self.speed
        if self.rect.x >= 1250 and self.rect.x <= 1350 and self.rect.y == 250:
            self.rect.x += self.speed
        if self.rect.x == 1350 and self.rect.y == 250:
            self.rect.x = 2000
            self.rect.y = 2000

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y


class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed):
        # pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface([width, height])

        # this rect determinies the position the ball is drawn
        # self.rect = self.image.get_rect()

        # Draw the ellipse onto the surface
        # pygame.draw.ellipse(self.image,  (234, 18, 18), [0, 0, width, height], 3)

        super().__init__()

        # Set height, width
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.speed = speed
        # Make our top-left corner the passed-in location.

        self.rect.y = y
        self.rect.x = x

    def getAASpeed(self):
        return self.speed
    def getcolli(self):
        print()

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)

RED = (234, 18, 18)
display_width = 1500
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SquareGang Defense')
gameDisplay.fill(white)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)
clock = pygame.time.Clock()
crashed = False

carImg = pygame.image.load('grass.jpg')
carImg = pygame.transform.scale(carImg, (49, 49))
dirtImg = pygame.image.load('Dirt.png')
dirtImg = pygame.transform.scale(dirtImg, (49, 49))
startImg = pygame.image.load('start.png')
startImg = pygame.transform.scale(startImg, (49, 49))
endImg = pygame.image.load('end.png')
endImg = pygame.transform.scale(endImg, (49, 49))
stonetowerImg = pygame.image.load('StoneTower.jpg').convert()
stonetowerImg = pygame.transform.scale(stonetowerImg, (49, 49))
knightImg = pygame.image.load('knight.png').convert_alpha()
knightImg = pygame.transform.scale(knightImg, (49, 49))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def dirt(x, y):
    gameDisplay.blit(dirtImg, (x, y))


def startTile(x, y):
    gameDisplay.blit(startImg, (x, y))


def endTile(x, y):
    gameDisplay.blit(endImg, (x, y))


def Stoney(x, y):
    gameDisplay.blit(stonetowerImg, (x, y))


def drawColLine(c):
    pygame.draw.aaline(gameDisplay, black, [c * 50, 0], [c * 50, 900], 1)


def drawRowLine(r):
    pygame.draw.aaline(gameDisplay, black, [0, r * 50], [1400, r * 50], 1)


def makeLvl(level):
    monster = []

    if level <= 100:
        for x in range(level):
            k1 = Knight(x * -200, 650, True)
            monster.append(k1)
    if level % 2 == 0:
        for x in range(level // 2):
            uk1 = UltraKnight(x * -100, 650, True)
            monster.append(uk1)
    if level % 5 == 0:
        for x in range(level // 5):
            mk1 = MegaKnight(x * -20, 650, True)
            monster.append(mk1)
    return monster


def makeSprite(level):
    monster = makeLvl(level)

    m = []
    for x in range(len(monster)):
        m.append(Mon(monster[x].getX(), monster[x].getY(), monster[x].getSpeed(), monster[x].getHealth()))
        all_sprite_list.add(Mon(monster[x].getX(), monster[x].getY(), monster[x].getSpeed(), monster[x].getHealth()))
    print(len(m))
    return m


counter = 0
q = 0
w = 650
b = 0
a = 0
bob = False
held = False
col = 0
row = 0
towers = []
m = pygame.mouse.get_pos()
nut = False
level = 2
money = 500
tr = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
km = makeSprite(level)


def colld(sprite, group, villians, ttv):
    if pygame.sprite.spritecollideany(sprite, group, collided=None):
       # print("boom")
        return True
    return False


def collide(sprite, group, villians, ttv):
    #print(pygame.sprite.collide_rect(sprite, ttv[0]))
    if pygame.sprite.spritecollideany(sprite, group, collided=None):
        print(group.sprites()[0].getAASpeed())
        for x in range(len(villians)):

            # print(sprite.getX()>= monster[x].getX() and sprite.getX()<= monster[x].getX()+50 and sprite.getY()>=monster[x].getY() and sprite.getY()<=monster[x].getY()+50)
            if (sprite.getX() + 25 >= villians[x].getX() and sprite.getX() + 25 <= villians[x].getX() + 50) and (
                    sprite.getY() + 25 >= villians[x].getY() and sprite.getY() + 25 <= villians[x].getY() + 50):

                villians[x].setHealth(villians[x].getHealth() - 50)
                print(villians[x].getHealth())
                if villians[x].getHealth() <= 0:
                    villians[x].setAlive(False)


# MAKEs THE MAGIC HAPPEN
while not crashed:
    clock = pygame.time.Clock()
    m = pygame.mouse.get_pos()
    # print(m[0],m[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if pygame.mouse.get_pressed()[0] and m[0] > 150 and m[0] < 200 and m[1] > 910 and m[1] < 960:
            # print(event.pos)
            held = True
        elif event.type == pygame.MOUSEBUTTONUP and held == True and event.button == 1 and m[0] > 0 and m[0] < 1400 and \
                m[1] > 0 and m[1] < 900:

            a = event.pos[0] // 50

            b = event.pos[1] // 50

            held = False

            if path[b][a] == 0:
                bob = True
            else:
                bob = False
    if (held == True):
        pygame.draw.circle(gameDisplay, black, [m[0], m[1]], 100, 3)
        Stoney(m[0] - 25, m[1] - 25)

    if bob == True:
        # stoneTower(a * 50, b * 50)
        # circle = pygame.draw.circle(gameDisplay, black, [a*50+25, b*50+25], 100, 3)

        kkk = StoneTower(a * 50, b * 50)
        towers.append(kkk)
        money -= kkk.getCost()
        t1 = Tower(a * 50 - 75, b * 50 - 75, 200, 200, kkk.getAASpeed())

        tr.add(t1)
        all_sprite_list.add(t1)
        bob = False

    for x in range(len(towers)):
        Stoney(towers[x].getX(), towers[x].getY())
    # enemies movemenet down here

    if nut == False:
        monster = makeLvl(level)
        km = makeSprite(level)
        nut = True

    for x in range(len(monster)):

        if monster[x].getX() <= 150 and monster[x].getY() == 650:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 150 and monster[x].getY() >= 100:
            monster[x].setY(monster[x].getY() - monster[x].getSpeed())
        if monster[x].getX() <= 300 and monster[x].getY() == 100:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 300 and monster[x].getY() <= 750:
            monster[x].setY(monster[x].getY() + monster[x].getSpeed())
        if monster[x].getX() < 450 and monster[x].getY() == 750:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 450 and monster[x].getY() >= 50:
            monster[x].setY(monster[x].getY() - monster[x].getSpeed())
        if monster[x].getX() <= 600 and monster[x].getY() == 50:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 600 and monster[x].getY() <= 750:
            monster[x].setY(monster[x].getY() + monster[x].getSpeed())
        if monster[x].getX() <= 800 and monster[x].getY() == 750:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 800 and monster[x].getY() >= 150:
            monster[x].setY(monster[x].getY() - monster[x].getSpeed())
        if monster[x].getX() >= 800 and monster[x].getX() <= 1000 and monster[x].getY() == 150:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 1000 and monster[x].getY() <= 750:
            monster[x].setY(monster[x].getY() + monster[x].getSpeed())
        if monster[x].getX() >= 1000 and monster[x].getX() <= 1300 and monster[x].getY() == 750:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 1300 and monster[x].getY() >= 600:
            monster[x].setY(monster[x].getY() - monster[x].getSpeed())
        if monster[x].getX() >= 1100 and monster[x].getY() == 600:
            monster[x].setX(monster[x].getX() - monster[x].getSpeed())
        if monster[x].getX() == 1100 and monster[x].getY() >= 450 and monster[x].getY() <= 600:
            monster[x].setY(monster[x].getY() - monster[x].getSpeed())
        if monster[x].getX() >= 1100 and monster[x].getX() <= 1250 and monster[x].getY() == 450:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 1250 and monster[x].getY() >= 250 and monster[x].getY() <= 450:
            monster[x].setY(monster[x].getY() - monster[x].getSpeed())
        if monster[x].getX() >= 1250 and monster[x].getX() <= 1350 and monster[x].getY() == 250:
            monster[x].setX(monster[x].getX() + monster[x].getSpeed())
        if monster[x].getX() == 1350 and monster[x].getY() == 250:
            monster[x].setX(2000)
            monster[x].setY(2000)
            lives -= monster[x].getLivesMinus()
        gameDisplay.blit(monster[x].getImg(), (monster[x].getX(), monster[x].getY()))
    if monster[len(monster) - 1].getX() == 2000 and monster[len(monster) - 1].getY() == 2000:
        level += 1
        nut = False
        km.clear()
        pygame.time.wait(800)

    for p in range(len(km)):
        # print(counter)
        if colld(km[p], tr, monster, towers) == True and counter % 8 == 0:
            collide(km[p], tr, monster, towers)

    counter += 1

    for x in range(len(monster)):

        if monster[x].getAliveStatus() == False:
            monster[x].setX(2000)
            monster[x].setY(2000)

    for q in range(len(km)):
        km[q].update()
        # km[q].draw(gameDisplay)
    tr.update()
    all_sprite_list.update()
    # tr.draw(gameDisplay)

    pygame.display.flip()
    clock.tick(120)
    # MAKES THE BOARD
    for c in range(0, 28):
        drawColLine(c)
    for r in range(0, 18):
        drawRowLine(r)
    for r in range(0, 18):
        for c in range(0, 28):
            if path[r][c] == 0:
                car(c * 50 + 1, r * 50 + 1)
            elif path[r][c] == 1:
                dirt(c * 50 + 1, r * 50 + 1)
            elif path[r][c] == 2:
                startTile(c * 50 + 1, r * 50 + 1)
            elif path[r][c] == 3:
                endTile(c * 50 + 1, r * 50 + 1)
    pygame.draw.rect(gameDisplay, RED, [0, 900, 1500, 100])
    pygame.draw.rect(gameDisplay, RED, [1400, 0, 100, 1000])
    dislives = myfont.render("Lives:" + str(lives), False, (0, 0, 0))
    gameDisplay.blit(dislives, (1405, 50))
    dislevel = myfont.render("Level:" + str(level), False, (0, 0, 0))
    gameDisplay.blit(dislevel, (1405, 100))
    dismoney = myfont.render("Clout:" + str(money), False, (0, 0, 0))
    gameDisplay.blit(dismoney, (1405, 150))
    for p in range(len(km)):
        # print(counter)
        if colld(km[p], tr, monster, towers) == True and counter % 8 == 0:
            pygame.draw.aaline(gameDisplay, RED, [km[p].getX(), km[p].getY()], [towers[0].getX(), towers[0].getY()], 10)
    Stoney(150, 910)
pygame.quit()
quit()