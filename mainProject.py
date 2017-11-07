import pygame
import random
import SetupScene as SetSce
import DrawScript as DS
import PhysicsScript as PS
import ColliderScript as CS
import Components as COMP
pygame.init()

print(SetSce.name)

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

endGame = False
change = True

Mouse = [(0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0]
# up,down,left,right,space
Key = [0, 0, 0, 0, 0]


# IableObject :
# string : msg
# point : startPosition  ( for area to draw)
# point : end position ( for area to draw)
# color : Color of object to be draw
# color : Color of text.
# DrawInfo:
#       Type : int ( rect, circle, )
#       Info : object.
#


def QuitGame():
    global gameExit
    gameExit = True


# set transform
tran = COMP.Transform()
tran.location = [75, 10]
# setdraw info (0,[type,info])
# Type : 0 -> info (color,[width, leng])
# Type : 1 -> info (color,radius)
dInfo = DS.DrawComponent([0, (darkGreen, [50, 20])])
# add Physics info (1, weight,velocity,drag)
pInfo = PS.PhysicsComponent([1, [0, 0], 0.1])
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


tran1 = COMP.Transform()
tran1.location = [275, 10]
dInfo1 = DS.DrawComponent([1, (darkGreen, 25)])
pInfo1 = PS.PhysicsComponent([0, [0, 0], 0.1])


Info1 = COMP.GameObject()
Info1.transform = tran1
Info1.listComp.append(dInfo1)
Info1.listComp.append(pInfo1)

SetSce.listObject.append(Info1)


playerChar = SetSce.listObject[1]
playerPhys = playerChar.GetComponent("PhysicsComponent")


# Call to draw object in screen.
# Info [0] : int , Type of object ( rect, circle, )
# Info [1] : transform


def UpdateRender():
    DS.surf.fill((255, 255, 255))
    for x in SetSce.listObject:
        for comps in x.listComp:
            comps.Active(x.transform)


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
                Key[0] = 1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Key[1] = 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Key[2] = 1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Key[3] = 1
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
    print(SetSce.listObject[0].listComp)
    if(Key[2] == 1):
        playerPhys.SetVelocity(playerChar.transform,
                               [-1, playerPhys.Info[1][1]])
    elif(Key[3] == 1):
        playerPhys.SetVelocity(playerChar.transform, [
                               1, playerPhys.Info[1][1]])
    elif(Key[0] == 1):
        playerPhys.SetVelocity(playerChar.transform, [
                               playerPhys.Info[1][0], -1])
    elif(Key[1] == 1):
        playerPhys.SetVelocity(playerChar.transform, [
            playerPhys.Info[1][0], 1])
    else:
        playerPhys.SetVelocity(playerChar.transform, [0, 0])

    #---- check if mouse is pressed on an interactable oject -----
    # if Mouse[1] == 1:
    # for index, x in enumerate(SetSce.listObject):
    #     if x[1][0] < Mouse[0][0] < x[1][0] + x[2][0] and x[1][1] < Mouse[0][1] < x[1][1] + x[2][1]:
    #         x[5](x, index)
    #----- If right mouse click.
    if Mouse[3] == 1:
        print(Mouse[0])
    # ===================== Apply physics =====================

    # ===================== Update and draw =====================
    if(change):
        UpdateRender()
    #-----------game end---------------
    pygame.display.update()
    clock.tick(30)

pygame.quit()
