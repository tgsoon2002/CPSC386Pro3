import Components as COMP
import math


class ColliderComponent(COMP.BaseComponent):
    """# add collider info (2,(type,Info))
    # 0 : rect [offsetx,offsety,width,length],
    # 1 : circle [offsetx, offsety,radius]
    """

    Type = 1
    Info = []

    def __init__(self, Info):
        self.Info = Info[1]
        self.Type = Info[0]
        self.name = "ColliderComponent"

    def CheckCollider(self, trans, otherColl, otherTrans):
        # self.CompareCircleToCircle(trans, otherTrans, 3, 3)
        """ Check Collider return True/False
            It will check between Circle or Rect with orther Circle or Rect"""
        if(self.Type == 1):
            if (otherColl.Type == 1):
                print("Check circle to circle")
                return self.CompareCircleToCircle(
                    trans, otherTrans, self.Info, otherColl.Info)
            if(otherColl.Type == 0):
                return self.CompareRectToCirCle(
                    trans, otherTrans, self.Info, otherColl.Info)
        elif(self.Type == 0):
            if (otherColl.Type == 1):
                return self.CompareRectToCirCle(
                    trans, otherTrans, self.Info, otherColl.Info)
            if(otherColl.Type == 0):
                return self.CompareRectToRect(
                    trans, otherTrans, self.Info, otherColl.Info)

    def CompareCircleToCircle(self, trans1, trans2, r1, r2):
        # print(r1[1])
        # print(r2[1])
        # print(r2[1][1])
        pos1 = [trans1.location[0] + r1[0], trans1.location[1] + r1[1]]
        pos2 = [trans2.location[0] + r2[0], trans2.location[1] + r2[1]]
        magnitude = self.GetMagnitude(pos1, pos2)
        return magnitude > (r1[2] + r2[2])
        # print(magnitude)

    def CompareRectToCirCle(self, cTrans, rTrans, cInfo, rInfo):
        """ cTrans,rTrans,cInfo,rInfo """
        offSet = [rTrans.location[0] + rInfo[0], rTrans.location[1] + rInfo[1]]
        if self.GetMagnitude(offSet, cTrans.location) <= cInfo[2]:
            return True
        if self.GetMagnitude([offSet[0] + rInfo[2], offSet[1]], cTrans.location) <= cInfo[2]:
            return True
        if self.GetMagnitude([offSet[0], offSet[1] + rInfo[3]], cTrans.location) <= cInfo[2]:
            return True
        if self.GetMagnitude([offSet[0] + rInfo[2], offSet[1] + rInfo[3]], cTrans.location) <= cInfo[2]:
            return True
        return False

    def CompareRectToRect(self, rTrans1, rTrans2, rInfo1, rInfo2):
        pos1 = [rTrans1.location[0] + rInfo1[0],
                rTrans1.location[1] + rInfo1[1]]
        pos2 = [rTrans2.location[0] + rInfo2[0],
                rTrans2.location[1] + rInfo2[1]]
        difx = math.fabs(pos1[0] - pos2[0])
        dify = math.fabs(pos1[1] - pos2[1])
        print(pos1)
        print(pos2)
        if pos1[0] < pos2[0]:
            if pos1[1] > pos2[1]:
                if difx < rInfo1[2] and dify < rInfo1[3]:
                    return True
            else:
                if difx < rInfo1[2] and dify < rInfo2[3]:
                    return True
        else:
            if pos1[1] > pos2[1]:
                if difx < rInfo2[2] and dify < rInfo1[3]:
                    return True
            else:
                if difx < rInfo2[2] and dify < rInfo2[3]:
                    return True
        return False

    def GetMagnitude(self, pos1, pos2):
        return math.sqrt(math.pow(math.fabs(
            pos1[0] - pos2[0]), 2.0) + math.pow(math.fabs(pos1[1] - pos2[1]), 2.0))
