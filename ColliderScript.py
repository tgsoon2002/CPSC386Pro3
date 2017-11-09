import Components as COMP
import math


class ColliderComponent(COMP.BaseComponent):
    """# add collider info (2,(type,Info))
    # 0 : rect [offsetx,offsety,width,length],
    # 1 : circle [offsetx, offsety,radius]
    """
    Type = 2
    Info = []

    def __init__(self, Info):
        self.Info = Info
        self.name = "ColliderComponent"

    def CheckCollider(self, trans, otherColl, otherTrans):
        self.CompareCircleToCircle(trans, otherTrans, 3, 3)

    def CompareCircleToCircle(self, trans1, trans2, r1, r2):
        magnitude = math.sqrt(math.pow(math.fabs(
            trans1.location[0] - trans2.location[0]), 2.0) + math.pow(math.fabs(trans1.location[1] - trans2.location[1]), 2.0))
        # print(magnitude)
