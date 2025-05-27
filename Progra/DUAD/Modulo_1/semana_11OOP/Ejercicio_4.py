class Head:
    def __init__(self):
        self.head= 1

    def __str__(self):
        return "This is the Head"


class Torso:
    def __init__(self):
        self.torso=1

    def __str__(self):
        return "This is the Torso"


class Arm:
    def __init__(self,side):
        self.side=side

    def __str__(self):
        return f'{self.side.capitalize()} arm'


class Hand:
    def __init__(self,side):
        self.side=side
        self.finger=5

    def __str__(self):
        return f'{self.side.capitalize()} hand with {self.finger} fingers'


class Leg:
    def __init__(self,side):
        self.side=side

    def __str__(self):
        return f'{self.side.capitalize()} leg'
        

class Feet:
    def __init__(self,side):
        self.side=side
        self.toes=5

    def __str__(self):
        return f'{self.side.capitalize()} feet with {self.toes} toes'


class Human:
    def __init__(self):
        self.head = Head()
        self.torso = Torso()
        self.right_arm = Arm("right")
        self.left_arm = Arm("left")
        self.right_hand = Hand("right")
        self.left_hand = Hand("left")
        self.right_leg = Leg("right")
        self.left_leg = Leg("left")
        self.right_foot = Feet("right")
        self.left_foot = Feet("left")



human = Human()

print(human.head)
print(human.torso)
print(human.right_arm)
print(human.left_hand)
print(human.right_leg)
print(human.left_foot)