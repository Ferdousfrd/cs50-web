class Robot:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def introSelf(self):
        print(f"Hello, I am {self.name}. I am {self.weight} pounds and my color is {self.color}.")

class Person:
    def __init__(self, name, personality, isSitting, robotOwned):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned

    def sit_down(self):
        self.isSitting == True

    def stand_up(self):
        self.isSitting == False

robot1 = Robot("Tom", 40, "Red")
robot2 = Robot("Roger", 30, "DarkGrey")

emily = Person("Emily", "strict", True, robot1)
devil = Person("Headson", "bad", False, robot2)

