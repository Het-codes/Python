print("FIND YOUR AGE")

import datetime

a = int(input("Enter your birth year: "))
x = datetime.datetime.now()

print("Your age is",x.year-a)


