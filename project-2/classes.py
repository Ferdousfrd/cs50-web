#practicing classes in python

class capacity():
    def __init__(self, tickets, passengers):
        self.a = tickets
        self.b = passengers

soldTicket = int(input("Enter amount of tickets been sold: "))
biman = capacity(300, soldTicket)

print(f"Total tickets are, {biman.a}")
print(f"Total tickets been sold, {biman.b}")

if biman.b < biman.a :
    print("There are still tickets available!")
else :
    print("No more tickets!")
