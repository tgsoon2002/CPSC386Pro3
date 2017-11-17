import pygame


class Vec2D:
    x = 0
    y = 0

    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY


class Transform:
    location = Vec2D(0, 0)
    rotation = 0,
    scale = Vec2D(0, 0)


class BaseComponent:
    name = "baseComponent"


class GameObject(pygame.sprite.Sprite):
    transform = Transform
    listComp = []
    objectName = ""

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill([0, 0, 0])
        self.rect = self.image.get_rect()
        self.transform = Transform()
        self.listComp = []

        

    def GetComponent(self, type):
        for comp in self.listComp:
            if(comp.name == type):
                return comp

    def UpdateComponent(self):
        for comp in self.listComp:
            print(comp)

    def setPosition(self, x, y):
        self.transform.location = [x, y]
        self.rect.x = x
        self.rect.y = y
