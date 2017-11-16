import Components as comp

#(1, weight, velocity, drag)


class PhysicsComponent (comp.BaseComponent):

    type = 1
    """add Physics info (weight,velocity,force,drag)"""
    Info = []
    layer = ""
    falling = True
    justJump = False

    def __init__(self, Info, layer):
        self.Info = Info
        self.name = "PhysicsComponent"

    def SetForce(self, force):
        self.Info[2][0] = force[0] * self.Info[0]
        self.Info[2][1] = force[1] * self.Info[0]
        # print(self.Info[2])

    def SetVelocity(self, trans, Info):
        self.Info[1] = Info
        # print(self.Info[1])

    def ApplyGravity(self):
        self.Info[2][1] = self.Info[2][1] + (0.01 * self.Info[0])
        self.Info[1][0] += self.Info[2][0]
        self.Info[1][1] += self.Info[2][1]
        # print(self.Info[2])

    def ApplyVelocity(self, trans):
        # print(self.Info[2])
        trans.location[0] += self.Info[1][0]
        if trans.location[1] < 500.0 and self.Info[1][1] > 0:
            self.falling = True
            trans.location[1] += self.Info[1][1]
        elif self.Info[1][1] < 0:
            trans.location[1] += self.Info[1][1]
        else:
            self.Info[2][1] = 0
            self.falling = False
            self.justJump = False

    def Jump(self, trans, Info):
        if self.justJump == False:
            self.Info[1] = Info
            self.justJump = True
