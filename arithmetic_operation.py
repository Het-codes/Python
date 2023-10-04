print("ARITHMETIC OPERATIONS")

a= int(input("enter first value "))
b= int(input("enter second value "))
c= input("enter arithmetic operation ")

if c == "+" :
    print("Addition is",(a+b))
elif c == "-":
    print("Subtraction is",(a-b))
elif c == "*":
    print("Multiplication is",(a*b))
elif c == "/":
    print("Division is",(a/b))
elif c == "%":
    print("Mod is",(a%b))
else:
    print("Invilid operation")
    
