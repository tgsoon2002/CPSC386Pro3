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


class GameObject:
    transform = Transform
    listComp = []

    def __init__(self):
        self.transform = Transform()
        self.listComp = []

    def GetComponent(self, type):
        for comp in self.listComp:
            if(comp.name == type):
                return comp

    def UpdateComponent(self):
        for comp in self.listComp:
            print(comp)
