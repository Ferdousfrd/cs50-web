#practicing error exception handling

import sys

try:
    x = int(input("Please give value of X: "))
    y = int(input("Please give value of Y: "))
except ValueError:
    print("GIve an interger please!")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Error: Cannot devide by 0")
    sys.exit(1)

print(f"{x}/{y} is : {result}")
