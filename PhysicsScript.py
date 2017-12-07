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
        print (Info)
        self.Info = Info
        self.name = "PhysicsComponent"

    def SetForce(self, force):
        self.Info[2][0] = force[0] * self.Info[0]
        self.Info[2][1] = force[1] * self.Info[0]
        # print(self.Info[2])

    def SetVelocity(self, Info):
        self.Info[1] = Info
       

    def ApplyGravity(self):
        self.Info[2][1] = self.Info[2][1] + (0.013 * self.Info[0])
        self.Info[1][0] += self.Info[2][0]
        self.Info[1][1] += self.Info[2][1]
        # print(self.Info[2])

    def ApplyVelocity(self, rect):
        rect.x += self.Info[1][0]
        # if the force is point down
        rect.y += self.Info[1][1]
       
        

    def Jump(self, Info):
        if self.justJump == False:
            self.Info[1] = Info
            self.justJump = True
