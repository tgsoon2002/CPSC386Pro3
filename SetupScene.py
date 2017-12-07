import pygame
import DrawScript as DS
import PhysicsScript as PS
import Components as COMP
name = "scene"
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
playerImage = pygame.image.load("cavemanSprite.png").convert_alpha()
playerCrounch = pygame.image.load("cavemanSprite_Crounch.png").convert_alpha()
alien = pygame.image.load("alien.png")
flyingAlien = pygame.image.load("Flying_Alien.png")
playerImage.set_colorkey(WHITE)
playerObject = ()

playerPhy = ()


def LoadLevel():
    # set transform
    AddPlayer()
    # append(plObject.GetComponent("ColliderComponent"))
    AddObject()

def AddEnemy(enemy):
    Info2 = COMP.GameObject()
    if(enemy == 5):
        Info2.SetSprite(flyingAlien)
        Info2.SetLocation([750, 215])
    else:
        Info2 .SetSprite(alien)
        Info2.SetLocation([750, 410])

    Info2.objectName = "alien"
    listDraw.add(Info2)
    listEnemy.append(Info2)

def AddObject():
    global listDraw
    global listPlatformCollider
    global listEnemy
    # add the ground
    ground = COMP.GameObject()
    ground.SetSolid(RED,800,300)
    ground.rect.y = 500

    # Create enemy.
    Info2 = COMP.GameObject()
    Info2.SetSprite(alien)
    Info2.objectName = "alien"
    Info2.SetLocation([750,410])
    
    listDraw.add(ground)
    listDraw.add(Info2)
    listPlatformCollider.add(ground)
    listEnemy.append(Info2)


def AddPlayer():
    global playerPhy
    global playerObject
    # ============
    pInfo = PS.PhysicsComponent([1, [0, 0], [0, 0], 0.01], "platform")
    
    # create object
    plObject = COMP.PlayerObject(42,75)
    plObject.SetSprite(playerImage)
    plObject.rect.y = 380
    
    # add component to object
    plObject.listComp.append(pInfo)
    
    # add player object to list.
    listDraw.add(plObject)
    playerObject = plObject
    playerPhy = pInfo


def ResetLevel():
    global playerObject
    global listEnemy
    playerObject.rect.x = 0
    for enemy in listEnemy:
        enemy.rect.x = 650
        

def ReDraw():
    listDraw.draw(DS.screen)

def PlayerCrounch(): 
    currentPos = playerObject.rect;
    print(currentPos)
    playerObject.SetSprite(playerCrounch)
    playerObject.rect.x = currentPos.x
    playerObject.rect.y = currentPos.y

def PlayerStand():
    currentPos = playerObject.rect;
    playerObject.SetSprite(playerImage)
    playerObject.rect.x = currentPos.x
    playerObject.rect.y = currentPos.y
