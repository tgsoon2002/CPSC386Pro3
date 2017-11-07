import Components as COMP


class ColliderComponent(COMP.BaseComponent):
    Type = 2
    Info = []

    def __init__(self, Info):
        self.Info = Info
        self.name = "ColliderComponent"

    def Active(self, trans):
        print("check collider")
