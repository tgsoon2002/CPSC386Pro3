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

    def SetSprite(self, newImage):
        self.image = newImage
        self.rect = self.image.get_rect()

    def SetSolid(self, color, width, height):
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

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
        super().__init__()
    def CheckCollider ( self,enemyList):
        block_hit_list = pygame.sprite.spritecollide(self, enemyList, False)
        
        # if block_hit_list
        for block in block_hit_list:
            if block.objectName == "alien":
                print(block.objectName)
                return True
        return False
            # If we are moving right,
        #     # set our right side to the left side of the item we hit
        #     if self.change_x > 0:
        #         self.rect.right = block.rect.left
        #     elif self.change_x < 0:
        #         # Otherwise if we are moving left, do the opposite.
        #         self.rect.left = block.rect.right
