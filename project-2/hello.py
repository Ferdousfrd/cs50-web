#practicing funcions in python
import functionsPage

length= int(input("Give length"))
print(f"You gave, {length}")

width = int(input("Give width"))
print(f"You gave, {width}")

print(f"area is, {functionsPage.area(length,width)}")

for i in range(6):
    print(f"{i} square is, {functionsPage.square(i)}")
