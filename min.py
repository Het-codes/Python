print("FIND MINIMUM VALUE")

a=input("Enter first value: ")
b=input("Enter second value: ")
c=input("Enter third value: ")

if a<b:
    if a<c:
        print(a," is the lowest value")
    else:
        print(c," is the lowest value")
else:
    if b<c:
        print(b," is the lowest value")
    else:
        print(c," is the lowest value")
