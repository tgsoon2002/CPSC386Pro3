import Components as comp

#(1, weight, velocity, drag)


class PhysicsComponent (comp.BaseComponent):
    type = 1
    Info = []

    def __init__(self, Info):
        self.Info = Info
        self.name = "PhysicsComponent"

    def SetVelocity(self, trans, Info):
        trans.location[0] += Info[0]
        trans.location[1] += Info[1]

    def Active(self, trans):
        vel = self.Info[1]
        # # apply physics
        vel[1] += self.Info[0] * 0.1
        # # update velocity
        self.Info[1] = vel
        # # apply gravity
        trans.location[0] += vel[0]
        trans.location[1] += vel[1]
