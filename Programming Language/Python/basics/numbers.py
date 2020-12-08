from math import *

num0 = 10
num1 = 10.3
num2 = 10.5
num3 = 10.7

# remainder, floor value
print(num0 % 3, num0 // 3)

# integer to string
print(f"my number: {num0}")
print("my number: " + str(num0))

# power
print(pow(num0, 2))

# round, floor, ceil (requires "math" module)
print(round(num1), round(num2), round(num3))
print(floor(num1), floor(num2), floor(num3))
print(ceil(num1), ceil(num2), ceil(num3))