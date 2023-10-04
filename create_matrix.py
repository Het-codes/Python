print("CREATE MATRIX")

a = int(input("Enter value: "))
b = 0

for i in range(1,a+1):
    print(str(i).zfill(2),end=" ")
    if i%3==0:
        print("\n")
    
    b+=i
    
print("\n")
print("---------------------------------------------------------------")
print("Total:",b)

    
