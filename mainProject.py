import pygame
from pygame import *
import random
import SetupScene as SetSce
import DrawScript as DS
import PhysicsScript as PS
import ColliderScript as CS
import Components as COMP
init()

clock = pygame.time.Clock()


#-----------screen setting---------------
DS.setupSurface(800, 600)
# screenSize_x = 800
# screenSize_y = 600
# gameDisplay = pygame.display.set_mode((screenSize_x, screenSize_y))
gameExit = False
#-----------Load image---------------
basicfont = pygame.font.SysFont(None, 40)
darkGreen = (0, 200, 0)
brightGreen = (0, 255, 0)
boardColor = (244, 66, 95)
lightGreen = (107, 244, 65)
textColor = (255, 0, 0)
image = pygame.image.load("cavemanSprite.jpg").convert()
alien = pygame.image.load("alien.gif")

endGame = False
change = True

moveVelocity = 4

listCollider = []

Mouse = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
# up,down,left,right,space
Key = [0, 0, 0, 0, 0]


def QuitGame():
    global gameExit
    gameExit = True


def AddObject():
    Info1 = COMP.GameObject()
    Info1.transform = COMP.Transform()
    Info1.transform.location = [0, 500]
    Info1.listComp.append(DS.DrawComponent([0, (textColor, [5000, 120])]))
    Info1.listComp.append(CS.ColliderComponent((0, [0, 0, 5000, 120])))
    SetSce.listObject.append(Info1)


# set transform
tran = COMP.Transform()
tran.location = [0, 400]
# setdraw info (0,[type,info])
# Type : 0 -> info (color,[width, leng])
# Type : 1 -> info (color,radius)
dInfo = DS.DrawComponent([2, (image, [10, 10])])
# add Physics info (1, [weight,velocity,drag],layer)
pInfo = PS.PhysicsComponent([1, [0, 0], [0, 0], 0.01], "platform")
# add collider info (2,(type,Info))
# 0 : rect [offsetx,offsety,width,length],
# 1 : circle [offsetx, offsety,radius]
cInfo = CS.ColliderComponent((0, [0, 0, 5, 5]))
Info = COMP.GameObject()
Info.transform = tran
Info.listComp.append(dInfo)
Info.listComp.append(pInfo)
Info.listComp.append(cInfo)
SetSce.listObject.append(Info)
listCollider.append(Info.GetComponent("ColliderComponent"))

# create a circle object
Info1 = COMP.GameObject()
Info1.transform = COMP.Transform()
Info1.transform.location = [650, 380]
#Info1.listComp.append(PS.PhysicsComponent([0, [0, 0], 0.1], "player"))
Info1.listComp.append(DS.DrawComponent([2, (alien, 25)]))
SetSce.listObject.append(Info1)

AddObject()

playerChar = SetSce.listObject[0]
playerPhys = playerChar.GetComponent("PhysicsComponent")
playerColl = playerChar.GetComponent("ColliderComponent")


def UpdateRender():
    DS.surf.fill((255, 255, 255))
    for x in SetSce.listObject:
        for comps in x.listComp:
            if comps.name == "DrawComponent":
                comps.Active(x.transform)


def ApplyPhysics():
    for x in SetSce.listObject:
        for comps in x.listComp:
            if comps.name == "PhysicsComponent":
                comps.ApplyGravity()
    # for x in SetSce.listObject:
    #     if x != playerChar:
    #         for comps in x.listComp:
    #             if comps.name == "ColliderComponent":
    #                 comps.CheckCollider(
    #                     x.transform, playerColl, playerChar.transform)
    for x in SetSce.listObject:
        for comps in x.listComp:
            if comps.name == "PhysicsComponent":
                comps.ApplyVelocity(x.transform)


#---------------- Setup value ------------------------


UpdateRender()
while not gameExit:
    # ===================== Input =====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Mouse[event.button] = 1
            Mouse[0] = (event.pos[0], event.pos[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            Mouse[event.button] = 0
            Mouse[0] = (event.pos[0], event.pos[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Key[0] += 1
                playerPhys.SetVelocity(playerChar.transform,
                                       [playerPhys.Info[1][0], -moveVelocity])
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Key[1] += 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Key[2] += 1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Key[3] += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Key[0] = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Key[1] = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Key[2] = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Key[3] = 0
    # ===================== Logic =====================
    # (1, [0, [0, 0], 0.1])
    # print(SetSce.listObject[0].listComp)
    if(Key[0] == 1):
        print(playerPhys.Info[1][0])

    # elif(Key[1] == 1):
    #     playerPhys.SetForce([0, moveVelocity])
    elif(Key[2] == 1):
        playerPhys.SetVelocity(playerChar.transform,
                               [-moveVelocity, playerPhys.Info[1][1]])
    elif(Key[3] == 1):
        playerPhys.SetVelocity(playerChar.transform, [
                               moveVelocity, playerPhys.Info[1][1]])
    else:
        playerPhys.SetVelocity(playerChar.transform, [
            0,  playerPhys.Info[1][1]])

    Info1.transform.location[0] = Info1.transform.location[0] - 2
    #---- check if mouse is pressed on an interactable oject -----
    # if Mouse[1] == 1:
    # for index, x in enumerate(SetSce.listObject):
    #     if x[1][0] < Mouse[0][0] < x[1][0] + x[2][0] and x[1][1] < Mouse[0][1] < x[1][1] + x[2][1]:
    #         x[5](x, index)
    #----- If right mouse click.
    if Mouse[3] == 1:
        print(Mouse[0])
    # ===================== Apply physics =====================
    # SetSce
    ApplyPhysics()
    # ===================== Update and draw =====================

    if(change):
        UpdateRender()
    #-----------game end---------------
    pygame.display.update()
    clock.tick(30)

pygame.quit()
