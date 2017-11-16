import pygame
import DrawScript as DS
import PhysicsScript as PS
import ColliderScript as CS
import Components as COMP
name = "scene"
listObject = []


# basicfont = pygame.font.SysFont(None, 40)
darkGreen = (0, 200, 0)
WHITE = (255, 255, 255)
brightGreen = (0, 255, 0)
boardColor = (244, 66, 95)
lightGreen = (107, 244, 65)
textColor = (255, 0, 0)
image = pygame.image.load("cavemanSprite.png").convert()
image.set_colorkey(WHITE)


def addObject(obj):
    listObject.append(obj)


def LoadLevel():
    # set transform
    tran = COMP.Transform()
    tran.location = [10, 10]
    # setdraw info (0,[type,info])
    # Type : 0 -> info (color,[width, leng])
    # Type : 1 -> info (color,radius)
    dInfo = DS.DrawComponent([2, (image, [20, 20])])
    # add Physics info (1, [weight,velocity,drag],layer)
    pInfo = PS.PhysicsComponent([1, [0, 0], [0, 0], 0.01], "platform")
    # add collider info (2,(type,Info))
    # 0 : rect [offsetx,offsety,width,length],
    # 1 : circle [offsetx, offsety,radius]
    cInfo = CS.ColliderComponent((0, [0, 0, 10, 100]))
    Info = COMP.GameObject()
    Info.transform = tran
    Info.listComp.append(dInfo)
    Info.listComp.append(pInfo)
    Info.listComp.append(cInfo)
    listObject.append(Info)
    # append(Info.GetComponent("ColliderComponent"))
    AddObject()


def AddObject():
    # add the ground
    Info1 = COMP.GameObject()
    Info1.transform = COMP.Transform()
    Info1.transform.location = [0, 500]
    Info1.listComp.append(DS.DrawComponent([0, (textColor, [500, 120])]))
    Info1.listComp.append(CS.ColliderComponent((0, [0, 0, 500, 120])))
    listObject.append(Info1)
