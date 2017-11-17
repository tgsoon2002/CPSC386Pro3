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

inputInfo = {'horizontal': 0, 'vertical': 0}

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


endGame = False
change = True

moveVelocity = 6


Mouse = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
# up,down,left,right,space
Key = [0, 0, 0, 0, 0]


def QuitGame():
    global gameExit
    gameExit = True


# pygame.mouse.set_visible(False)
SetSce.LoadLevel()

playerChar = SetSce.playerObject
playerPhys = SetSce.playerPhy

listOtherObject = SetSce.listEnemy




def ApplyPhysics():
    # check for collider
    # for x in SetSce.listEnemy:
    #     # print(x.listComp)
    #     for comps in x.listComp:
    #         if comps.name == "ColliderComponent":
                
                # result = comps.CheckCollider(
                #     x.transform, playerChar.GetComponent("ColliderComponent"), playerChar.transform)
                # if result:
                #     SetSce.ResetLevel()
                # print(result)
    hit =  playerChar.CheckCollider(SetSce.listEnemy)
    if hit == True :
        SetSce.ResetLevel()
    # update velocity base on force
    playerPhys.ApplyGravity()
    # apply velocity to transform.
    playerPhys.ApplyVelocity(playerChar.rect)


#---------------- Setup value ------------------------


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
                playerPhys.Jump([playerPhys.Info[1][0], -moveVelocity])
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
    if(Key[2] == 1):
        playerPhys.SetVelocity( [-moveVelocity, playerPhys.Info[1][1]])
    elif(Key[3] == 1):
        playerPhys.SetVelocity([moveVelocity, playerPhys.Info[1][1]])
    else:
        playerPhys.SetVelocity([0,  playerPhys.Info[1][1]])

    #---- check if mouse is pressed on an interactable oject -----
    # if Mouse[1] == 1:
    # for index, x in enumerate(SetSce.listObject):
    #     if x[1][0] < Mouse[0][0] < x[1][0] + x[2][0] and x[1][1] < Mouse[0][1] < x[1][1] + x[2][1]:
    #         x[5](x, index)
    #----- If right mouse click.
    # if Mouse[3] == 1:
    #     print(Mouse[0])
    for enemy in SetSce.listEnemy:
        enemy.rect.x -= 5
        # ===================== Apply physics =====================
        # SetSce
    ApplyPhysics()
    # ===================== Update and draw =====================

    if(change):
        DS.DrawBackground()
        SetSce.ReDraw()
    #-----------game end---------------
    pygame.display.update()
    clock.tick(30)

pygame.quit()
