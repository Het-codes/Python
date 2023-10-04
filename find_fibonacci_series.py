print("FIND FIBONACCI SERIES")

a = int(input("Enter value: "))

i = 1
b = 0
c = 1

print("Fibonacci series:",c,",",end="")
      
while i<a :
    i+=1
    d = b+c
    b = c
    c = d
    print(d,end=",")
