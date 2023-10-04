print("MATHS FUMCTION")

print("--------------")

print("FIND SQUARE ROOT")

import math

a = int(input("Enter value: "))

print(math.sqrt(a))

print("--------------------------------------------------------------")

print("FIND POWER")

b = int(input("Enter base and power: "))

print("Answer is",math.pow(b,b))

print("--------------------------------------------------------------")

print("PERFORM TRIGNOMETRIC FUNCTION")

c = int(input("Enter value: "))
d = input("Enter trignometric function: ")

if d=="sin":
    print("Sine of the value is",math.sin(c))
    
elif d=="cos":
    print("Cosine of the value is",math.cos(c))

elif d=="tan":
    print("Tangent of the value is",math.tan(c))

else:
    print("Invalid operation")

print("--------------------------------------------------------------")













