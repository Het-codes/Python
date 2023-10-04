print("CHECK WEATHER THE NUMBER IS PRIME OR NOT")

a = int(input("Enter value: "))
b=0
for i in range(2,a):
    if a%i==0:
        #print(a,"is a prime number")
        b=1
        break

if b!=1:
    print(a,"is prime number")
else:
    print(a,"is Not prime number")
    
    
