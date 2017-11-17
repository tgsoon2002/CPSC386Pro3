import pygame
import DrawScript as DS
import PhysicsScript as PS
import ColliderScript as CS
import Components as COMP
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
    # append(plObject.GetComponent("ColliderComponent"))
    AddObject()


def AddObject():
    global listDraw
    global listPlatformCollider
    global listEnemy
    # add the ground
    Info1 = COMP.GameObject()
    Info1.SetSolid(RED,800,300)
    Info1.rect.y = 500
    # Info1.listComp.append(DS.DrawComponent([0, (RED, [800, 120])]))
    Info1.listComp.append(CS.ColliderComponent((0, [0, 0, 500, 120])))

    # create a circle object
    Info2 = COMP.GameObject()
    
    # Info1.listComp.append(PS.PhysicsComponent([0, [0, 0], 0.1], "player"))
    
    Info2.SetSprite(alien)
    Info2.objectName = "alien"
    Info2.rect.x = 650
    Info2.rect.y = 380
    Info2.listComp.append(CS.ColliderComponent((0, [0, 0, 20, 30])))
    listDraw.add(Info1)
    listDraw.add(Info2)
    listPlatformCollider.add(Info1)
    listEnemy.append(Info2)


def AddPlayer():
    global playerPhy
    global playerObject
    global listObject
    pInfo = PS.PhysicsComponent([1, [0, 0], [0, 0], 0.01], "platform")
    cInfo = CS.ColliderComponent((0, [0, 0, 10, 100]))
    plObject = COMP.PlayerObject()

    plObject.SetSprite(playerImage)
    plObject.rect.y = 380
    # plObject.listComp.append(dInfo)
    plObject.listComp.append(pInfo)
    plObject.listComp.append(cInfo)
    listObject.append(plObject)
    listDraw.add(plObject)
    playerObject = plObject
    playerPhy = pInfo


def ResetLevel():
    global playerObject
    global listEnemy
    playerObject.rect.x = 0
    playerObject.rect.y = 400
    for enemy in listEnemy:
        enemy.rect.x = 650
        

def ReDraw():
    listDraw.draw(DS.screen)
