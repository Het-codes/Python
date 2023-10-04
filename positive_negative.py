print("CHECK WEATHER THE NUMBER IS POSITIVE OR NEGATIVE OR ZERO")

a= int(input("Enter value: "))

if a!=0:
    if a>0:
        print(a," is positive")
    else:
        print(a," is negative")
else:
    print(a," is zero")
