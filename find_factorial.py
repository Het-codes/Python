print("FIND FACTORIAL")

a = int(input("Enter value: "))

j = a
i = a

while i>1 :
    i-=1
    j*=i

print("Factorial of",a,"is",j)

print("-------------------------------------------------------------------------------")

f=1

for x in range(1,a+1):
    f = f * x
print("Factorial of",a,"is0",f)
