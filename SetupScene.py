import pygame
import DrawScript as DS
import PhysicsScript as PS
import ColliderScript as CS
import Components as COMP
from spritesheet_functions import SpriteSheet
name = "scene"
listObject = []
listPlatformCollider = pygame.sprite.Group()
listDraw = pygame.sprite.Group()
listEnemy = []
# basicfont = pygame.font.SysFont(None, 40)
darkGreen = (0, 200, 0)
WHITE = (255, 255, 255)
brightGreen = (0, 255, 0)
boardColor = (244, 66, 95)
lightGreen = (107, 244, 65)
RED = (255, 0, 0)
playerImage = pygame.image.load("cavemanSprite.jpg").convert()
alien = pygame.image.load("alien.gif")
playerImage.set_colorkey(WHITE)
playerObject = ()

playerPhy = ()


def LoadLevel():
    # set transform
    AddPlayer()
    # append(Info.GetComponent("ColliderComponent"))
    AddObject()


def AddObject():
    global listDraw
    global listPlatformCollider
    global listEnemy
    # add the ground
    Info1 = COMP.GameObject(playerImage, 20, 20)
    Info1.transform = COMP.Transform()
    Info1.transform.location = [0, 500]

    # Info1.listComp.append(DS.DrawComponent([0, (RED, [800, 120])]))
    Info1.listComp.append(CS.ColliderComponent((0, [0, 0, 500, 120])))

    # create a circle object
    Info2 = COMP.GameObject(WHITE, 20, 20)
    Info2.transform = COMP.Transform()
    Info2.transform.location = [650, 380]
    # Info1.listComp.append(PS.PhysicsComponent([0, [0, 0], 0.1], "player"))
    Info2.listComp.append(DS.DrawComponent([2, (alien, 25)]))
    Info2.listComp.append(CS.ColliderComponent((0, [0, 0, 20, 30])))
    listDraw.add(Info1)
    listDraw.add(Info2)
    listPlatformCollider.add(Info1)
    listEnemy.append(Info2)


def AddPlayer():
    global playerPhy
    global playerObject
    global listObject
    tran = COMP.Transform()
    tran.location = [0, 300]
    dInfo = DS.DrawComponent([2, (playerImage, [20, 20])])
    pInfo = PS.PhysicsComponent([1, [0, 0], [0, 0], 0.01], "platform")
    cInfo = CS.ColliderComponent((0, [0, 0, 10, 100]))
    Info = COMP.GameObject(WHITE, 20, 20)
    Info.transform = tran
    Info.listComp.append(dInfo)
    Info.listComp.append(pInfo)
    Info.listComp.append(cInfo)
    listObject.append(Info)
    listDraw.add(Info)
    playerObject = Info
    playerPhy = pInfo


def ResetLevel():
    global playerObject
    global listEnemy
    playerObject.transform.location = [0, 400]
    for enemy in listEnemy:
        enemy.transform.location = [650, 380]
