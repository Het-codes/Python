print("CHECK YOUR LUCKY NUMBER")

import random

a = random.randrange(1,11)
#print(a)

b = int(input("Enter your number "))

if b==a:
    print(b,"is your lucky number")
else:
    print(b,"is not your lucky number")
