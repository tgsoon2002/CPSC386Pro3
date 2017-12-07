import pygame
from pygame import *
import random
import SetupScene as SetSce
import DrawScript as DS
import PhysicsScript as PS
import Components as COMP
import random
from timeit import default_timer
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
global time_to_spawn
time_to_spawn = 0;
endGame = False
change = True

moveVelocity = 6

global gameTime
gameTime = 0

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
    global gameTime
    hit =  playerChar.CheckCollider(SetSce.listEnemy)
    if hit == True :
        SetSce.ResetLevel()
        gameTime = 0
        print(playerChar.rect)
    # hit = playerChar.CheckCollider(SetSce.listEnemy)
    # update velocity base on force
    playerPhys.ApplyGravity()
    # apply velocity to transform.
    playerPhys.ApplyVelocity(playerChar.rect)
    #check velocity if touch platform
    playerChar.CheckCollidePlatform(SetSce.listPlatformCollider, playerPhys)


#---------------- Setup value ------------------------


while not gameExit:

    dt = clock.tick(30)/1000.0
    time_to_spawn += dt
    gameTime += dt

    rand = random.random()
    # ===================== Input =====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Key[0] += 1
                playerPhys.Jump([playerPhys.Info[1][0], -moveVelocity])
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                SetSce.PlayerCrounch()
                Key[1] += 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Key[2] += 1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Key[3] += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Key[0] = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                SetSce.PlayerStand()
                Key[1] = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Key[2] = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Key[3] = 0
    # ===================== Logic =====================
    if(Key[2] == 1): #left key
        playerPhys.SetVelocity( [-moveVelocity, playerPhys.Info[1][1]])
    elif(Key[3] == 1): # right key
        playerPhys.SetVelocity([moveVelocity, playerPhys.Info[1][1]])
    else:
        playerPhys.SetVelocity([0,  playerPhys.Info[1][1]])

    if(playerChar.rect.x >= DS.screenSize_x):
        gameTime = 0
        SetSce.ResetLevel()

    # make all enemy move to the left.
    for enemy in SetSce.listEnemy:
        enemy.rect.x -= 5
        # ===================== Apply physics =====================
        # SetSce
    ApplyPhysics()
    # ===================== Update and draw =====================

    if(change):
        DS.DrawBackground()
        SetSce.ReDraw()


    if( time_to_spawn > 1):
        time_to_spawn -= 1
        if(rand < .15):
            SetSce.AddEnemy(5)
        elif( rand < .5):
            SetSce.AddEnemy(3)
        elif(rand < .75):
            SetSce.AddEnemy(5)
            SetSce.AddEnemy(3)

    timer = basicfont.render(str(gameTime), True, textColor)

    DS.screen.blit(timer, (0,0))
    #-----------game end---------------
    pygame.display.update()


pygame.quit()
