#practicing classes in python

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def addingPass(self, names):
        if not self.openCapacity():
            return False
        self.passengers.append(names)
        return True

    def openCapacity(self):
        return self.capacity-len(self.passengers)



bimanBala = Flight(3)

people = ["jack", "bichi", "sda", "ava"]
for i in people:
    success = bimanBala.addingPass(i)
    if success:
        print(f"We added {i} successfully")
    else:
        print(f"{i} cant board, plane full")
