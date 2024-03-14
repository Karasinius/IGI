import circle
import square
import sys
args = sys.argv[1:]
if args:
    val = int(args[0])
    print(f"Square area of square with side = {val} equals {square.area(val)} " )
    print(f"Perimeter of square with side = {val} equals {square.perimeter(val)} " )
    print(f"Cirlce area of circle with radius = {val} equals {circle.area(val)} " )
    print(f"Circle area of side = {val} equals {circle.perimeter(val)} " )
else:
    print("INVALID ARGUMENTS")

