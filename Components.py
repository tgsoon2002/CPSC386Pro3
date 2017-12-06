import pygame
class BaseComponent:
    name = "baseComponent"


class GameObject(pygame.sprite.Sprite):
    listComp = []
    objectName = ""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([0, 0])
        self.image.fill([0, 0, 0])
        self.rect = self.image.get_rect()
        self.listComp = []

    def ChangeSprite (self, newImage):
        self.image = newImage
        self.rect = self.image.get_rect()
        
    def SetSprite(self, newImage):
        self.image = newImage
        self.rect = self.image.get_rect()

    def SetSolid(self, color, width, height):
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def SetLocation ( self, location):
        self.rect.x = location[0]
        self.rect.y = location[1]

    def GetComponent(self, type):
        for comp in self.listComp:
            if(comp.name == type):
                return comp

    def UpdateComponent(self):
        for comp in self.listComp:
            print(comp)

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

class PlayerObject(GameObject):
    def __init__(self):
        super(PlayerObject, self).__init__()
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([x, y])
        self.image.fill([0, 0, 0])
        self.rect = self.image.get_rect()
        self.listComp = []
    def CheckCollider ( self,enemyList):
        block_hit_list = pygame.sprite.spritecollide(self, enemyList, False)
        
        # if block_hit_list
        for block in block_hit_list:
            if block.objectName == "alien":
                print(block_hit_list)
                return True
        return False
        

