import Components as comp

#(1, weight, velocity, drag)


class PhysicsComponent (comp.BaseComponent):
    type = 1
    Info = []
    layer = ""
    falling = True

    def __init__(self, Info, layer):
        self.Info = Info
        self.name = "PhysicsComponent"

    def SetVelocity(self, trans, Info):
        self.Info[1] = Info
        print(self.Info[1])

    def ApplyGravity(self):
        if self.falling == True or self.Info[1][1] < 0:
            vel = self.Info[1]
            # # apply physics
            vel[1] += self.Info[0] * 0.1
            # # update velocity
            self.Info[1] = vel

    def ApplyVelocity(self, trans):
        print(self.Info[1])
        trans.location[0] += self.Info[1][0]
        if trans.location[1] < 480.0 and self.Info[1][1] > 0:
            self.falling = True
            trans.location[1] += self.Info[1][1]
        elif self.Info[1][1] < 0:
            print("Jump")
            trans.location[1] += self.Info[1][1]
        else:
            print("not falling")
            self.falling = False

    def Active(self, trans):
        self.ApplyGravity()
        # print(trans.location[0])
        # if(trans.location[0] < 500):
        # self.ApplyVelocity(trans)
