import pygame
import Components as COMP
import SetupScene as SetSce
screenSize_x = 800
screenSize_y = 600
screen = pygame.display.set_mode((screenSize_x, screenSize_y))

bgImage = pygame.image.load("Snake_Cave_Background.jpg").convert()


def setupSurface(x, y):
    screenSize_x = x
    screenSize_y = y
    screen = pygame.display.set_mode((screenSize_x, screenSize_y))

    # define the function blocks


def DrawBackground():
    screen.blit(bgImage, [0, 0])
# Draw rectabngle,
# tran : transform of object
# Info : [color,[width, length]]


def DrawTexture(tran, info):
    screen.blit(info[0], tran.location)


def DrawRectangle(tran, Info):
    """ Draw Rectangle:
        tran : transform of object
        Info : [color,[width, length]]"""

    pygame.draw.rect(screen, Info[0], [tran.location[0],
                                       tran.location[1], Info[1][0], Info[1][1]])

# Draw circle:
# tran : transform of object
# Info : [color,radius]


def DrawCircle(tran, Info):
    """ Draw circle:
        tran : transform of object
        Info : [color,radius]"""
    pygame.draw.circle(
        screen, Info[0], [int(tran.location[0]), int(tran.location[1])], Info[1])


# map the inputs to the function blocks
options = {0: DrawRectangle,
           1: DrawCircle,
           2: DrawTexture
           }

# Call to draw object in screen.
# Info [0] : int , Type of object ( rect, circle, )
# Info [1] : transform


def DrawCall(trans, Info):
    options[Info[0]](trans, Info[1])


class DrawComponent(COMP.BaseComponent):
    Info = []

    def __init__(self, Info):
        self.Info = Info
        self.name = "DrawComponent"

    def Active(self, trans):
        DrawCall(trans, self.Info)
