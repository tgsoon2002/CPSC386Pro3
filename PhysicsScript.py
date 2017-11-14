import Components as comp

#(1, weight, velocity, drag)


class PhysicsComponent (comp.BaseComponent):

    type = 1
    """add Physics info (weight,velocity,force,drag)"""
    Info = []
    layer = ""
    falling = True

    def __init__(self, Info, layer):
        self.Info = Info
        self.name = "PhysicsComponent"

    def SetForce(self, force):
        self.Info[2][0] = force[0] * self.Info[0]
        self.Info[2][1] = force[1] * self.Info[0]
        print(self.Info[2])

    def SetVelocity(self, trans, Info):
        self.Info[1] = Info
        print(self.Info[1])

    def ApplyGravity(self):
        self.Info[2][1] = self.Info[2][1] + (0.01 * self.Info[0])
        self.Info[1][0] += self.Info[2][0]
        self.Info[1][1] += self.Info[2][1]
        print(self.Info[2])

    def ApplyVelocity(self, trans):
        # print(self.Info[2])
        trans.location[0] += self.Info[1][0]
        if trans.location[1] < 400.0 and self.Info[1][1] > 0:
            self.falling = True
            trans.location[1] += self.Info[1][1]
        elif self.Info[1][1] < 0:
            # print("Jump")

            trans.location[1] += self.Info[1][1]
        else:
            # print("Not falling")
            self.Info[2][1] = 0
            self.falling = False

    # def Active(self, trans):
    #     self.ApplyGravity()
    #     # print(trans.location[0])
        # if(trans.location[0] < 500):
        # self.ApplyVelocity(trans)
