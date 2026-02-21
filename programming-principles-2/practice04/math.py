import math
import random

# 1
degree = random.randint(0, 360)
print(f"Input degree: {degree}\nOutput radian: {math.radians(degree):.6f}\n")

# 2
height = random.randint(1, 10)
baseFirst = random.randint(1, 10)
baseSecond = random.randint(1, 10)
area = ((baseFirst + baseSecond) / 2) * height
print(f"Input height: {height}\nInput first base: {baseFirst}\nInput second base: {baseSecond}\nTrapezoidal area: {area:.1f}\n")

# 3 
sides = random.randint(3, 10)
sideLength = random.randint(1, 25)
area = (sides * pow(sideLength, 2)) / (4 * math.tan(math.pi / sides))
print(f"Input sides: {sides}\nInput side length: {sideLength}\nThe area of the polygon is: {area:.2f}\n")

# 4
baseLength = random.randint(1, 10)
height = random.randint(1, 10)
area = baseLength * height
print(f"Input base length: {baseLength}\nInput height: {height}\nThe area of the parallelogram is: {area:.2f}")